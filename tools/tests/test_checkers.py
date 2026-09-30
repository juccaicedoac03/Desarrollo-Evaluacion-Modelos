"""Tests for tools/check_notebooks.py and tools/check_links.py on small hand-built inputs."""
import json
import re
import sys
from pathlib import Path

import nbformat
import pytest
from nbformat import v4

TOOLS_DIR = Path(__file__).resolve().parents[1]
SNIPPETS_DIR = TOOLS_DIR / "snippets"
sys.path.insert(0, str(TOOLS_DIR))

import check_links  # noqa: E402
import check_notebooks  # noqa: E402


def snippet(name):
    return (SNIPPETS_DIR / name).read_text(encoding="utf-8").rstrip("\n")


def with_session(text, session):
    return re.sub(r'(?m)^SESSION = "S\d\d"$', f'SESSION = "{session}"', text)


def md(text):
    return v4.new_markdown_cell(text)


def code(text):
    return v4.new_code_cell(text)


def good_lab_cells():
    return [md("# Lab"), code(snippet("setup_lab.py") + '\nensure("transformers")'), code("print('hi')"), md("## Wrap-up")]


def good_challenge_cells(session="S03"):
    return [
        md("# Challenge de la Sesión 03"),
        code(with_session(snippet("setup_challenge.py"), session)),
        code('CONFIG = {"dataset": pick(["a", "b"])}\nprint("Tu configuración personal", CONFIG)'),
        md("## Tarea 1 — Algo (Ejecución técnica)"),
        code("x = 1"),
        code("RESULTS = {'x': 1}"),
        md(snippet("ai_log.md")),
        code(snippet("fingerprint.py")),
    ]


def write_nb(path, cells, **kwargs):
    nb = v4.new_notebook(cells=cells, **kwargs)
    path.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, path)
    return path


def run_nb_checker(capsys, *args):
    code_ = check_notebooks.main([str(a) for a in args])
    return code_, capsys.readouterr().out


# ------------------------------------------------------------------- check_notebooks: good
def test_good_lab_and_challenge_pass(tmp_path, capsys):
    session = tmp_path / "03-transfer-learning"
    write_nb(session / "lab.ipynb", good_lab_cells())
    write_nb(session / "challenge.ipynb", good_challenge_cells("S03"))
    status, out = run_nb_checker(capsys, session)
    assert status == 0
    assert out.count("OK ") == 2 and "FAIL" not in out


def test_challenge_session_value_can_be_any_sNN_when_folder_is_not_a_session(tmp_path, capsys):
    write_nb(tmp_path / "scratch" / "challenge.ipynb", good_challenge_cells("S11"))
    status, out = run_nb_checker(capsys, tmp_path / "scratch")
    assert status == 0, out


def test_lab_notebook_with_startti_client_passes(tmp_path, capsys):
    cells = good_lab_cells() + [code(snippet("startti_client.py")),
                                code('print(startti_run("agent", "hi"))')]
    write_nb(tmp_path / "lab.ipynb", cells)
    status, out = run_nb_checker(capsys, tmp_path)
    assert status == 0, out


def test_scanning_a_directory_skips_other_notebooks(tmp_path, capsys):
    write_nb(tmp_path / "lab.ipynb", good_lab_cells())
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "explore.ipynb").write_text("not even json")
    status, out = run_nb_checker(capsys, tmp_path)
    assert status == 0 and out.count("\n") == 1


# -------------------------------------------------------------------- check_notebooks: bad
def bad_case(tmp_path, capsys, name, cells, **kwargs):
    path = write_nb(tmp_path / name, cells, **kwargs)
    status, out = run_nb_checker(capsys, path)
    return status, out


def test_outputs_and_execution_count_fail(tmp_path, capsys):
    cell = code(snippet("setup_lab.py"))
    cell.outputs = [v4.new_output("stream", name="stdout", text="Device: cpu\n")]
    cell.execution_count = 3
    status, out = bad_case(tmp_path, capsys, "lab.ipynb", [cell])
    assert status == 1
    assert "FAIL" in out and "outputs" in out and "execution_count" in out


def test_lab_without_setup_block_fails(tmp_path, capsys):
    status, out = bad_case(tmp_path, capsys, "lab.ipynb", [md("# Lab"), code("import torch")])
    assert status == 1 and "setup_lab.py" in out


def test_lab_setup_block_must_be_at_the_start_of_the_first_code_cell(tmp_path, capsys):
    status, out = bad_case(tmp_path, capsys, "lab.ipynb", [code("# hi\n" + snippet("setup_lab.py"))])
    assert status == 1 and "setup_lab.py" in out


def test_lab_setup_block_modified_fails(tmp_path, capsys):
    altered = snippet("setup_lab.py").replace("SEED = 42", "SEED = 7")
    status, out = bad_case(tmp_path, capsys, "lab.ipynb", [code(altered)])
    assert status == 1 and "setup_lab.py" in out


def test_lab_with_no_code_cells_fails(tmp_path, capsys):
    status, out = bad_case(tmp_path, capsys, "lab.ipynb", [md("# only markdown")])
    assert status == 1 and "no code cells" in out


def test_startti_call_without_client_block_fails(tmp_path, capsys):
    cells = good_lab_cells() + [code('print(startti_run("agent", "hi"))')]
    status, out = bad_case(tmp_path, capsys, "lab.ipynb", cells)
    assert status == 1 and "startti_client.py" in out


def test_startti_mention_in_comment_or_markdown_is_not_a_call(tmp_path, capsys):
    cells = good_lab_cells() + [md("call startti_run(...) later"), code("# startti_run(agent, 'x')\nx = 1")]
    status, out = bad_case(tmp_path, capsys, "lab.ipynb", cells)
    assert status == 0, out


def test_startti_client_block_modified_fails(tmp_path, capsys):
    altered = snippet("startti_client.py").replace("timeout_s=120", "timeout_s=5")
    cells = good_lab_cells() + [code(altered)]
    status, out = bad_case(tmp_path, capsys, "lab.ipynb", cells)
    assert status == 1 and "startti_client.py" in out


def test_challenge_missing_pieces_are_each_reported(tmp_path, capsys):
    cells = good_challenge_cells()
    path = tmp_path / "03-x" / "challenge.ipynb"

    def fails_with(mutated, expected):
        write_nb(path, mutated)
        status, out = run_nb_checker(capsys, path)
        assert status == 1 and expected in out, out

    # setup cell altered
    altered = [c.copy() for c in cells]
    altered[1] = code(with_session(snippet("setup_challenge.py"), "S03").replace("PERSONAL_SEED", "MY_SEED"))
    fails_with(altered, "setup_challenge.py")
    # no CONFIG
    fails_with(cells[:2] + cells[3:], "CONFIG")
    # CONFIG not personalised
    fails_with(cells[:2] + [code("CONFIG = {'dataset': 'a'}")] + cells[3:], "pick(")
    # no RESULTS
    fails_with([c for c in cells if "RESULTS = {'x'" not in c.source], "RESULTS")
    # RESULTS after fingerprint is not enough
    fails_with(cells[:5] + [cells[6], cells[7], code("RESULTS = {}")], "fingerprint")
    # no ai log
    fails_with([c for c in cells if "Registro de uso de IA" not in c.source], "ai_log.md")
    # ai log altered
    fails_with(cells[:6] + [md(snippet("ai_log.md").replace("(20%)", "(30%)"))] + cells[7:], "ai_log.md")
    # ai log not adjacent to fingerprint cell
    fails_with(cells[:6] + [cells[6], md("extra"), cells[7]], "right before")
    # fingerprint missing
    fails_with(cells[:-1], "fingerprint.py")
    # fingerprint not last
    fails_with(cells + [code("print('after')")], "last code cell")


def test_challenge_session_must_match_folder(tmp_path, capsys):
    path = write_nb(tmp_path / "05-evaluating-generative-models" / "challenge.ipynb",
                    good_challenge_cells("S03"))
    status, out = run_nb_checker(capsys, path)
    assert status == 1 and 'SESSION = "S03"' in out and "S05" in out


def test_challenge_session_placeholder_value_is_accepted_anywhere(tmp_path, capsys):
    path = write_nb(tmp_path / "_template" / "challenge.ipynb", good_challenge_cells("S99"))
    status, out = run_nb_checker(capsys, path)
    assert status == 0, out


def test_invalid_notebooks_fail(tmp_path, capsys):
    (tmp_path / "lab.ipynb").write_text("{ not json")
    status, out = run_nb_checker(capsys, tmp_path / "lab.ipynb")
    assert status == 1 and "cannot read notebook" in out

    (tmp_path / "v3").mkdir()
    (tmp_path / "v3" / "lab.ipynb").write_text('{"nbformat": 3, "nbformat_minor": 0, "worksheets": []}')
    status, out = run_nb_checker(capsys, tmp_path / "v3" / "lab.ipynb")
    assert status == 1 and "nbformat must be 4" in out

    raw = json.loads(nbformat.writes(v4.new_notebook(cells=[code(snippet("setup_lab.py"))])))
    raw["cells"][0]["outputs"] = "not-a-list"
    (tmp_path / "bad").mkdir()
    (tmp_path / "bad" / "lab.ipynb").write_text(json.dumps(raw))
    status, out = run_nb_checker(capsys, tmp_path / "bad" / "lab.ipynb")
    assert status == 1 and "nbformat validation failed" in out


def test_cells_without_ids_fail_validation(tmp_path, capsys):
    nb = json.loads(nbformat.writes(v4.new_notebook(cells=good_lab_cells())))
    for c in nb["cells"]:
        c.pop("id")
    (tmp_path / "lab.ipynb").write_text(json.dumps(nb))
    status, out = run_nb_checker(capsys, tmp_path / "lab.ipynb")
    assert status == 1 and "id" in out


def test_missing_path_and_empty_directory_fail(tmp_path, capsys):
    status, out = run_nb_checker(capsys, tmp_path / "nope")
    assert status == 1 and "path not found" in out
    (tmp_path / "empty").mkdir()
    status, out = run_nb_checker(capsys, tmp_path / "empty")
    assert status == 1 and "no lab.ipynb or challenge.ipynb" in out


def test_explicit_file_with_other_name_uses_kind_flag(tmp_path, capsys):
    path = write_nb(tmp_path / "draft.ipynb", [code("print(1)")])
    status, out = run_nb_checker(capsys, path)
    assert status == 0  # generic checks only
    status, out = run_nb_checker(capsys, "--kind", "lab", path)
    assert status == 1 and "setup_lab.py" in out


def test_mixed_run_reports_each_notebook_and_fails_overall(tmp_path, capsys):
    write_nb(tmp_path / "a" / "lab.ipynb", good_lab_cells())
    write_nb(tmp_path / "b" / "lab.ipynb", [code("print(1)")])
    status, out = run_nb_checker(capsys, tmp_path)
    lines = out.strip().splitlines()
    assert status == 1 and len(lines) == 2
    assert lines[0].startswith("OK ") and lines[1].startswith("FAIL ")


# ------------------------------------------------------------------------- check_links
def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def run_links(capsys, root):
    status = check_links.main([str(root)])
    captured = capsys.readouterr()
    return status, captured.out, captured.err


def test_links_all_good(tmp_path, capsys):
    write(tmp_path / "sessions/01/slides.html",
          '<link rel="stylesheet" href="../../assets/css/course.css">\n'
          '<script src="../../assets/js/course.js"></script>\n'
          '<a href="lab.ipynb#part-1">lab</a> <a href="../">up</a> <a href="?x=1">q</a>')
    write(tmp_path / "assets/css/course.css", "")
    write(tmp_path / "assets/js/course.js", "")
    write(tmp_path / "sessions/01/lab.ipynb", "{}")
    write(tmp_path / "README.md",
          "[slides](sessions/01/slides.html) ![badge](sessions/01/lab.ipynb)\n"
          "[dir](sessions/01/) [frag](#top) [ext](https://example.com/x) [mail](mailto:a@b.co)\n"
          "[both](sessions/01/lab.ipynb?raw=1#top) [titled](sessions/01/lab.ipynb \"Lab\")\n"
          "[spaced](docs/a%20b.md)\n[ref]: sessions/01/lab.ipynb\n")
    write(tmp_path / "docs/a b.md", "x")
    status, out, err = run_links(capsys, tmp_path)
    assert status == 0, out + err
    assert out.startswith("OK")


def test_broken_links_are_reported_with_file_and_line(tmp_path, capsys):
    write(tmp_path / "sessions/01/slides.html",
          '<html>\n<a href="lab.ipynb">ok</a>\n<img src="img/missing.png">\n'
          "<a href='gone.html#x'>x</a>\n")
    write(tmp_path / "sessions/01/lab.ipynb", "{}")
    write(tmp_path / "README.md", "# Title\n\nsee [x](nope.md) and [y](sessions/01/lab.ipynb)\n\n"
                                  "![b](assets/none.png)\n[ref]: missing-ref.md\n")
    status, out, err = run_links(capsys, tmp_path)
    reported = out.strip().splitlines()
    assert status == 1
    assert "README.md:3: nope.md" in reported
    assert "README.md:5: assets/none.png" in reported
    assert "README.md:6: missing-ref.md" in reported
    assert any(l.endswith("slides.html:3: img/missing.png") for l in reported)
    assert any(l.endswith("slides.html:4: gone.html") or l.endswith("slides.html:4: gone.html#x")
               for l in reported)
    assert len(reported) == 5 and "5 broken" in err


def test_markdown_code_fences_inline_code_and_comments_are_ignored(tmp_path, capsys):
    write(tmp_path / "README.md",
          "```md\n[not a link](missing.md)\n<a href=\"missing.html\">\n```\n"
          "~~~\n[tilde](missing2.md)\n~~~\n"
          "Use `[x](inline-code.md)` for links.\n"
          "<!-- [hidden](hidden.md) -->\n"
          "[real](missing-real.md)\n")
    status, out, _ = run_links(capsys, tmp_path)
    assert status == 1 and out.strip().splitlines() == ["README.md:10: missing-real.md"]


def test_html_inline_script_and_comments_are_ignored(tmp_path, capsys):
    write(tmp_path / "index.html",
          '<!-- <a href="old.html">old</a> -->\n'
          '<script>\n  el.innerHTML = \'<a href="${slug}/x.html">\';\n</script>\n'
          '<script src="missing.js"></script>\n')
    status, out, _ = run_links(capsys, tmp_path)
    assert status == 1 and out.strip().splitlines() == ["index.html:5: missing.js"]


def test_excluded_directories_are_not_scanned(tmp_path, capsys):
    for d in (".superpowers/sdd", "instructor/sessions", "node_modules/pkg", ".git/x", ".claude/worktrees/a"):
        write(tmp_path / d / "notes.md", "[broken](nope.md)")
    write(tmp_path / "README.md", "fine")
    status, out, _ = run_links(capsys, tmp_path)
    assert status == 0 and "1 file" in out


def test_links_are_case_sensitive(tmp_path, capsys):
    write(tmp_path / "sessions/01/slides.html", "")
    write(tmp_path / "README.md", "[a](sessions/01/Slides.html) [b](Sessions/01/slides.html)"
                                  " [c](sessions/01/slides.html)")
    status, out, _ = run_links(capsys, tmp_path)
    assert status == 1
    assert sorted(out.strip().splitlines()) == ["README.md:1: Sessions/01/slides.html",
                                                "README.md:1: sessions/01/Slides.html"]


def test_root_absolute_links(tmp_path, capsys):
    write(tmp_path / "assets/x.css", "")
    write(tmp_path / "page.html", '<link href="/assets/x.css">')
    write(tmp_path / "README.md", "[ok](/assets/x.css) [bad](/assets/missing.css)")
    status, out, _ = run_links(capsys, tmp_path)
    lines = out.strip().splitlines()
    assert status == 1 and len(lines) == 2
    assert lines[0].startswith("README.md:1: /assets/missing.css")
    assert lines[1].startswith("page.html:1: /assets/x.css") and "GitHub Pages" in lines[1]


def test_other_schemes_and_protocol_relative_links_are_ignored(tmp_path, capsys):
    write(tmp_path / "page.html",
          '<a href="tel:+57123">t</a><a href="javascript:void(0)">j</a>'
          '<img src="data:image/png;base64,AAAA"><script src="//cdn.example.com/x.js"></script>'
          '<a href="https://example.com/a">e</a><a href="#">top</a><a href="">empty</a>')
    status, out, _ = run_links(capsys, tmp_path)
    assert status == 0, out


def test_nested_badge_link_in_markdown(tmp_path, capsys):
    write(tmp_path / "lab.ipynb", "{}")
    write(tmp_path / "README.md",
          "[![Kaggle](https://img.shields.io/badge/k.svg)](lab.ipynb) "
          "[![Colab](assets/colab.svg)](lab.ipynb)\n")
    status, out, _ = run_links(capsys, tmp_path)
    assert status == 1 and out.strip().splitlines() == ["README.md:1: assets/colab.svg"]

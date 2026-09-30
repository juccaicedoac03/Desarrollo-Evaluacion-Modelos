/* ==========================================================================
   Desarrollo y Evaluación de Modelos Propios — deck runtime (global `Course`)
   Universidad del Rosario · Rosario GSB

   Requires reveal.js 5.1.0 (+ notes, math, highlight plugins) loaded before this file.

   Public API
   ----------
   Course.init({ session: "01" })     Reveal.initialize(...) + auto-mount components
   Course.onReady(fn)                 run fn once Reveal is ready and components are mounted
   Course.softmax(logits, temperature = 1)       -> number[]
   Course.sample(probs, rng = Math.random)       -> index (never -1; see sample())
   Course.topK(probs, k)                         -> renormalized probs, zeros outside top-k
   Course.seededRandom(seed)                     -> () => number   (mulberry32)
   Course.barChart(el, labels, values, opts?)    opts: { max, format, highlight, color, ... }
   Course.lineChart(el, series, opts?)           opts: { xLabel, yLabel, yMax, yMin, ... }
   Course.bindRange(input, output, fmt?, onChange?)   fires once on bind
   Course.tokenize(text)                         -> lowercase word tokens
   Course.ngrams(tokens, n)                      -> string[] ("a b", "b c", …)

   Extras (optional): Course.mount(root), Course.topP(probs, p).

   Declarative components mounted automatically: .quiz, .timer, .flip-card
   (alias .reveal-card), .agenda[data-current]. .prompt-card and .block-tag are CSS-only.
   ========================================================================== */
(function (global) {
  'use strict';

  var SVG_NS = 'http://www.w3.org/2000/svg';
  var COURSE_NAME = 'Desarrollo y Evaluación de Modelos Propios';
  var INSTITUTION = 'Universidad del Rosario · Rosario GSB';
  var BLOCK_COLORS = {
    warmup: '#B45309',
    theory: '#4338CA',
    break: '#475569',
    lab: '#0F766E',
    challenge: '#9E1B32'
  };

  var state = {
    initialized: false,
    ready: false,
    queue: [],
    session: '',
    readyPromise: null
  };
  var mounted = new WeakSet();

  // ------------------------------------------------------------------------
  // Small helpers
  // ------------------------------------------------------------------------

  function toArray(list) {
    return Array.prototype.slice.call(list || []);
  }

  function isFiniteNumber(v) {
    return typeof v === 'number' && isFinite(v);
  }

  function clamp(v, lo, hi) {
    return Math.min(hi, Math.max(lo, v));
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function gen(node) {
    node.setAttribute('data-course-gen', '');
    return node;
  }

  function removeGenerated(root) {
    toArray(root.querySelectorAll('[data-course-gen]')).forEach(function (n) {
      if (n.parentNode) n.parentNode.removeChild(n);
    });
  }

  function blockColor(block) {
    var value = '';
    try {
      value = getComputedStyle(document.documentElement).getPropertyValue('--block-' + block).trim();
    } catch (e) { /* ignore */ }
    return value || BLOCK_COLORS[block] || BLOCK_COLORS.theory;
  }

  function safeCall(fn, what) {
    try {
      return fn();
    } catch (err) {
      console.error('[Course] ' + what + ' failed:', err);
      return undefined;
    }
  }

  function trimNumber(v, decimals) {
    return String(+(+v).toFixed(decimals));
  }

  function defaultFormat(v) {
    if (!isFiniteNumber(v)) return String(v);
    if (Number.isInteger(v)) return v.toLocaleString('en-US');
    var a = Math.abs(v);
    var d = a >= 100 ? 0 : a >= 10 ? 1 : a >= 1 ? 2 : 3;
    return trimNumber(v, d);
  }

  // Rough text width estimate (Inter, average glyph ≈ 0.56em). Charts are sized
  // from their viewBox, never from measured pixels, so they render correctly
  // even when their slide is hidden at draw time.
  function textWidth(str, fontSize) {
    return String(str).length * fontSize * 0.56;
  }

  // ------------------------------------------------------------------------
  // Math / sampling helpers
  // ------------------------------------------------------------------------

  function argmaxIndex(xs) {
    var best = -1;
    for (var i = 0; i < xs.length; i++) {
      if (!(xs[i] === xs[i])) continue; // skip NaN
      if (best === -1 || xs[i] > xs[best]) best = i;
    }
    return best === -1 ? 0 : best;
  }

  function softmax(logits, temperature) {
    var xs = toArray(logits).map(Number);
    var n = xs.length;
    if (!n) return [];
    var T = temperature == null ? 1 : Number(temperature);
    if (!(T > 0)) {
      // T <= 0 (or NaN): greedy decoding → one-hot on the (first) argmax.
      var best = argmaxIndex(xs);
      return xs.map(function (_, i) { return i === best ? 1 : 0; });
    }
    var scaled = xs.map(function (x) { return x / T; });
    var m = -Infinity;
    for (var i = 0; i < n; i++) if (scaled[i] > m) m = scaled[i];
    if (m === Infinity) {
      var infs = scaled.map(function (x) { return x === Infinity ? 1 : 0; });
      var c = infs.reduce(function (a, b) { return a + b; }, 0);
      return infs.map(function (v) { return v / c; });
    }
    if (m === -Infinity) {
      return xs.map(function () { return 1 / n; });
    }
    var ex = scaled.map(function (x) { return Math.exp(x - m); }); // subtract max: no overflow
    var sum = ex.reduce(function (a, b) { return a + b; }, 0);
    return ex.map(function (e) { return e / sum; });
  }

  function sample(probs, rng) {
    var ps = toArray(probs).map(Number);
    var random = typeof rng === 'function' ? rng : Math.random;
    var total = 0;
    var last = -1;
    for (var i = 0; i < ps.length; i++) {
      if (ps[i] > 0 && isFinite(ps[i])) {
        total += ps[i];
        last = i;
      }
    }
    // No positive probability mass (all zeros, negatives, NaN or empty input): there is nothing
    // to sample from, so fall back to the argmax of the input (0 for an empty array) instead of
    // returning -1. Callers can therefore always index with the result, e.g. VOCAB[sample(p)].
    if (last === -1) return argmaxIndex(ps);
    var r = random() * total;
    for (var j = 0; j < ps.length; j++) {
      var p = ps[j] > 0 && isFinite(ps[j]) ? ps[j] : 0;
      if (r < p) return j;
      r -= p;
    }
    return last; // floating-point fallback
  }

  function rankIndices(ps) {
    var val = function (i) { return isFiniteNumber(ps[i]) ? ps[i] : -Infinity; };
    return ps.map(function (_, i) { return i; }).sort(function (a, b) {
      var d = val(b) - val(a);
      return d || a - b; // ties: lower index first (deterministic)
    });
  }

  function renormalize(ps) {
    var sum = ps.reduce(function (a, b) { return a + b; }, 0);
    return sum > 0 ? ps.map(function (v) { return v / sum; }) : ps;
  }

  function topK(probs, k) {
    var ps = toArray(probs).map(Number);
    var n = ps.length;
    if (!n) return [];
    var kk = Math.floor(Number(k));
    if (!(kk >= 1)) kk = 1;
    var keep = {};
    rankIndices(ps).slice(0, Math.min(kk, n)).forEach(function (i) { keep[i] = true; });
    return renormalize(ps.map(function (p, i) {
      return keep[i] && p > 0 && isFinite(p) ? p : 0;
    }));
  }

  function topP(probs, p) {
    var ps = toArray(probs).map(Number);
    if (!ps.length) return [];
    var target = Number(p);
    if (!(target > 0)) target = 0;
    var total = ps.reduce(function (a, b) { return a + (b > 0 && isFinite(b) ? b : 0); }, 0);
    var keep = {};
    var cum = 0;
    var order = rankIndices(ps);
    for (var i = 0; i < order.length; i++) {
      keep[order[i]] = true;
      cum += ps[order[i]] > 0 ? ps[order[i]] : 0;
      if (total > 0 && cum / total >= target - 1e-12) break;
    }
    return renormalize(ps.map(function (v, i) { return keep[i] && v > 0 && isFinite(v) ? v : 0; }));
  }

  function seededRandom(seed) {
    // mulberry32
    var a = (Number(seed) || 0) >>> 0;
    return function () {
      a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  var TOKEN_RE;
  try {
    TOKEN_RE = new RegExp("[\\p{L}\\p{N}]+(?:['’][\\p{L}\\p{N}]+)*", 'gu');
  } catch (e) {
    TOKEN_RE = /[A-Za-z0-9À-ÖØ-öø-ÿ]+(?:['’][A-Za-z0-9À-ÖØ-öø-ÿ]+)*/g;
  }

  function tokenize(text) {
    return String(text == null ? '' : text).toLowerCase().match(TOKEN_RE) || [];
  }

  function ngrams(tokens, n) {
    var ts = toArray(tokens);
    var size = Math.floor(Number(n));
    var out = [];
    if (!(size >= 1)) return out;
    for (var i = 0; i + size <= ts.length; i++) out.push(ts.slice(i, i + size).join(' '));
    return out;
  }

  // ------------------------------------------------------------------------
  // Range binding
  // ------------------------------------------------------------------------

  function bindRange(input, output, fmt, onChange) {
    if (!input) throw new Error('Course.bindRange: input element not found');
    var format = typeof fmt === 'function' ? fmt : function (v) { return String(v); };
    input.setAttribute('data-prevent-swipe', '');
    var handler = function () {
      var v = parseFloat(input.value);
      if (output) output.textContent = format(v);
      if (typeof onChange === 'function') onChange(v);
    };
    input.addEventListener('input', handler);
    handler();
  }

  // ------------------------------------------------------------------------
  // Charts (inline SVG, sized by viewBox)
  // ------------------------------------------------------------------------

  function svg(tag, attrs, parent) {
    var node = document.createElementNS(SVG_NS, tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        if (attrs[k] != null) node.setAttribute(k, attrs[k]);
      });
    }
    if (parent) parent.appendChild(node);
    return node;
  }

  function svgText(parent, x, y, str, attrs) {
    var t = svg('text', Object.assign({ x: x, y: y }, attrs || {}), parent);
    t.textContent = str;
    return t;
  }

  function chartRoot(host, type, W, H, ariaLabel) {
    if (!host || !host.appendChild) throw new Error('Course.' + type + 'Chart: target element not found');
    var root = null;
    for (var i = 0; i < host.children.length; i++) {
      var c = host.children[i];
      if (c.namespaceURI === SVG_NS && c.classList.contains('chart')) { root = c; break; }
    }
    if (!root) {
      root = svg('svg', { role: 'img' });
      host.appendChild(root);
    }
    while (root.firstChild) root.removeChild(root.firstChild);
    root.setAttribute('class', 'chart chart-' + type);
    root.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
    root.setAttribute('preserveAspectRatio', 'xMidYMid meet');
    root.setAttribute('aria-label', ariaLabel);
    root.style.aspectRatio = W + ' / ' + H;
    return root;
  }

  // Bar with a rounded data-end and a square baseline end.
  function hBarPath(xBase, xTip, y, h, r) {
    var w = Math.abs(xTip - xBase);
    if (w < 0.5) return 'M' + xBase + ' ' + y + 'h0.5v' + h + 'h-0.5Z';
    r = Math.min(r, w, h / 2);
    var s = xTip >= xBase ? 1 : -1;
    return 'M' + xBase + ' ' + y +
      'H' + (xTip - s * r) +
      'Q' + xTip + ' ' + y + ' ' + xTip + ' ' + (y + r) +
      'V' + (y + h - r) +
      'Q' + xTip + ' ' + (y + h) + ' ' + (xTip - s * r) + ' ' + (y + h) +
      'H' + xBase + 'Z';
  }

  function vBarPath(yBase, yTip, x, w, r) {
    var h = Math.abs(yTip - yBase);
    if (h < 0.5) return 'M' + x + ' ' + yBase + 'h' + w + 'v-0.5h' + (-w) + 'Z';
    r = Math.min(r, h, w / 2);
    var s = yTip <= yBase ? 1 : -1; // 1 = bar grows upwards
    return 'M' + x + ' ' + yBase +
      'V' + (yTip + s * r) +
      'Q' + x + ' ' + yTip + ' ' + (x + r) + ' ' + yTip +
      'H' + (x + w - r) +
      'Q' + (x + w) + ' ' + yTip + ' ' + (x + w) + ' ' + (yTip + s * r) +
      'V' + yBase + 'Z';
  }

  // Truncate a label with an ellipsis so its estimated width fits in maxWidth (SVG user units).
  function fitLabel(str, maxWidth, fontSize) {
    if (textWidth(str, fontSize) <= maxWidth) return str;
    var keep = Math.max(1, Math.floor(maxWidth / (fontSize * 0.56)) - 1);
    return str.slice(0, keep).replace(/\s+$/, '') + '…';
  }

  function barChart(host, labels, values, opts) {
    opts = opts || {};
    var vals = toArray(values).map(function (v) { v = Number(v); return isFinite(v) ? v : 0; });
    var labs = toArray(labels).map(function (l) { return l == null ? '' : String(l); });
    var n = vals.length;
    var fmt = typeof opts.format === 'function' ? opts.format : defaultFormat;
    var fs = opts.fontSize || 20;
    var vertical = opts.orientation === 'vertical';
    var dataMax = n ? Math.max.apply(null, vals) : 0;
    var dataMin = n ? Math.min.apply(null, vals) : 0;
    var hi = opts.max != null ? Number(opts.max) : Math.max(0, dataMax);
    var lo = opts.min != null ? Number(opts.min) : Math.min(0, dataMin);
    if (!(hi > lo)) hi = lo + 1;
    var highlight = opts.highlight == null ? -1 : Number(opts.highlight);
    var title = opts.title || 'Bar chart';
    var summary = labs.map(function (l, i) { return (l || i) + ': ' + fmt(vals[i]); }).join(', ');
    var formatted = vals.map(function (v) { return fmt(v); });

    var W, H, root, g, i;
    if (!vertical) {
      W = opts.width || 640;
      var rowH = opts.rowHeight || 40;
      var pad = 6;
      H = opts.height || Math.max(80, pad * 2 + n * rowH);
      rowH = n ? (H - pad * 2) / n : rowH;
      var barH = Math.min(26, rowH * 0.66);
      var labelW = clamp(Math.max.apply(null, [0].concat(labs.map(function (l) { return textWidth(l, fs); }))) + 14, 40, W * 0.42);
      var valueW = clamp(Math.max.apply(null, [0].concat(formatted.map(function (s) { return textWidth(s, fs - 1); }))) + 16, 48, W * 0.3);
      var x0 = labelW + 6;
      var x1 = W - valueW;
      var sx = function (v) { return x0 + (clamp(v, lo, hi) - lo) / (hi - lo) * (x1 - x0); };
      var base = sx(0);
      root = chartRoot(host, 'bar', W, H, title);
      svg('title', null, root).textContent = title + ' — ' + summary;
      g = svg('g', { class: 'bars' }, root);
      for (i = 0; i < n; i++) {
        var yc = pad + i * rowH + rowH / 2;
        var row = svg('g', { class: 'bar-row' + (i === highlight ? ' is-highlight' : '') }, g);
        svg('title', null, row).textContent = labs[i] + ': ' + formatted[i];
        svgText(row, labelW, yc, fitLabel(labs[i], labelW - 14, fs), {
          class: 'label' + (i === highlight ? ' is-highlight-label' : ''),
          'text-anchor': 'end', dy: '0.35em'
        });
        var tip = sx(vals[i]);
        var bar = svg('path', {
          class: 'bar' + (i === highlight ? ' is-highlight' : ''),
          d: hBarPath(base, tip, yc - barH / 2, barH, 4)
        }, row);
        if (opts.color && i !== highlight) bar.style.fill = opts.color;
        var neg = vals[i] < 0;
        svgText(row, neg ? base + 8 : Math.max(tip, base) + 8, yc, formatted[i], {
          class: 'value', 'text-anchor': 'start', dy: '0.35em'
        });
      }
      svg('line', { class: 'domain', x1: base, x2: base, y1: 0, y2: H }, root);
    } else {
      W = opts.width || 640;
      H = opts.height || 360;
      var top = fs + 14;
      var bottom = fs + 18;
      var left = 8;
      var right = 8;
      var band = n ? (W - left - right) / n : W;
      var barW = Math.min(56, band * 0.62);
      var y0 = top;
      var y1 = H - bottom;
      var sy = function (v) { return y1 - (clamp(v, lo, hi) - lo) / (hi - lo) * (y1 - y0); };
      var baseY = sy(0);
      var maxChars = Math.max(3, Math.floor(band / (fs * 0.56)));
      root = chartRoot(host, 'bar', W, H, title);
      svg('title', null, root).textContent = title + ' — ' + summary;
      g = svg('g', { class: 'bars' }, root);
      for (i = 0; i < n; i++) {
        var xc = left + band * i + band / 2;
        var col = svg('g', { class: 'bar-row' + (i === highlight ? ' is-highlight' : '') }, g);
        svg('title', null, col).textContent = labs[i] + ': ' + formatted[i];
        var tipY = sy(vals[i]);
        var cbar = svg('path', {
          class: 'bar' + (i === highlight ? ' is-highlight' : ''),
          d: vBarPath(baseY, tipY, xc - barW / 2, barW, 4)
        }, col);
        if (opts.color && i !== highlight) cbar.style.fill = opts.color;
        var lab = labs[i].length > maxChars ? labs[i].slice(0, maxChars - 1) + '…' : labs[i];
        svgText(col, xc, H - 6, lab, {
          class: 'label' + (i === highlight ? ' is-highlight-label' : ''), 'text-anchor': 'middle'
        });
        svgText(col, xc, vals[i] < 0 ? baseY - 8 : Math.min(tipY, baseY) - 8, formatted[i], {
          class: 'value', 'text-anchor': 'middle'
        });
      }
      svg('line', { class: 'domain', x1: 0, x2: W, y1: baseY, y2: baseY }, root);
    }
    host.__courseChart = { type: 'bar', labels: labs, values: vals, opts: opts };
  }

  function niceStep(range, count) {
    var raw = range / Math.max(1, count);
    if (!(raw > 0)) return 1;
    var mag = Math.pow(10, Math.floor(Math.log10(raw)));
    var norm = raw / mag;
    var step = norm < 1.5 ? 1 : norm < 3 ? 2 : norm < 7 ? 5 : 10;
    return step * mag;
  }

  function ticksFor(lo, hi, step) {
    var out = [];
    var start = Math.ceil(lo / step - 1e-9) * step;
    for (var v = start, k = 0; v <= hi + step * 1e-6 && k < 200; v += step, k++) {
      out.push(+v.toFixed(12));
    }
    return out;
  }

  function stepDecimals(step) {
    return Math.max(0, Math.min(6, -Math.floor(Math.log10(step) + 1e-9)));
  }

  function lineChart(host, series, opts) {
    opts = opts || {};
    var list = toArray(series).filter(function (s) { return s && s.points; });
    var W = opts.width || 800;
    var H = opts.height || 440;
    var fs = opts.fontSize || 20;
    var xs = [];
    var ys = [];
    list.forEach(function (s) {
      toArray(s.points).forEach(function (p) {
        if (p && isFiniteNumber(+p[0]) && isFiniteNumber(+p[1])) {
          xs.push(+p[0]);
          ys.push(+p[1]);
        }
      });
    });
    var xMin = opts.xMin != null ? +opts.xMin : (xs.length ? Math.min.apply(null, xs) : 0);
    var xMax = opts.xMax != null ? +opts.xMax : (xs.length ? Math.max.apply(null, xs) : 1);
    if (!(xMax > xMin)) { xMin -= 1; xMax += 1; }
    var dMin = ys.length ? Math.min.apply(null, ys) : 0;
    var dMax = ys.length ? Math.max.apply(null, ys) : 1;
    var yMin = opts.yMin != null ? +opts.yMin : Math.min(0, dMin);
    var yMax = opts.yMax != null ? +opts.yMax : dMax;
    if (!(yMax > yMin)) yMax = yMin + 1;
    var yStep = niceStep(yMax - yMin, 5);
    if (opts.yMax == null) yMax = Math.ceil(yMax / yStep - 1e-9) * yStep;
    if (opts.yMin == null) yMin = Math.floor(yMin / yStep + 1e-9) * yStep;
    var yTicks = ticksFor(yMin, yMax, yStep);
    var xStep = niceStep(xMax - xMin, 6);
    var xTicks = ticksFor(xMin, xMax, xStep);
    var yFmt = typeof opts.yFormat === 'function' ? opts.yFormat : function (v) { return trimNumber(v, stepDecimals(yStep)); };
    var xFmt = typeof opts.xFormat === 'function' ? opts.xFormat : function (v) { return trimNumber(v, stepDecimals(xStep)); };

    var showLegend = opts.legend != null ? !!opts.legend : list.length > 1;
    var tickW = Math.max.apply(null, [0].concat(yTicks.map(function (t) { return textWidth(yFmt(t), fs - 1); })));
    var mLeft = tickW + 14 + (opts.yLabel ? fs + 16 : 0);
    var mRight = 24;
    var mTop = showLegend ? fs + 30 : 14;
    var mBottom = fs + 16 + (opts.xLabel ? fs + 14 : 0);
    var px0 = mLeft;
    var px1 = W - mRight;
    var py0 = mTop;
    var py1 = H - mBottom;
    var sx = function (v) { return px0 + (v - xMin) / (xMax - xMin) * (px1 - px0); };
    var sy = function (v) { return py1 - (clamp(v, yMin, yMax) - yMin) / (yMax - yMin) * (py1 - py0); };

    var title = opts.title || 'Line chart';
    var root = chartRoot(host, 'line', W, H, title);
    svg('title', null, root).textContent = title + ' — ' + list.map(function (s) { return s.name; }).join(', ');

    var grid = svg('g', { class: 'axis y-axis' }, root);
    yTicks.forEach(function (t) {
      var y = sy(t);
      svg('line', { class: 'grid', x1: px0, x2: px1, y1: y, y2: y }, grid);
      svgText(grid, px0 - 10, y, yFmt(t), { class: 'tick', 'text-anchor': 'end', dy: '0.35em' });
    });
    var xAxis = svg('g', { class: 'axis x-axis' }, root);
    svg('line', { class: 'domain', x1: px0, x2: px1, y1: py1, y2: py1 }, xAxis);
    xTicks.forEach(function (t) {
      var x = sx(t);
      svg('line', { class: 'domain', x1: x, x2: x, y1: py1, y2: py1 + 6 }, xAxis);
      svgText(xAxis, x, py1 + fs + 8, xFmt(t), { class: 'tick', 'text-anchor': 'middle' });
    });
    if (opts.xLabel) {
      svgText(root, (px0 + px1) / 2, H - 6, opts.xLabel, { class: 'axis-title', 'text-anchor': 'middle' });
    }
    if (opts.yLabel) {
      var yl = svgText(root, 0, 0, opts.yLabel, { class: 'axis-title', 'text-anchor': 'middle' });
      yl.setAttribute('transform', 'translate(' + (fs * 0.9) + ' ' + ((py0 + py1) / 2) + ') rotate(-90)');
    }

    var plot = svg('g', { class: 'plot' }, root);
    list.forEach(function (s, si) {
      var cls = 'series s-' + (si % 6) + (s.dashed ? ' is-dashed' : '');
      var sg = svg('g', { class: cls }, plot);
      if (s.color) sg.style.setProperty('--sc', s.color);
      var d = '';
      var pen = false;
      var pts = toArray(s.points);
      pts.forEach(function (p) {
        var ok = p && isFiniteNumber(+p[0]) && isFiniteNumber(+p[1]);
        if (!ok) { pen = false; return; }
        d += (pen ? 'L' : 'M') + sx(+p[0]).toFixed(2) + ' ' + sy(+p[1]).toFixed(2);
        pen = true;
      });
      if (d) svg('path', { class: 'line', d: d }, sg);
      var showDots = s.markers != null ? !!s.markers : pts.length <= 30;
      if (showDots) {
        pts.forEach(function (p) {
          if (!(p && isFiniteNumber(+p[0]) && isFiniteNumber(+p[1]))) return;
          var c = svg('circle', { cx: sx(+p[0]).toFixed(2), cy: sy(+p[1]).toFixed(2), r: 4.5 }, sg);
          svg('title', null, c).textContent = (s.name || 'Series ' + (si + 1)) + ': (' + xFmt(+p[0]) + ', ' + yFmt(+p[1]) + ')';
        });
      }
    });

    if (showLegend) {
      var lg = svg('g', { class: 'legend' }, root);
      var lx = px0;
      var ly = fs * 0.5 + 8;
      list.forEach(function (s, si) {
        var name = s.name || 'Series ' + (si + 1);
        var item = svg('g', { class: 'series s-' + (si % 6) + (s.dashed ? ' is-dashed' : '') }, lg);
        if (s.color) item.style.setProperty('--sc', s.color);
        svg('line', { class: 'swatch', x1: lx, x2: lx + 30, y1: ly, y2: ly }, item);
        svgText(item, lx + 40, ly, name, { dy: '0.35em' });
        lx += 40 + textWidth(name, fs) + 30;
      });
    }
    host.__courseChart = { type: 'line', series: list, opts: opts };
  }

  // ------------------------------------------------------------------------
  // UI strings (component labels are English by default, Spanish inside lang="es")
  // ------------------------------------------------------------------------

  var STRINGS = {
    en: {
      start: 'Start', pause: 'Pause', resume: 'Resume', reset: 'Reset', plus: '+1 min',
      plusAria: 'Add one minute', done: "time's up!", timer: 'Timer', flip: 'flip card',
      correct: '✓ Correct!', tryAgain: 'Try again',
      notQuite: function (keys) { return '✗ Not quite: the answer is ' + keys + '.'; },
      chose: function (key) { return 'You chose ' + key + '.'; }
    },
    es: {
      start: 'Iniciar', pause: 'Pausar', resume: 'Reanudar', reset: 'Reiniciar', plus: '+1 min',
      plusAria: 'Añadir un minuto', done: '¡Tiempo!', timer: 'Temporizador', flip: 'tarjeta giratoria',
      correct: '✓ ¡Correcto!', tryAgain: 'Intentar de nuevo',
      notQuite: function (keys) { return '✗ No exactamente: la respuesta es ' + keys + '.'; },
      chose: function (key) { return 'Elegiste ' + key + '.'; }
    }
  };

  // Strings for a component: Spanish when the nearest ancestor with a `lang` attribute
  // (the element itself included) starts with "es", English otherwise.
  function strings(node) {
    var host = node && node.closest ? node.closest('[lang]') : null;
    var lang = host ? String(host.getAttribute('lang') || '') : '';
    return /^es(?:$|[-_])/i.test(lang) ? STRINGS.es : STRINGS.en;
  }

  // ------------------------------------------------------------------------
  // Declarative components
  // ------------------------------------------------------------------------

  function mountQuiz(q) {
    removeGenerated(q);
    q.classList.remove('is-answered', 'is-correct', 'is-wrong');
    q.setAttribute('data-prevent-swipe', '');
    var ui = strings(q);
    var options = toArray(q.querySelectorAll('.quiz-opt'));
    var correct = String(q.getAttribute('data-correct') || '')
      .split(/[\s,]+/).filter(Boolean).map(function (s) { return s.toLowerCase(); });

    options.forEach(function (b, i) {
      if (!b.getAttribute('data-key')) b.setAttribute('data-key', String.fromCharCode(97 + i));
      if (b.tagName === 'BUTTON') {
        if (!b.getAttribute('type')) b.setAttribute('type', 'button');
      } else {
        b.setAttribute('role', 'button');
        b.setAttribute('tabindex', '0');
      }
      b.classList.remove('is-chosen', 'is-correct', 'is-wrong', 'is-dimmed');
      b.removeAttribute('aria-disabled');
    });

    var feedback = gen(el('div', 'quiz-feedback'));
    feedback.setAttribute('aria-live', 'polite');
    var explain = q.querySelector('.quiz-explain');
    if (explain) q.insertBefore(feedback, explain); else q.appendChild(feedback);

    function keyOf(b) { return String(b.getAttribute('data-key')).toLowerCase(); }

    function reset() {
      q.classList.remove('is-answered', 'is-correct', 'is-wrong');
      options.forEach(function (b) {
        b.classList.remove('is-chosen', 'is-correct', 'is-wrong', 'is-dimmed');
        b.removeAttribute('aria-disabled');
      });
      feedback.textContent = '';
      if (options[0]) options[0].focus();
    }

    function answer(b) {
      if (q.classList.contains('is-answered')) return;
      var key = keyOf(b);
      var ok = null;
      q.classList.add('is-answered');
      b.classList.add('is-chosen');
      feedback.textContent = '';
      var verdict = el('span', 'quiz-verdict');
      if (correct.length) {
        ok = correct.indexOf(key) !== -1;
        q.classList.add(ok ? 'is-correct' : 'is-wrong');
        options.forEach(function (o) {
          var k = keyOf(o);
          if (correct.indexOf(k) !== -1) o.classList.add('is-correct');
          else if (o === b) o.classList.add('is-wrong');
          else o.classList.add('is-dimmed');
        });
        verdict.textContent = ok
          ? ui.correct
          : ui.notQuite(correct.map(function (k) { return k.toUpperCase(); }).join(', '));
      } else {
        options.forEach(function (o) { if (o !== b) o.classList.add('is-dimmed'); });
        verdict.textContent = ui.chose(key.toUpperCase());
      }
      options.forEach(function (o) { o.setAttribute('aria-disabled', 'true'); });
      var again = el('button', 'quiz-reset', ui.tryAgain);
      again.type = 'button';
      feedback.appendChild(verdict);
      feedback.appendChild(again);
      q.dispatchEvent(new CustomEvent('quiz:answer', { bubbles: true, detail: { key: key, correct: ok } }));
    }

    q.addEventListener('click', function (e) {
      var t = e.target;
      if (!(t instanceof Element)) return;
      if (t.closest('.quiz-reset')) { reset(); return; }
      var b = t.closest('.quiz-opt');
      if (b && q.contains(b)) answer(b);
    });
    q.addEventListener('keydown', function (e) {
      var b = e.target instanceof Element ? e.target.closest('.quiz-opt') : null;
      if (b && b.tagName !== 'BUTTON' && (e.key === 'Enter' || e.key === ' ')) {
        e.preventDefault();
        answer(b);
      }
    });
  }

  var audioCtx = null;

  function unlockAudio() {
    try {
      var AC = global.AudioContext || global.webkitAudioContext;
      if (!AC) return;
      if (!audioCtx) audioCtx = new AC();
      if (audioCtx.state === 'suspended' && audioCtx.resume) audioCtx.resume().catch(function () {});
    } catch (e) { /* audio is optional */ }
  }

  function beep() {
    try {
      if (!audioCtx || audioCtx.state !== 'running') return; // never unlocked by a user gesture
      var t0 = audioCtx.currentTime + 0.02;
      [0, 0.28, 0.56].forEach(function (dt, i) {
        var osc = audioCtx.createOscillator();
        var gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.value = i === 2 ? 1175 : 880;
        gain.gain.setValueAtTime(0.0001, t0 + dt);
        gain.gain.exponentialRampToValueAtTime(0.3, t0 + dt + 0.02);
        gain.gain.exponentialRampToValueAtTime(0.0001, t0 + dt + 0.22);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(t0 + dt);
        osc.stop(t0 + dt + 0.25);
      });
    } catch (e) { /* audio is optional */ }
  }

  function fmtClock(seconds) {
    var s = Math.max(0, Math.ceil(seconds - 1e-6));
    var m = Math.floor(s / 60);
    var r = s % 60;
    return (m < 10 ? '0' : '') + m + ':' + (r < 10 ? '0' : '') + r;
  }

  function mountTimer(t) {
    removeGenerated(t);
    var ui = strings(t);
    var minutes = parseFloat(t.getAttribute('data-minutes'));
    var extra = parseFloat(t.getAttribute('data-seconds'));
    var initial = Math.round((isFinite(minutes) ? minutes : (isFinite(extra) ? 0 : 5)) * 60 + (isFinite(extra) ? extra : 0));
    if (!(initial > 0)) initial = 60;
    var labelText = t.getAttribute('data-label');
    var sound = t.getAttribute('data-sound') !== 'off' && t.getAttribute('data-sound') !== 'false';

    t.setAttribute('role', 'group');
    t.setAttribute('aria-label', (labelText || ui.timer) + ' (' + fmtClock(initial) + ')');
    t.setAttribute('data-prevent-swipe', '');
    t.classList.remove('is-running', 'is-warning', 'is-done');

    if (labelText) {
      var labelEl = gen(el('div', 'timer-label', labelText));
      // CSS shows this after the label once the timer is done (content: attr(data-done-label)).
      labelEl.setAttribute('data-done-label', t.getAttribute('data-done-label') || ui.done);
      t.appendChild(labelEl);
    }
    var display = gen(el('div', 'timer-display', fmtClock(initial)));
    display.setAttribute('role', 'timer');
    display.setAttribute('aria-live', 'off');
    t.appendChild(display);
    var bar = gen(el('div', 'timer-bar'));
    var fill = el('span');
    bar.appendChild(fill);
    t.appendChild(bar);
    var controls = gen(el('div', 'timer-controls'));
    var startBtn = el('button', 'btn btn-sm timer-start', ui.start);
    var resetBtn = el('button', 'btn btn-sm btn-ghost timer-reset', ui.reset);
    var plusBtn = el('button', 'btn btn-sm btn-ghost timer-plus', ui.plus);
    [startBtn, resetBtn, plusBtn].forEach(function (b) { b.type = 'button'; controls.appendChild(b); });
    plusBtn.setAttribute('aria-label', ui.plusAria);
    t.appendChild(controls);

    var total = initial;
    var remaining = initial;
    var endAt = 0;
    var interval = null;
    var started = false;

    function render() {
      display.textContent = fmtClock(remaining);
      fill.style.transform = 'scaleX(' + clamp(remaining / total, 0, 1) + ')';
      t.classList.toggle('is-running', !!interval);
      t.classList.toggle('is-warning', started && remaining > 0 && remaining <= 60);
    }

    function stopInterval() {
      if (interval) clearInterval(interval);
      interval = null;
    }

    function finish() {
      stopInterval();
      remaining = 0;
      started = false;
      startBtn.textContent = ui.start;
      t.classList.add('is-done');
      render();
      display.setAttribute('aria-live', 'assertive');
      if (sound) beep();
      t.dispatchEvent(new CustomEvent('timer:done', { bubbles: true }));
    }

    function tick() {
      remaining = Math.max(0, (endAt - Date.now()) / 1000);
      if (remaining <= 0) finish(); else render();
    }

    function start() {
      if (interval) return;
      unlockAudio();
      if (remaining <= 0) resetTimer();
      t.classList.remove('is-done');
      display.setAttribute('aria-live', 'off');
      started = true;
      endAt = Date.now() + remaining * 1000;
      interval = setInterval(tick, 200);
      startBtn.textContent = ui.pause;
      render();
    }

    function pause() {
      if (!interval) return;
      remaining = Math.max(0, (endAt - Date.now()) / 1000);
      stopInterval();
      startBtn.textContent = ui.resume;
      render();
    }

    function resetTimer() {
      stopInterval();
      total = initial;
      remaining = initial;
      started = false;
      startBtn.textContent = ui.start;
      t.classList.remove('is-done');
      display.setAttribute('aria-live', 'off');
      render();
    }

    function addMinute() {
      if (t.classList.contains('is-done')) {
        t.classList.remove('is-done');
        remaining = 0;
      }
      remaining += 60;
      if (interval) endAt += 60000;
      total = Math.max(total, remaining);
      render();
    }

    controls.addEventListener('click', function (e) {
      e.stopPropagation();
      var b = e.target instanceof Element ? e.target.closest('button') : null;
      if (!b) return;
      if (b === startBtn) { if (interval) pause(); else start(); }
      else if (b === resetBtn) resetTimer();
      else if (b === plusBtn) addMinute();
    });

    t.__courseTimer = { start: start, pause: pause, reset: resetTimer, addMinute: addMinute };
    render();
  }

  function mountFlipCard(card) {
    card.setAttribute('tabindex', card.getAttribute('tabindex') || '0');
    card.setAttribute('role', 'button');
    card.setAttribute('data-prevent-swipe', '');
    var front = card.querySelector('.front');
    if (!card.getAttribute('aria-label') && front) {
      card.setAttribute('aria-label', front.textContent.trim().slice(0, 120) + ' (' + strings(card).flip + ')');
    }
    card.setAttribute('aria-pressed', card.classList.contains('is-flipped') ? 'true' : 'false');
    function toggle() {
      var flipped = card.classList.toggle('is-flipped');
      card.setAttribute('aria-pressed', flipped ? 'true' : 'false');
    }
    card.addEventListener('click', function (e) {
      var t = e.target instanceof Element ? e.target : null;
      if (t && t !== card && t.closest('a, button, input, select, textarea')) return;
      toggle();
    });
    card.addEventListener('keydown', function (e) {
      if (e.target !== card) return;
      if (e.key === 'Enter' || e.key === ' ' || e.key === 'Spacebar') {
        e.preventDefault();
        e.stopPropagation();
        toggle();
      }
    });
  }

  function mountAgenda(ol) {
    var current = ol.getAttribute('data-current');
    var items = toArray(ol.children).filter(function (li) { return li.tagName === 'LI'; });
    var hasCurrent = items.some(function (li) { return li.getAttribute('data-block') === current; });
    var seen = false;
    items.forEach(function (li) {
      var isCurrent = hasCurrent && li.getAttribute('data-block') === current && !seen;
      li.classList.toggle('is-current', isCurrent);
      li.classList.toggle('is-past', hasCurrent && !seen && !isCurrent);
      if (isCurrent) {
        li.setAttribute('aria-current', 'step');
        seen = true;
      } else {
        li.removeAttribute('aria-current');
      }
    });
  }

  var COMPONENTS = [
    { selector: '.quiz', mount: mountQuiz },
    { selector: '.timer', mount: mountTimer },
    { selector: '.flip-card, .reveal-card', mount: mountFlipCard },
    { selector: 'ol.agenda, ul.agenda', mount: mountAgenda }
  ];

  function mount(root) {
    var scope = root || document;
    COMPONENTS.forEach(function (c) {
      var nodes = toArray(scope.querySelectorAll(c.selector));
      if (scope !== document && scope.matches && scope.matches(c.selector)) nodes.unshift(scope);
      nodes.forEach(function (node) {
        if (mounted.has(node)) return;
        mounted.add(node);
        safeCall(function () { c.mount(node); }, 'mounting ' + c.selector);
      });
    });
  }

  // ------------------------------------------------------------------------
  // Deck setup
  // ------------------------------------------------------------------------

  function prepareSlides(opts) {
    toArray(document.querySelectorAll('.reveal .slides section.section-slide')).forEach(function (s) {
      var hasBg = s.hasAttribute('data-background-color') || s.hasAttribute('data-background') ||
        s.hasAttribute('data-background-gradient') || s.hasAttribute('data-background-image');
      if (!hasBg) s.setAttribute('data-background-color', blockColor(s.getAttribute('data-block') || 'theory'));
      if (!s.classList.contains('no-center')) s.classList.add('center'); // reveal.js vertical centring
    });
    toArray(document.querySelectorAll('.reveal .slides section.title-slide')).forEach(function (s) {
      if (!s.getAttribute('data-session') && state.session) s.setAttribute('data-session', state.session);
      if (!s.querySelector('.title-footer')) {
        var f = el('p', 'title-footer', INSTITUTION);
        var notes = s.querySelector('aside.notes');
        if (notes) s.insertBefore(f, notes); else s.appendChild(f);
      }
    });
    if (opts.footer !== false) {
      var revealEl = document.querySelector('.reveal');
      if (revealEl && !revealEl.querySelector('.course-footer')) {
        var text = typeof opts.footer === 'string' ? opts.footer
          : (state.session ? 'S' + state.session + ' · ' : '') + COURSE_NAME;
        revealEl.appendChild(el('div', 'course-footer', text));
      }
    }
  }

  function updateSlideKind(slide) {
    var revealEl = document.querySelector('.reveal');
    if (!revealEl || !slide) return;
    var cover = slide.classList.contains('title-slide') || slide.classList.contains('section-slide');
    revealEl.classList.toggle('is-cover-slide', cover);
  }

  function bindGlobalHandlers(Reveal) {
    var slidesEl = Reveal.getSlidesElement ? Reveal.getSlidesElement() : document.querySelector('.reveal .slides');
    if (slidesEl) {
      // Keep Space/Enter on interactive controls from also advancing the deck.
      slidesEl.addEventListener('keydown', function (e) {
        var t = e.target;
        if (!(t instanceof Element)) return;
        if (t.tagName === 'SELECT') { e.stopPropagation(); return; }
        var key = e.key;
        var activation = key === 'Enter' || key === ' ' || key === 'Spacebar';
        if (!activation) return;
        if (t.matches('button, summary, [role="button"], [tabindex]:not([tabindex="-1"])')) e.stopPropagation();
        else if (key === 'Enter' && t.matches('a[href]')) e.stopPropagation();
      });
    }
    Reveal.on('slidechanged', function (e) {
      var a = document.activeElement;
      if (a && a !== document.body && e.previousSlide && e.previousSlide.contains(a) && a.blur) a.blur();
      updateSlideKind(e.currentSlide);
    });
  }

  function markReady() {
    if (state.ready) return;
    state.ready = true;
    var q = state.queue.splice(0);
    q.forEach(function (fn) { safeCall(fn, 'Course.onReady callback'); });
  }

  function onReady(fn) {
    if (typeof fn !== 'function') return;
    if (state.ready) safeCall(fn, 'Course.onReady callback');
    else state.queue.push(fn);
  }

  function init(opts) {
    opts = opts || {};
    if (state.initialized) {
      console.warn('[Course] Course.init() called more than once; ignoring.');
      return state.readyPromise;
    }
    state.initialized = true;
    var titleSlide = document.querySelector('.reveal .slides section.title-slide');
    state.session = opts.session != null ? String(opts.session)
      : (titleSlide && titleSlide.getAttribute('data-session')) || '';
    if (state.session) document.documentElement.setAttribute('data-session', state.session);

    safeCall(function () { prepareSlides(opts); }, 'preparing slides');

    var Reveal = global.Reveal;
    if (!Reveal || typeof Reveal.initialize !== 'function') {
      console.error('[Course] reveal.js is not loaded; components mounted without a deck.');
      mount(document);
      markReady();
      state.readyPromise = Promise.resolve();
      return state.readyPromise;
    }

    var plugins = [];
    if (global.RevealNotes) plugins.push(global.RevealNotes);
    if (global.RevealMath && global.RevealMath.KaTeX) plugins.push(global.RevealMath.KaTeX);
    if (global.RevealHighlight) plugins.push(global.RevealHighlight);

    var config = {
      hash: true,
      slideNumber: 'c/t',
      width: 1280,
      height: 720,
      margin: 0.05,
      minScale: 0.2,
      maxScale: 2.0,
      transition: 'fade',
      transitionSpeed: 'fast',
      backgroundTransition: 'fade',
      center: false,
      controls: true,
      controlsTutorial: false,
      progress: true,
      navigationMode: 'linear',
      pdfSeparateFragments: false,
      pdfMaxPagesPerSlide: 1,
      katex: {
        version: '0.16.11',
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '\\[', right: '\\]', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\(', right: '\\)', display: false }
        ],
        ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'svg', 'option'],
        ignoredClasses: ['no-math'],
        throwOnError: false
      },
      plugins: plugins
    };
    var overrides = opts.reveal || {};
    Object.keys(overrides).forEach(function (k) { config[k] = overrides[k]; });

    Reveal.on('ready', function (e) {
      mount(document);
      safeCall(function () { bindGlobalHandlers(Reveal); }, 'binding deck handlers');
      updateSlideKind(e && e.currentSlide ? e.currentSlide : Reveal.getCurrentSlide());
      markReady();
      // Web fonts change text metrics: re-run reveal's layout/scale once they have loaded.
      if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(function () {
          safeCall(function () { Reveal.layout(); }, 'Reveal.layout after fonts');
        });
      }
    });

    state.readyPromise = Reveal.initialize(config);
    return state.readyPromise;
  }

  global.Course = {
    init: init,
    onReady: onReady,
    softmax: softmax,
    sample: sample,
    topK: topK,
    topP: topP,
    seededRandom: seededRandom,
    barChart: barChart,
    lineChart: lineChart,
    bindRange: bindRange,
    tokenize: tokenize,
    ngrams: ngrams,
    mount: mount
  };
})(typeof window !== 'undefined' ? window : this);

#let ar-font = ("Sakkal Majalla", "DejaVu Sans")
#let ink = rgb("#1F4E79")
#let law-fill = rgb("#EAF2FB")
#let law-stroke = rgb("#2E5C8A")
#let bar-fill = luma(217)
#let level-colors = ("أساسي": rgb("#1B7F3A"), "متوسط": rgb("#B26A00"), "متقدم": rgb("#B00020"))

#let head-table(lesson, kind) = {
  set text(size: 15pt)
  show strong: it => text(stroke: 0.45pt, it.body)
  let shaded = luma(230)
  table(
    columns: (2.4cm, 3.6cm, 1fr, 5cm), stroke: 0.6pt + black,
    inset: (x: 5pt, y: 5pt), align: horizon + center,
    table.cell(fill: shaded)[*#kind*],
    table.cell(fill: shaded)[*المادة: رياضيات*],
    [#text(size: 18pt, fill: ink)[*#lesson*]],
    table.cell(fill: shaded)[*التاريخ:* #h(0.2cm) #box[#text(dir: ltr)[2026 / ...... / ......]]],
    table.cell(colspan: 2, align: right)[الاسم: ...............................],
    table.cell(align: right)[الصف: ................................],
    table.cell(align: right)[الشعبة: ...............],
  )
}

#let setup(lesson, kind: "ورقة عمل", body) = {
  set page(paper: "us-letter", margin: (top: 3.7cm, bottom: 1.2cm, x: 1.3cm),
    header-ascent: 18%, header: head-table(lesson, kind))
  set text(font: ar-font, lang: "ar", dir: rtl, size: 16pt)
  show strong: it => text(stroke: 0.45pt, it.body)
  set par(leading: 0.55em, spacing: 0.7em, justify: false)
  show math.equation: set text(font: "New Computer Modern Math", size: 14pt)
  body
}

#let level-tag(level) = text(size: 17pt, fill: level-colors.at(level), stroke: 0.3pt + level-colors.at(level))[\[ #level \]]

#let title-bar(title, level) = block(width: 100%, fill: bar-fill, inset: (y: 4pt), below: 6pt,
  stroke: (bottom: 0.8pt + black),
  align(center)[#text(size: 22pt, stroke: 0.5pt)[#title] #h(0.6em) #level-tag(level)])

#let law(label, formula) = block(width: 100%, fill: law-fill, stroke: 0.5pt + law-stroke, radius: 2pt,
  inset: (x: 8pt, y: 7pt), below: 6pt,
  grid(columns: (1fr, auto), column-gutter: 8pt, align: (right + horizon, left + horizon),
    text(fill: ink, size: 16pt)[*القانون:* #label], text(fill: black)[#formula]))

#let letter-box(l) = box(width: 0.75cm, height: 0.62cm, stroke: 0.9pt + black,
  align(center + horizon, text(font: "DejaVu Sans", size: 11pt, weight: "bold", dir: ltr)[#l]))

#let choices(opts, side: none) = {
  set text(dir: ltr)
  let col = grid(columns: (auto, auto), column-gutter: 10pt, row-gutter: 4pt,
    align: (center + horizon, left + horizon),
    ..opts.enumerate().map(((i, o)) => (letter-box("ABCD".at(i)), block(inset: (y: 1pt),
      if o.func() == math.equation { set align(left); set block(spacing: 0pt, above: 0pt, below: 0pt); math.equation(block: true, o.body) } else { o }))).flatten())
  if side == none { col } else {
    grid(columns: (5.5cm, 1fr), align: (left + horizon, center + horizon), col, [#set text(dir: rtl); #side])
  }
}

#let question(ordinal, level, laws: (), stem, opts, side: none) = block(
  width: 100%, breakable: false, stroke: 1.2pt + black, inset: (x: 7pt, top: 5pt, bottom: 7pt), below: 8pt, {
    title-bar("السؤال: " + ordinal, level)
    for l in laws { law(l.at(0), l.at(1)) }
    block(below: 7pt, stem)
    choices(opts, side: side)
  })

#let part(l, body) = block(below: 6pt, grid(columns: (auto, 1fr), column-gutter: 6pt, align: horizon, letter-box(l), body))

#let solve(level, intro, formula, parts) = block(width: 100%, breakable: false, stroke: 1.2pt + black,
  inset: (x: 7pt, top: 6pt, bottom: 8pt), below: 10pt, {
  title-bar("حل السؤال التالي", level)
  par(intro)
  align(center, formula)
  for (lw, l, txt, hgt) in parts {
    if lw != none { law(..lw) }
    part(l, txt)
    rect(width: 100%, height: hgt * 0.78, stroke: 0.9pt + luma(128))
    v(2pt)
  }
})

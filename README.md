# Heaft — pitch deck and market study

**Pitch deck:** https://omarmudhaffar.github.io/heaft-pitch/next/
Arrow keys or click to move · **F** fullscreen · phone remote: add `#remote` to the URL.

**Market study (Sep 2026):** https://omarmudhaffar.github.io/heaft-pitch/market-study/
- `market-study/index.html` — the deck (laptop). **N** = presenter notes, **F** = fullscreen.
- `market-study/speech.html` — the speech, slide by slide, in easy English, with reading notes. Made for phones.
- `market-study/Heaft-Market-Study.pdf` — the same 17 slides as a PDF.

**Short version, for presenting (5 slides):** https://omarmudhaffar.github.io/heaft-pitch/market-study/short/
The same study cut to one chart per point — the problem, the market, the competitors, the money,
the verdict. Built for an audience of students: pictures first, one number per picture, sources
still printed on every slide. **N** = presenter notes, **F** = fullscreen.
- `market-study/short/index.html` — the deck, and the source of truth. There is no build step.
- `market-study/short/Heaft-Market-Study-Short.pdf` — the 5 slides as a PDF (6 pages with the cover).

**Go-to-market (for the business presentation):** https://omarmudhaffar.github.io/heaft-pitch/business/
Six slides that carry the spoken go-to-market talk: Ali our first creator, creators-ads-results,
what one subscriber costs, the three-year creator plan, the shares, and the close. The slides are
visual support — the words live in the presenter notes (**N**), which hold the speech itself.
- `business/index.html` — the deck, and the source of truth.
- `business/Heaft-Business-Model.pdf` — the same slides as a PDF. Rebuild it after any edit:
  `python3 tools/build_pdf.py business/index.html business/Heaft-Business-Model.pdf`
- `collab/index.html` — the two-slide version of the trainer deal, for showing a coach.

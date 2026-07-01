# Tao of Clinical Touch — Project Track

## STATUS: AWAITING LCCN → THEN KDP UPLOAD

One thing is blocking launch: LCCN from the Library of Congress.
Applied: March 23, 2026. Allow up to 30 calendar days (by ~April 22).

---

## When the LCCN Arrives — Checklist

- [ ] Add LCCN to copyright page in `build_interior.js` (replace [PENDING])
- [ ] Run `node build_main.js` → overwrites `tao_interior.docx`
- [ ] Copy to `tao_interior_final.docx`
- [ ] Export interior PDF from Word (Save as PDF → Best for printing)
- [ ] Add white barcode placeholder rectangle to `Tao_Clinical_Touch_Cover_v4.psd`
- [ ] Export cover PDF from Photoshop (Save a Copy → Photoshop PDF → Press Quality)
- [ ] Upload both files to KDP and complete metadata entry
- [ ] Launch previewer in KDP — review before approving
- [ ] Publish

## Book Specs (Final)

| Field | Value |
|---|---|
| Title | The Tao of Clinical Touch |
| Subtitle | The Neuroscience of Permission |
| Author | Drew Freedman |
| Imprint | Clinical Touch Press |
| ISBN (paperback) | 979-8-9954733-0-5 |
| LCCN | Pending (applied March 23, 2026) |
| Price | $24.99 USD |
| Royalty (est.) | ~$12.17/copy on Amazon |
| Publication date | April 2026 |

## What's Done

- ✅ Manuscript: complete (8 chapters, foreword by Whitney Lowe, appendices, about sections)
- ✅ Interior build system: Node.js + docx.js, `tao_interior_final.docx` is master
- ✅ Cover: `Tao_Clinical_Touch_Cover_v4.psd` — layered, 300 DPI, correct canvas for 77 pages
- ✅ ISBN: purchased (Bowker block of 10), registered at myidentifiers.com
- ✅ LCCN: applied via Library of Congress PrePub Book Link
- ✅ KDP metadata: title, subtitle, description, keywords, categories — all ready in `tao_project_log.md`
- ✅ KDP upload guide: step-by-step in `tao_kdp_readiness.md`
- ✅ Royalty and pricing worked out: $24.99, 60% royalty

## Key Files

| File | Purpose |
|---|---|
| `tao_interior_final.docx` | Master interior — open this in Word |
| `build_main.js` | Rebuilds interior from source files |
| `Tao_Clinical_Touch_Cover_v4.psd` | Master cover |
| `tao_project_log.md` | Full specs, decisions, KDP metadata |
| `tao_kdp_readiness.md` | Step-by-step KDP upload guide |
| `tao_metadata_package.md` | HTML description + keywords ready to paste |

## After KDP Launch

- Order 2–3 author proof copies before announcing
- Set up Amazon Author Central (author.amazon.com)
- Email KDP support to request additional categories (Pain Medicine, Neuroscience, Continuing Education)
- Phase 2: IngramSpark for library/bookstore distribution (same ISBN, same files)
- Phase 3: Kindle edition

## Publishing Path

- Phase 1 (current): KDP paperback launch
- Phase 2: IngramSpark distribution
- Phase 3: Kindle edition
- Phase 4: Hardcover (requires new ISBN from block)

## Notes

- Clinical Touch Press is the imprint. 9 ISBNs remain in the Bowker block for future titles.
- Future titles may include Learn2Tape CE manuals, K-Cuts Taping System, additional Tao volumes.

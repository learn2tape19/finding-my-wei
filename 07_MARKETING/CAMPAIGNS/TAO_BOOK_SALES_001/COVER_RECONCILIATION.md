# Cover-source reconciliation — Creative 03
Date: October 21, 2026
Result: PASS for visual reconciliation of the clean v4 PDF front design; KDP upload-file identity remains unverified. Final placed-cover fidelity QA remains pending.

## Live authority inspected
Amazon product B0GVTZZS99 opened live; product image enlarged in its image viewer.
Visible title: THE TAO OF / CLINICAL TOUCH.
Visible subtitle: The Neuroscience of Permission.
Visible author: Drew Freedman.
Dark cover, blue ripple in lower half.
Displayed Amazon image: https://m.media-amazon.com/images/I/5100zwgsaFL._SL1499_.jpg
DOM intrinsic dimensions: 1000×1499 (ratio 0.6671, consistent with 6×9).
No remote image downloaded.
Live Tao Shop displays an angled/shadow product image; it is a commerce derivative, not evidence of the print master.

## Local sources inspected
Root: /Users/Drewdog19/Desktop/Coding-folder/Tao/ . Read-only.
| File | Dimensions / evidence | Result |
|---|---|---|
| Tao_Clinical_Touch_Cover_v4 copy.png | 3724×2775, visually inspected full wrap | Visible production label at top; differing back copy; not usable as-is |
| Tao_Clinical_Touch_Cover_v4.jpg | 3727×2775, visually inspected full wrap | Clean-looking front panel, title/subtitle/ripple/author design consistent with Amazon; back differs from PNG despite v4 naming |
| Tao_Clinical_Touch_Cover_front.jpg | 1882×2485, visually inspected | Ratio 0.7573 differs from Amazon 0.6671; do not stretch into a 6×9 cover or accept merely from filename |
| Tao_Clinical_Touch_Cover_front.png | 700×823 from file metadata | Lower resolution and different ratio; not selected |
| Tao_Clinical_Touch_Cover_front_shadow.png | 584×760, previously visually inspected | Small product derivative; not selected as source master |
| Tao_Clinical_Touch_Cover_v4.psd | PSD header 3727×2775, 8-bit RGB, 4 channels; hashed | Dimensions align to clean JPG wrap; layer visibility and final saved front not visually certified |
| Tao_Clinical_Touch_Cover_v4.pdf | One-page 894.48×666 pt wrap; Photoshop PDF, modified March 30, 2026; rendered and visually inspected | Clean front design agrees with enlarged Amazon image in title/subtitle/author, ripple and overall hierarchy; preferred reproduction source |

SHA-256:
- v4 copy.png: 54478014c5beda14930eec56defe4ed994f29e07d40a0286f402c356e24eb00c
- v4.jpg: 8aebd2ad6f034cade626781db27a8bbcb098ec97e85a66c08d27389dd059bd1f
- v4.pdf: 80c040a86d00397f8368ba20568bfc84e95f20be1e9700ff00a15860017769b7
- v4.psd: 33066ea968ff31fad0ed146eb64d87704471fcbd8928df6d256e75d0d7701179

Builder script tao_cover_build_v4_barcode_locked.jsx was read as historical evidence, not executed. It specifies 300 dpi, 12.414×9.25-inch wrap and front trim guides x=6.289..12.289 inches, y=.125..9.125 inches. That would imply a 1800×2700 front panel. However, script copy differs from saved JPG; it is not proof that the JPG/PSD retains those exact bounds or represents the published uploaded edition.

## Reconciliation conclusion
The clean v4 PDF is selected as the source for the front-cover reproduction, with the matching clean JPG and layered PSD retained as provenance candidates. Its front was visually compared with the enlarged Amazon image: exact words, line structure, relative placement and original ripple design agree. The PDF was last modified March 30, preceding the March 31 publication date shown on Amazon. That timing supports, but does not prove, the source chain.
This is visual reconciliation, not byte equality or certification of which file was uploaded to KDP. Amazon's processed JPEG and the source wrap are different artifacts. Back-cover differences disqualify the PNG as a whole-wrap authority but do not require changing any front artwork.
No front-panel crop or campaign image was created in this pass. After copy approval, extract only the genuine front panel from the clean PDF at the verified trim bounds, compare the extracted front again against Amazon, and place it proportionally. If that comparison fails, stop production and resolve the source; never stretch, regenerate or retype the cover. Final cover fidelity stays pending until that actual export is inspected.

## Ripple resolution for this layout
Standalone ripple omitted under the October 21 Founder instruction. No substitution. Existing printed ripple on the book remains intact. This resolves the standalone-mark dependency for Creative 03 without claiming a new canonical mark.

## Remaining rendered QA
After source and copy approval: proportional cover placement, complete title/subtitle/author proof, no accidental print guides/back panel, color/contrast inspection, 1080×1350 export verified from file header and separate metadata, checksum and Founder image approval. These checks are NOT PERFORMED now.

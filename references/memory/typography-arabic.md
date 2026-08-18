# Arabic Typography & Content — Reference for `typography` (and auto-loaded whenever content is Arabic/bilingual)

Latin pairing basics live at the end of this file. Everything else here is what makes Arabic UI work read as considered and premium instead of a mirrored English template — the actual differentiator this skill exists to deliver.

## How Arabic letterforms affect reading (why the rules below aren't arbitrary)
Arabic is a connected, cursive script — most letters change shape depending on position in the word (isolated/initial/medial/final). This has direct UI consequences:
- **Letter-spacing (`letter-spacing`) is dangerous, not just a style knob.** Positive letter-spacing breaks the visual connections between letterforms, which for Arabic doesn't just look loose — it can make words harder to parse, since the joins carry reading information Latin spacing doesn't. Default to `letter-spacing: normal` for Arabic; only ever adjust it for a large, sparse, all-caps-equivalent display treatment, and verify legibility at the actual size used, not assumed from the Latin equivalent.
- **Diacritics and vertical space.** Even without visible diacritical marks (tashkeel) in most UI copy, Arabic letterforms carry more vertical ink (ascenders/descenders, ligature height in naskh-style faces) than Latin at the same point size — this is why Arabic needs more line-height, not a stylistic preference.
- **Weight reads differently.** A Bold Arabic weight at small UI sizes can smear/lose the letter joins on lower-quality screens faster than Bold Latin does — test the actual weight at the actual deployed size, especially for a face with tight letter joins.

## Arabic-first vs. mirrored-English — a real design decision, not just RTL flipping
Flipping an English-first layout's `direction` is not the same as designing Arabic-first:
- **Arabic-first**: type scale, spacing, and component proportions are chosen for how Arabic actually reads (see line-length and multi-line heading notes below), then the Latin/English variant is derived from it.
- **Mirrored-English**: an English layout's exact proportions (line-length, button width, card height) are kept and only `direction`/logical properties applied — this is the fast path and often fine for interior app UI, but it's the reason "mirrored, not designed" reads as generic/sloppy on anything brand-visible (hero, marketing pages, luxury positioning). For those surfaces, treat Arabic as the first-class design pass, not a mirror of the English one.

## Sizing, line-height, and line length
- Arabic body text generally wants **~10-15% larger font-size** and **noticeably more line-height** (1.6-1.9 vs. a Latin body's 1.4-1.5) than the Latin equivalent at the same visual weight.
- **Ideal Arabic line length** is shorter in character count than the equivalent English guidance suggests — aim for roughly 45-65 Arabic characters per line for body copy; a full-width column that reads comfortably in English at 75-90 characters often overshoots comfortable Arabic reading measure.
- **Multi-line Arabic headings**: because word-lengths and connecting shapes differ from English, an Arabic headline will wrap at different points than its English counterpart — never assume the same `clamp()`/breakpoint tuning that works for the English heading also prevents awkward wraps in Arabic; check the actual Arabic copy's wrap points, especially for a 2-3 word headline where a bad break looks worse than in a long paragraph.

## Numerals
- **Arabic-Indic (١٢٣) vs. Western Arabic (123)** is a market/brand decision — confirm which the specific market expects (Gulf audiences more often expect Arabic-Indic; Egypt/Levant commonly use Western numerals even in Arabic copy) rather than assuming, and keep it consistent site-wide once decided, including inside dates, prices, and phone numbers.
- Numerals inside Arabic RTL text do not reverse digit-order on their own (`120` stays `120`) — this is correct default bidi behavior; don't apply manual string-reversal logic to "fix" numerals, that's what actually breaks them.

## Mixing Arabic + English + numerals in one element
Common (a price, a product code, a brand name inside an Arabic sentence) — not an edge case to design around later. The bidi-isolation mechanism itself lives in `rtl-css-engineering.md`; the typography-specific rule on top of it: keep the embedded Latin fragment's own internal letter-spacing and line-height untouched — don't apply the Arabic sizing/spacing rules from this file to an embedded English word, they're tuned for Arabic letterforms specifically.

## Arabic punctuation
Arabic uses its own punctuation marks with different shapes and spacing conventions, not reused Latin glyphs: `،` (Arabic comma, not `,`), `؛` (Arabic semicolon), `؟` (Arabic question mark). Using the Latin punctuation marks in Arabic copy is a common, visible "not actually localized" tell — verify the font/content pipeline is using the correct Unicode codepoints, not Latin lookalikes.

## Foreign/technical terms inside Arabic copy
Product names, technical terms, and acronyms are commonly kept in Latin script inside Arabic UI by convention (brand names, "API", "URL") rather than transliterated — this is a legitimate content decision, not a translation gap, but it means every such instance needs the bidi-isolation treatment above, and a consistent house rule (which terms stay Latin vs. get Arabic equivalents) should be confirmed once per project rather than decided ad hoc per string.

## Dynamic/long text handling
Arabic strings are frequently ~20-30% longer than their English equivalent for the same meaning (see the button-label example below) — any component with fixed-width assumptions (a button sized to its English label, a card title truncation point tuned for English character count) will break or truncate wrong in Arabic. Design components to accommodate variable text length by default (flexible width, tested truncation with actual Arabic strings) rather than retrofitting after the English version ships.

## Google Arabic Fonts — comparison for choosing by function, not by name recognition
Evaluate any candidate on: x-height/Arabic proportions, weight range available, screen rendering quality at small sizes, density (how much horizontal space the script takes at a given size), UI suitability vs. editorial suitability, and Latin-companion compatibility if the project is bilingual.

| Face | Character | Best for | Avoid for |
|---|---|---|---|
| **Tajawal** | Clean geometric, wide weight range, very legible at small sizes | Default body/UI workhorse — the safe default for almost any direction | Luxury/editorial headline moments (too neutral to feel premium alone) |
| **Cairo** | Geometric, slightly warmer than Tajawal | General-purpose alternative body/UI face | — |
| **IBM Plex Sans Arabic** | Technical, engineered rhythm, pairs natively with IBM Plex Sans (Latin) | Swiss/technical directions, bilingual projects wanting genuine family-level pairing | Warm/luxury brand voices |
| **Noto Sans Arabic** | Maximum legibility, near-neutral, extremely broad language/script support | High-legibility UI, accessibility-first products, dashboards with dense mixed-script data | Anywhere a distinctive brand voice matters — reads as the "default system font" of Arabic web type |
| **Noto Kufi Arabic** | Geometric Kufic-influenced, no connecting curves — more angular/modern | Tech/modern brand headlines, geometric-direction UI accents | Body text (Kufic-style forms trade some natural readability for geometric consistency) |
| **Alexandria** | Contemporary, versatile geometric sans, generous weight range | Modern SaaS direction, works well as an El Messiri alternative with a cooler tone | — |
| **Readex Pro** | Rounded, friendly, designed for UI/interface use specifically | Approachable consumer products, onboarding/education contexts | Luxury/editorial-premium direction |
| **Changa** | Condensed geometric display | Tight headline space (nav, cards, badges) without feeling cramped | Body copy at length |
| **El Messiri** | Modern geometric-leaning display, contemporary rather than traditional | Default heading choice for Modern SaaS and most general brand work | Ultra-minimal/Swiss directions wanting more neutrality |
| **Almarai** | Rounded, friendly geometric | Approachable consumer brands | Luxury/Editorial-Premium (too soft/casual for that register) |
| **Rubik Arabic** | Rounded-geometric, matches Rubik's Latin companion closely | Bilingual projects already using Rubik for Latin, playful/modern consumer brands | Formal/technical/luxury registers |

**Building an Arabic type scale**: define the scale (e.g. `12/14/16/18/24/32/48/64px` or the project's existing token steps) once with Arabic's larger-size-and-line-height needs already factored in — don't take an existing Latin type scale and reuse the same numbers for Arabic, and don't pick font-size per-element by eye.

## Luxury/editorial Arabic display type — headline-only, used sparingly
- **Markazi Text** — Arabic serif-leaning display; pairs elegantly with a Latin serif for Luxury/Editorial-Premium. Headline sizes only, not body.
- **Aref Ruqaa** — calligraphic, high-register; strong as a single signature headline moment (hospitality/heritage/premium beauty). Never at body size or in dense UI.
- **Rakkas** — bold display with character; accent/logotype-adjacent use, sparingly, not a running heading face across many pages.
- **Paid foundry option**: 29LT (e.g. 29LT Zarid, 29LT Bukra) for flagship brand identity work where free-font parity with a premium Latin identity matters — flag as a paid recommendation rather than silently substituting a free face and calling it equivalent.

## Recommended pairings by design school / mood (7 Routes)

| Mood / Design School | Arabic Heading | Arabic Body | Latin Companion | Style Notes & Constraints |
|---|---|---|---|---|
| **1. Modern SaaS** | El Messiri or Alexandria | Tajawal | Plus Jakarta Sans / Inter | Clean, scalable, high legibility across dense dashboards |
| **2. Luxury / Editorial** | Markazi Text or Aref Ruqaa (≤24px rule) | Tajawal or Cairo | Cormorant Garamond / Fraunces | Premium high-register. Never Amiri >24px, never calligraphic for body |
| **3. Swiss / Technical** | IBM Plex Sans Arabic | IBM Plex Sans Arabic | IBM Plex Sans / Inter | Disciplined single-family hierarchy across weights |
| **4. Neo-Brutalism** | DG Bebo / Changa / Cairo | Tajawal | Outfit / Oswald / Space Grotesk | High contrast, bold borders, hard offset typography |
| **5. Glassmorphism** | Alexandria / Noto Kufi Arabic | Tajawal | Outfit / Inter | Refined geometric forms, soft translucency pairings |
| **6. Clean Corporate** | Cairo / Almarai | Tajawal | Inter / Roboto | Neutral, accessible, high WCAG AA readability |
| **7. Playful / Consumer** | Readex Pro / Rubik Arabic | Tajawal / Readex Pro | Rubik / Outfit | Rounded geometric forms, friendly microcopy tone |

### Mandatory Typography Constraints
- **The Amiri Rule**: Never use Amiri for headings or UI text above 24px (Amiri is a traditional Naskh book font; at large sizes in web UI it breaks modern layout proportions).
- **No Manuscript / Calligraphic Body**: Calligraphic fonts (Aref Ruqaa, Diwan, Nastaliq) are restricted to single signature headline moments (max 1 per view). Never use them for body text or dense UI items.
- **Letterform-Aware Sizing**: Arabic body text must be sized 10–15% larger with `line-height: 1.6–1.9` compared to Latin equivalents.

## Arabic content design (microcopy) — the text is part of the design, not content dropped into it
Arabic string length and rhythm change a component's visual weight, not just its content — the classic example: a button reading **"إتمام عملية الشراء"** (a fuller, formal phrasing) occupies meaningfully more visual space and reads more formal in tone than **"شراء"** (terse, direct) — these aren't interchangeable translations of "Checkout" / "Buy", they're different design decisions with different visual and tonal outcomes. Same for an empty state: **"لا توجد نتائج مطابقة لبحثك"** (longer, explains why) vs. **"لا توجد نتائج"** (short, blunt) need different treatment — the longer phrasing needs more space and reads more helpful/human; the shorter one fits a dense UI but can read curt.

Decide register (formal vs. direct) once per project and apply consistently across:
- Button labels, form instructions, required-field/error messages
- Empty states, notifications, tooltips, onboarding copy
- Dashboard/navigation terminology, search-interface copy, confirmation dialogs

Where the actual copywriting itself (not just its design/layout impact) is the task — full microcopy drafting, brand voice documentation — that's `website-copywriting-mena`'s job; this skill's concern is how the chosen copy's length and register shape the component/layout decision, not authoring the copy from scratch.

## Interaction states in RTL — production-specific, re-check per component
Don't assume a global mirror handles everything — see `rtl-css-engineering.md`'s per-component checklist (modals, dropdowns, tooltips, icons, tables, forms, animations) for what needs individual verification.

## Voice & tone
If the project has a documented Arabic brand voice, apply it directly rather than translating the English copy literally — a good Arabic UI voice is not a literal translation of the English one. If no Arabic voice is documented yet and the page is customer-facing, flag this before shipping rather than guessing a register.

## Web font loading performance — production-specific, not a concern in a throwaway prototype
Pairing a Latin face with an Arabic face means loading two font families at once — a common real-world performance hit if left unmanaged.
- Load only the weights actually used (2-3 weights per family, not the full 9-weight variable range).
- Self-host critical fonts (heading + body, both languages) when the stack supports it, rather than a render-blocking third-party request — set `font-display: swap` either way.
- If pulling from Google Fonts directly, add `<link rel="preconnect">` for `fonts.googleapis.com`/`fonts.gstatic.com` and preload the above-the-fold heading font specifically.
- Never load a display-only face (Aref Ruqaa, Rakkas, Markazi Text) at more than one weight — these are headline-only faces; a full weight range for a face used in one place is wasted payload.

## Logo & identity
Logo/wordmark stays pixel-identical and unmirrored across locales regardless of typography direction chosen elsewhere on the page.

---

## Latin pairing basics (non-Arabic projects)
- One display/heading face + one body face, rarely a third for accents/labels only.
- Pair by contrast, not similarity: a geometric sans heading with a humanist sans body reads intentional; two similar grotesks pairing reads like an oversight.
- Match x-height and weight range to the direction: Swiss/Minimalism want a disciplined, limited weight range; Modern SaaS can carry a fuller variable-font weight range for hierarchy.

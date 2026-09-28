# Semantic Accessibility Violation Examples

This document provides unambiguous examples of **semantic web accessibility violations**, one per violation type in the taxonomy.

## Operational definition

A **semantic accessibility violation** is a case in which the relevant HTML, ARIA, label, state, or other accessibility-related syntax is **present and structurally valid**, but determining whether it is correct requires understanding the **meaning, purpose, context, visual content, relationship, or resulting interaction state** of the webpage.

"Present" includes empty values: `alt=""` is present and valid, so axe-core passes it. Whether it is correct is a semantic question. A *missing* attribute is a syntactic violation.

Each example contains:

- the HTML under test;
- the supplementary context required for detection (for interactive types: the state reached after the action);
- the expected judgment; and
- a short explanation of why the case is semantic rather than syntactic.

> **Generation rule:** Use clearly incompatible meanings. Do not generate borderline cases where reasonable annotators could disagree.

---

## 1. Image Alt Text Not Descriptive

**Violation:** `image-alt-not-descriptive`  
**WCAG:** 1.1.1  
**Required context:** Image  
**Expected judgment:** Violation

### HTML

```html
<img src="img/p-0412.jpg" alt="Red table lamp">
```

### Supplementary context

The image appears in the product grid of a furniture shop. `img/p-0412.jpg` clearly shows a **wooden dining chair** and contains no lamp. The shop also sells lamps, so the alt text is plausible for the page. Only the image reveals the mismatch.

### Why this is a semantic violation

The `alt` attribute is present and syntactically valid. Detecting the violation requires understanding the image and recognizing that **"Red table lamp"** does not describe a chair.

---

## 2. Informative Image Marked Decorative

**Violation:** `informative-image-marked-decorative`  
**WCAG:** 1.1.1  
**Required context:** Image and surrounding text  
**Expected judgment:** Violation

### HTML

```html
<section>
  <h2>Quarterly sales</h2>
  <p>Sales grew in every region this year.</p>
  <img src="img/fig-03.png" alt="">
</section>
```

### Supplementary context

`img/fig-03.png` is a **bar chart** showing sales per region for Q1–Q4 with numeric values. None of these values appear in the surrounding text.

### Why this is a semantic violation

The `alt` attribute is **present** with an empty value, which is valid HTML and marks the image as decorative. axe-core reports no violation. Detecting the problem requires seeing that the image carries information that is not available elsewhere.

---

## 3. Video Captions Inaccurate

**Violation:** `video-captions-inaccurate`  
**WCAG:** 1.2.2  
**Required context:** Video/audio and captions  
**Expected judgment:** Violation

### HTML

```html
<video controls>
  <source src="media/v-01.mp4" type="video/mp4">
  <track kind="captions" src="media/v-01.en.vtt" srclang="en" label="English" default>
</video>
```

### Supplementary context

At 00:14, the speaker clearly says:

> "Turn left at the main entrance."

The caption displayed at the same moment says:

> "Turn right at the main entrance."

### Why this is a semantic violation

A caption track exists and is correctly associated with the video. The violation can only be identified by comparing the meaning of the caption with the spoken content.

---

## 4. Page Language Mismatch

**Violation:** `lang-mismatch`  
**WCAG:** 3.1.1  
**Required context:** Page text  
**Expected judgment:** Violation

### HTML

```html
<html lang="en">
  <body>
    <h1>Studienangebote</h1>
    <p>Hier finden Sie Informationen zu unseren Studiengängen und Bewerbungsfristen.</p>
  </body>
</html>
```

### Supplementary context

The page content is clearly written in **German**, while the page is declared as English.

### Why this is a semantic violation

`lang="en"` is syntactically valid. Detecting the problem requires identifying the actual language of the page content. An *invalid* code (e.g., `lang="english"`) would be the syntactic violation `html-lang-valid`.

---

## 5. Language of Parts Mismatch

**Violation:** `language-of-parts-mismatch`  
**WCAG:** 3.1.2  
**Required context:** Passage text  
**Expected judgment:** Violation

### HTML

```html
<p>
  The lecturer described the course as
  <span lang="fr">sehr interessant</span>.
</p>
```

### Supplementary context

The phrase **"sehr interessant"** is German, not French.

### Why this is a semantic violation

`lang="fr"` is a valid language declaration. Determining that it is wrong requires recognizing the language of the enclosed text.

---

## 6. Link Text Mismatch

**Violation:** `link-text-mismatch`  
**WCAG:** 2.4.4  
**Required context:** Destination / next state  
**Expected judgment:** Violation

### HTML

```html
<a href="/action/42">Download invoice</a>
```

### Supplementary context

- **S0 (current state):** account overview page that has an invoices section, so the link text is plausible.
- **Action:** activate the link.
- **S1 (next state):** the user's **Account Settings** page. No invoice is downloaded or displayed.

### Why this is a semantic violation

The link has valid text and a valid destination, and the `href` is opaque. The violation requires comparing the link's stated purpose with the state reached after activation.

---

## 7. Button Label Mismatch

**Violation:** `button-label-mismatch`  
**WCAG:** 2.4.6  
**Required context:** Resulting action / next state  
**Expected judgment:** Violation

### HTML

```html
<button type="button">Save changes</button>
```

### Supplementary context

- **S0:** profile settings form. Saving is a plausible action here.
- **Action:** activate the button.
- **S1:** a confirmation dialog asking **"Permanently delete your account?"** Confirming deletes the account.

### Why this is a semantic violation

The button is valid and has an accessible name. Detecting the violation requires observing that the actual action is **deletion**, not saving.

---

## 8. Form Label Mismatch

**Violation:** `form-label-mismatch`  
**WCAG:** 2.4.6  
**Required context:** Intended field purpose / next state  
**Expected judgment:** Violation

### HTML

```html
<label for="f1">Phone number</label>
<input id="f1" name="f1" type="text">
<button type="submit">Continue</button>
```

### Supplementary context

- **Action:** enter a value and submit.
- **S1:** "We sent a confirmation link to **[entered value]**. Check your inbox." The value is stored as the account **email address**.

### Why this is a semantic violation

The label exists and is correctly associated with the input. The markup itself does not reveal the field's purpose (`type="text"`, opaque `id`/`name`). Detecting the mismatch requires the state after submission.

---

## 9. Widget Label Purpose Mismatch

**Violation:** `widget-label-purpose-mismatch`  
**WCAG:** 2.4.6, 4.1.2  
**Required context:** Widget content / resulting state  
**Expected judgment:** Violation

### HTML

```html
<div role="tablist" aria-label="Account sections">
  <button id="t1" role="tab" aria-selected="false" aria-controls="panel-a">Profile</button>
</div>
<div id="panel-a" role="tabpanel" aria-labelledby="t1" hidden></div>
```

### Supplementary context

Selecting the **Profile** tab displays a panel containing only credit-card details, billing address, and payment history. No profile information is shown.

### Why this is a semantic violation

The ARIA relationships are structurally valid. The tab label **"Profile"** does not describe the content it reveals.

**Button or widget?** The element is a `<button>`, but its role is `tab`, so this is `widget-label-purpose-mismatch`. The role decides. A plain `<button>` or an accordion trigger would be `button-label-mismatch`.

---

## 10. Heading Not Descriptive

**Violation:** `heading-not-descriptive`  
**WCAG:** 2.4.6  
**Required context:** Associated section content  
**Expected judgment:** Violation

### HTML

```html
<section>
  <h2>Shipping Information</h2>
  <p>Select a payment method:</p>
  <ul>
    <li>Visa</li>
    <li>Mastercard</li>
    <li>PayPal</li>
  </ul>
  <p>Your payment will be processed after order confirmation.</p>
</section>
```

### Supplementary context

The section is exclusively about **payment methods and payment processing**. It contains no shipping information.

### Why this is a semantic violation

The heading is correctly marked up as an `<h2>`. Detecting the violation requires understanding the topic of the section and comparing it with the heading.

---

## 11. Landmark Purpose Mismatch

**Violation:** `landmark-purpose-mismatch`  
**WCAG:** 1.3.1, 2.4.6  
**Required context:** Landmark content and page structure  
**Expected judgment:** Violation

### HTML

```html
<header>
  <nav aria-label="Footer navigation">
    <a href="/">Home</a>
    <a href="/products">Products</a>
    <a href="/contact">Contact</a>
  </nav>
</header>
```

### Supplementary context

This navigation is the site's **primary navigation** and appears in the page header. The actual footer contains a separate set of links.

### Why this is a semantic violation

The navigation landmark is structurally valid and has a label. The label is wrong because it identifies primary header navigation as footer navigation. A wrong landmark *role* is the same violation type, e.g., `role="search"` on an order-confirmation region.

---

## 12. Page Title Not Descriptive

**Violation:** `page-title-not-descriptive`  
**WCAG:** 2.4.2  
**Required context:** Whole-page content and purpose  
**Expected judgment:** Violation

### HTML

```html
<head>
  <title>Contact Us</title>
</head>
<body>
  <main>
    <h1>Plans and Pricing</h1>
    <p>Choose the subscription plan that fits your organization.</p>
    <section><h2>Basic</h2><p>€10 per month</p></section>
    <section><h2>Professional</h2><p>€30 per month</p></section>
  </main>
</body>
```

### Supplementary context

The page is a **pricing and subscription page**. It contains no contact form or contact information.

### Why this is a semantic violation

A valid, non-empty `<title>` exists. Detecting the problem requires understanding the purpose of the page and comparing it with the title.

---

## 13. Autocomplete Purpose Mismatch

**Violation:** `autocomplete-purpose-mismatch`  
**WCAG:** 1.3.5  
**Required context:** Actual field purpose  
**Expected judgment:** Violation

### HTML

```html
<label for="a1">Email address</label>
<input id="a1" type="text" autocomplete="postal-code">
```

### Supplementary context

The field collects the user's **email address** and is used for account notifications.

### Why this is a semantic violation

`postal-code` is a syntactically valid `autocomplete` token. The problem is that it describes a different type of information than the field's actual purpose.

---

## 14. ARIA State Mismatch

**Violation:** `aria-state-mismatch`  
**WCAG:** 4.1.2  
**Required context:** Current rendered / interaction state  
**Expected judgment:** Violation

### HTML

```html
<button aria-expanded="false" aria-controls="d1">Product details</button>
<div id="d1">
  <p>Material: solid oak</p>
  <p>Height: 85 cm</p>
</div>
```

### Supplementary context

In the current rendered state, the **Product details panel is visible and expanded** beneath the button.

### Why this is a semantic violation

`aria-expanded="false"` is a valid ARIA value. Detecting the violation requires comparing the declared state with the actual UI state.

---

## 15. Table Header Association Mismatch

**Violation:** `table-header-association-mismatch`  
**WCAG:** 1.3.1  
**Required context:** Table contents and relationships  
**Expected judgment:** Violation

### HTML

```html
<table>
  <tr>
    <th id="h1">Product</th>
    <th id="h2">Price</th>
  </tr>
  <tr>
    <td headers="h2">Office chair</td>
    <td headers="h1">€120</td>
  </tr>
</table>
```

### Supplementary context

**Office chair** is the product name and **€120** is its price.

### Why this is a semantic violation

Both `headers` references point to existing `<th>` IDs, so the syntax is valid. The violation is that the associations are reversed.

---

## 16. Error Message Mismatch

**Violation:** `error-message-mismatch`  
**WCAG:** 3.3.1  
**Required context:** User input and validation state  
**Expected judgment:** Violation

### HTML

```html
<label for="e1">Email address</label>
<input id="e1" type="text" aria-invalid="true" aria-describedby="e1-msg">
<p id="e1-msg">Your password must contain at least eight characters.</p>
```

### Supplementary context

The user entered `john@`. The form rejects the value because it is **not a valid email address**. No password field is involved.

### Why this is a semantic violation

The error message exists and is programmatically associated with the input. Detecting the violation requires understanding the actual validation failure and comparing it with the message.

---

# Boundary Rules Between Semantic Violation Types

1. **Button vs. widget: the role decides, not the HTML element.**
   - If the element's role is `button` (`<button>`, `<input type="button|submit|reset|image">`, `role="button"`, accordion triggers), use `button-label-mismatch`.
   - If the element has another widget role (`tab`, `menuitem`, `treeitem`, `option`, `switch`, …), use `widget-label-purpose-mismatch`. This holds even when the element is a `<button>`: `<button role="tab">Profile</button>` is a tab.
2. **Images inside controls are judged as the control's label.**
   - `<input type="image">` is a button, so its `alt` falls under `button-label-mismatch`.
   - An `<img>` that is the only content of a link, and an `<area>`, fall under `link-text-mismatch`.
3. **Empty alt vs. missing alt.**
   - `alt` missing: syntactic (`image-alt`).
   - `alt=""` on a decorative image: correct, not a violation.
   - `alt=""` on an informative image: `informative-image-marked-decorative`.
   - Exception: `alt=""` on an image that is the only content of a link or button makes axe report `link-name` / `button-name`. That is syntactic, so do not use such cases for the semantic type.
4. **Language.**
   - `lang-mismatch` is about `<html lang>`. `language-of-parts-mismatch` is about `lang` on an element inside the page.
   - An *invalid* language code (`lang="english"`, `lang="#!"`, `lang=""`) is syntactic (`html-lang-valid` / `valid-lang`), not semantic.
5. **Form label vs. autocomplete.**
   - The visible label is wrong: `form-label-mismatch`.
   - The label is right but the `autocomplete` token is wrong: `autocomplete-purpose-mismatch`.
6. **Heading vs. page title.** A heading describes its section. The `<title>` describes the whole page.

---

# Annotation and Generation Rules

To keep generated cases unambiguous and free of shortcuts:

1. **Use clear semantic contradictions.**  
   Prefer `chair` vs. `lamp`, `save` vs. `delete`, or `payment` vs. `shipping` over closely related concepts (chair vs. armchair).

2. **Keep the wrong value plausible on the page.**  
   The wrong alt text, label, or title should fit the page's domain (a lamp on a furniture shop). The mismatch must then be visible only in the image or next state, not from page text alone.

3. **Do not leak the answer in the HTML.**
   - Use `type="text"` rather than `type="email"` when the field's purpose is supplied as context.
   - Use opaque file names, ids, classes, and hrefs: `img/p-0412.jpg`, not `chair.jpg`; `/action/42`, not `/settings`; no `id="voiceSearchButton"`.
   - Do not use page titles such as "Failed Example 2".

4. **Strip violation markers before detection.**  
   Comments such as `<!-- Accessibility Violation Starts Here -->` are for human readers only. Remove them from the HTML passed to the detector.

5. **Provide only observable supplementary information.**  
   Supply the image, next state, destination, form purpose, current UI state, or surrounding content. Do not state "this is a violation" in the context.

6. **For interactive types, the next state must be necessary.**  
   For link, button, widget, form label, and error message, the current state (S0) must not contradict the label on its own. For example, avoid text like "Click the button below to reveal tips" next to a button labelled "Submit form". The contradiction should appear only in the state reached after the action (S1).

7. **Visible text and accessible name should match.**  
   Do not create the mismatch with an `aria-label` that differs from the visible text. That can be detected by string comparison (WCAG 2.5.3, label in name) without understanding the next state. Change the visible label itself.

8. **Avoid borderline wording.**  
   Do not use labels such as "Learn more", "More", "Go", or "Details", whose adequacy depends on interpretation.

9. **Keep syntax valid.**  
   Run axe-core on every case. It should report no violations related to the element under test. Invalid `lang` codes, broken `aria-labelledby` references, duplicate `<title>` elements, `tabindex > 0`, and similar are syntactic and do not belong in the semantic set.

10. **Use one primary violation per generated case.**  
    Avoid combining multiple failures in a single example unless the benchmark explicitly evaluates multi-violation cases.

11. **Make supplementary context sufficient for agreement.**  
    A human annotator should be able to determine the violation from the supplied HTML and context without guessing hidden implementation details.

12. **Do not copy public test suites verbatim.**  
    W3C ACT rule examples and similar public sets may be in LLM training data. Write new content, or adapt it and cite the source.

13. **Use local, licensed assets.**  
    Store images and videos in the dataset instead of hotlinking. Record the license of each asset.

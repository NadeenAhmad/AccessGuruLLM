# Semantic Accessibility Violation Examples

This document provides unambiguous examples of **semantic web accessibility violations**.

## Operational definition

A **semantic accessibility violation** is a case in which the relevant HTML, ARIA, label, state, or other accessibility-related syntax is present and structurally valid, but determining whether it is correct requires understanding the **meaning, purpose, context, visual content, relationship, or resulting interaction state** of the webpage.

The examples below are intentionally constructed to avoid borderline cases. Each violation contains:

- the HTML under test;
- the supplementary context required for detection;
- the expected judgment; and
- a short explanation of why the case is semantic rather than purely syntactic.

> **Generation rule:** Use clearly incompatible meanings. Do not generate borderline cases where reasonable annotators could disagree.

---

## 1. Image Alt Text Not Descriptive

**Violation:** `image-alt-not-descriptive`  
**WCAG:** 1.1.1  
**Required context:** Image  
**Expected judgment:** Violation

### HTML

```html
<img src="assets/chair.jpg" alt="Red table lamp">
```

### Supplementary context

`assets/chair.jpg` clearly shows a **wooden dining chair** and contains no lamp.

### Why this is a semantic violation

The `alt` attribute is present and syntactically valid. Detecting the violation requires understanding the image and recognizing that **"Red table lamp"** does not describe a chair.

---

## 2. Video Captions Inaccurate

**Violation:** `video-captions-inaccurate`  
**WCAG:** 1.2.2  
**Required context:** Video/audio and captions  
**Expected judgment:** Violation

### HTML

```html
<video controls>
  <source src="assets/directions.mp4" type="video/mp4">
  <track
    kind="captions"
    src="assets/directions-en.vtt"
    srclang="en"
    label="English"
    default>
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

## 3. Page Language Mismatch

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

`lang="en"` is syntactically valid. Detecting the problem requires identifying the actual language of the page content.

---

## 4. Language of Parts Mismatch

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

## 5. Link Text Mismatch

**Violation:** `link-text-mismatch`  
**WCAG:** 2.4.4  
**Required context:** Destination or next state  
**Expected judgment:** Violation

### HTML

```html
<a id="invoice-link" href="/action/42">
  Download invoice
</a>
```

### Supplementary context

Following the link opens the user's **Account Settings** page. It does not download or display an invoice.

### Why this is a semantic violation

The link has valid text and a valid destination. The violation requires comparing the link's stated purpose with the destination reached after activation.

---

## 6. Button Label Mismatch

**Violation:** `button-label-mismatch`  
**WCAG:** 2.4.6  
**Required context:** Resulting action or next state  
**Expected judgment:** Violation

### HTML

```html
<button id="account-action">
  Save changes
</button>
```

### Supplementary context

Activating the button opens a confirmation dialog that says:

> "Permanently delete your account?"

Confirming the dialog deletes the account.

### Why this is a semantic violation

The button is valid and has an accessible label. Detecting the violation requires observing that the actual action is **deletion**, not saving.

---

## 7. Form Label Mismatch

**Violation:** `form-label-mismatch`  
**WCAG:** 2.4.6  
**Required context:** Intended field purpose  
**Expected judgment:** Violation

### HTML

```html
<label for="contact-value">Phone number</label>
<input
  id="contact-value"
  name="contact-value"
  type="text">
```

### Supplementary context

This field is used to collect the user's **email address**. The form stores the entered value as the account email and later uses it to send confirmation messages.

### Why this is a semantic violation

The label exists and is correctly associated with the input. The markup itself does not reveal the intended field purpose. Detecting the mismatch requires understanding what information the field is actually meant to collect.

---

## 8. Widget Label Purpose Mismatch

**Violation:** `widget-label-purpose-mismatch`  
**WCAG:** 2.4.6, 4.1.2  
**Required context:** Widget content or resulting state  
**Expected judgment:** Violation

### HTML

```html
<div role="tablist" aria-label="Account sections">
  <button
    id="profile-tab"
    role="tab"
    aria-selected="false"
    aria-controls="panel-a">
    Profile
  </button>
</div>

<div
  id="panel-a"
  role="tabpanel"
  aria-labelledby="profile-tab">
</div>
```

### Supplementary context

Selecting the **Profile** tab displays a panel containing only:

- credit-card details;
- billing address; and
- payment history.

No profile or personal-account information is shown.

### Why this is a semantic violation

The ARIA relationships are structurally valid. The problem is that the tab label **"Profile"** does not describe the content it reveals.

---

## 9. Heading Not Descriptive

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

## 10. Semantic Element Purpose Mismatch

**Violation:** `semantic-element-purpose-mismatch`  
**WCAG:** 1.3.1, 4.1.2  
**Required context:** Component content and function  
**Expected judgment:** Violation

### HTML

```html
<div role="search" aria-label="Product search">
  <h2>Review your order</h2>
  <p>Order #4832</p>
  <p>Total: €79.00</p>
  <button>Confirm purchase</button>
</div>
```

### Supplementary context

The region is an **order-confirmation component**. It contains no search field and performs no search function.

### Why this is a semantic violation

`role="search"` is syntactically valid. Detecting that the role is wrong requires understanding the actual function of the component.

---

## 11. Landmark Purpose Mismatch

**Violation:** `landmark-purpose-mismatch`  
**WCAG:** 1.3.6  
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

This navigation is the site's **primary navigation** and appears in the page header on every page. The actual footer contains a separate set of links.

### Why this is a semantic violation

The navigation landmark is structurally valid and has a label. The label is semantically wrong because it identifies primary header navigation as footer navigation.

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

    <section>
      <h2>Basic</h2>
      <p>€10 per month</p>
    </section>

    <section>
      <h2>Professional</h2>
      <p>€30 per month</p>
    </section>
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
<label for="email-value">Email address</label>
<input
  id="email-value"
  type="text"
  autocomplete="postal-code">
```

### Supplementary context

The field collects the user's **email address** and is used for account notifications.

### Why this is a semantic violation

`postal-code` is a syntactically valid `autocomplete` token. The problem is that it describes a different type of information from the field's actual purpose.

---

## 14. ARIA State Mismatch

**Violation:** `aria-state-mismatch`  
**WCAG:** 4.1.2  
**Required context:** Current rendered or interaction state  
**Expected judgment:** Violation

### HTML

```html
<button
  id="details-control"
  aria-expanded="false"
  aria-controls="product-details">
  Product details
</button>

<div id="product-details">
  <p>Material: solid oak</p>
  <p>Height: 85 cm</p>
</div>
```

### Supplementary context

In the current rendered state, the **Product details panel is visible and expanded** beneath the button.

### Why this is a semantic violation

`aria-expanded="false"` is a valid ARIA value. Detecting the violation requires comparing the declared accessibility state with the actual current UI state.

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
    <th id="product">Product</th>
    <th id="price">Price</th>
  </tr>
  <tr>
    <td headers="price">Office chair</td>
    <td headers="product">€120</td>
  </tr>
</table>
```

### Supplementary context

**Office chair** is the product name and **€120** is its price.

### Why this is a semantic violation

Both `headers` references point to existing IDs, so the syntax is structurally valid. The violation is that the semantic associations are reversed.

---

## 16. Error Message Mismatch

**Violation:** `error-message-mismatch`  
**WCAG:** 3.3.1  
**Required context:** User input and validation state  
**Expected judgment:** Violation

### HTML

```html
<label for="email">Email address</label>

<input
  id="email"
  type="text"
  aria-invalid="true"
  aria-describedby="email-error">

<p id="email-error">
  Your password must contain at least eight characters.
</p>
```

### Supplementary context

The user entered:

```text
john@
```

The form rejects the value because it is **not a valid email address**. No password field is involved in this error.

### Why this is a semantic violation

The error message exists and is programmatically associated with the input. Detecting the violation requires understanding the actual validation failure and comparing it with the message.

---

## 17. Color-Only Distinction

**Violation:** `color-only-distinction`  
**WCAG:** 1.4.1  
**Required context:** Rendered visual state and meaning of the colors  
**Expected judgment:** Violation

### HTML

```html
<style>
  .requires-action {
    color: red;
  }

  .complete {
    color: green;
  }
</style>

<p>Items shown in red require your action.</p>

<ul>
  <li class="requires-action">Invoice #1042</li>
  <li class="complete">Invoice #1043</li>
</ul>
```

### Supplementary context

In the rendered page:

- Invoice #1042 is red;
- Invoice #1043 is green; and
- there is **no icon, text label, pattern, shape, or other non-color indicator** attached to either invoice.

The colors communicate status: red means **requires action**, and green means **complete**.

### Why this is a semantic violation

The violation is not merely that colors differ. It is that **color alone communicates meaningful status information**. Detecting this requires understanding what the colors represent in context.

---

## 18. Illogical Focus Order

**Violation:** `illogical-focus-order`  
**WCAG:** 2.4.3  
**Required context:** Focus sequence and logical content grouping  
**Expected judgment:** Violation

### HTML

```html
<section>
  <h2>Personal information</h2>

  <label>
    Name
    <input type="text" tabindex="1">
  </label>

  <label>
    Street
    <input type="text" tabindex="3">
  </label>

  <label>
    City
    <input type="text" tabindex="5">
  </label>
</section>

<section>
  <h2>Newsletter preferences</h2>

  <label>
    <input type="checkbox" tabindex="2">
    Technology
  </label>

  <label>
    <input type="checkbox" tabindex="4">
    Science
  </label>
</section>
```

### Supplementary context

The rendered page presents two clearly separate tasks:

1. **Personal information:** Name → Street → City
2. **Newsletter preferences:** Technology → Science

The keyboard focus sequence is:

```text
Name
→ Technology
→ Street
→ Science
→ City
```

### Why this is a semantic violation

The focus order can be mechanically extracted, but deciding whether it preserves the logical task sequence requires understanding the grouping and meaning of the page content.

---

# Cases Excluded from the Semantic Category

The following cases should not be generated as semantic violations in this benchmark when they can be determined from structure or string comparison alone.

## Landmark Structural Violation

Example:

```html
<main>Primary content</main>
<main>Secondary content</main>
```

This is a **syntax/structural** violation because duplicate main landmarks can be detected automatically without understanding the meaning of the content.

## Label / Accessible-Name Mismatch

Example:

```html
<button aria-label="Delete item">Save</button>
```

This is a **syntax/comparison** violation when the criterion is specifically that the visible label text must be contained in the accessible name. It can be detected by automated comparison and does not require understanding the actual action of the control.

This is different from `button-label-mismatch`, where the button's label and accessible name may agree with each other but both are wrong relative to the action the button actually performs.

---

# Annotation and Generation Rules

To keep generated cases unambiguous:

1. **Use clear semantic contradictions.**  
   Prefer `chair` vs. `lamp`, `save` vs. `delete`, or `payment` vs. `shipping` over closely related concepts.

2. **Do not leak the answer unnecessarily in the HTML.**  
   For example, for a form-label mismatch, use `type="text"` rather than `type="email"` if the intended purpose is supplied separately as context.

3. **Provide only observable supplementary information.**  
   Supply the image, next state, destination, form purpose, current UI state, or surrounding content. Do not state "this is a violation" in the context.

4. **Avoid borderline wording.**  
   Do not use labels such as "Learn more", "Details", or other cases whose adequacy may reasonably depend on interpretation unless the context makes the mismatch indisputable.

5. **Keep syntax valid.**  
   Semantic examples should not simultaneously contain missing attributes, invalid ARIA values, broken references, duplicate IDs, or other syntax violations.

6. **Use one primary violation per generated case.**  
   Avoid combining multiple failures in a single example unless the benchmark explicitly evaluates multi-violation cases.

7. **Make supplementary context sufficient for agreement.**  
   A human annotator should be able to determine the violation from the supplied HTML and context without guessing hidden implementation details.

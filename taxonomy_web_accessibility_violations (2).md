# Taxonomy of Web Accessibility Violations

Each violation includes a **Violation Name**, **Description**, the corresponding **WCAG Success Criteria** it violates, **Impact**, and, where needed, the **Supplementary Information** required to detect and correct it.

Following AccessGuru (Fathallah et al., ASSETS '25), violations are classified into three categories:

- **Syntactic violations** arise when required accessibility-enhancing HTML elements or attributes are **missing or malformed**, e.g., an `<img>` without an `alt` attribute, or an invalid `lang` value. They are detected with rule-based tools (Axe-Playwright). Violation names follow axe-core.
- **Layout violations** occur when the **visual and spatial arrangement** of content fails accessibility guidelines, e.g., insufficient color contrast, or a viewport that disables zooming. Corrections must not distort the page for other users.
- **Semantic violations** occur when accessibility-enhancing HTML elements or attributes are **present and syntactically valid but fail to convey meaningful or correct content**, e.g., alt text that does not describe the image. Detecting them requires understanding meaning, context, visual content, or the state reached after an interaction. Rule-based tools cannot detect them.

---

## Semantic Violations

| **Category** | **Violation Name** | **Description** | **WCAG** | **Impact** | **Supplementary Information Required** |
| --- | --- | --- | --- | --- | --- |
| Semantic | `image-alt-not-descriptive` | Alternative text is present but is inaccurate, misleading, or does not correctly describe the content or purpose of the image (`<img>`, `<svg role="img">`, `role="img"`, `<object>`). | 1.1.1 | Critical | Image and surrounding context |
| Semantic | `informative-image-marked-decorative` | An informative image is marked as decorative: its `alt` attribute is **present but empty** (`alt=""`), or it has `role="presentation"` / `role="none"`. Assistive technologies skip it, although it conveys information not available in the surrounding text (e.g., a chart or a notice). | 1.1.1 | Critical | Image and surrounding context |
| Semantic | `video-captions-inaccurate` | Captions are present but do not accurately represent the spoken content or meaningful audio information in the video. | 1.2.2 | Critical | Video/audio and captions |
| Semantic | `lang-mismatch` | A valid page-level `lang` attribute is present, but its value does not match the actual language of the page content. | 3.1.1 | Serious | Page content |
| Semantic | `language-of-parts-mismatch` | A valid language declaration is present on a passage or component, but it does not match the actual language of that content. | 3.1.2 | Serious | Text of the relevant passage/component |
| Semantic | `link-text-mismatch` | Link text or its accessible name is present but does not accurately describe the destination or purpose of the link. | 2.4.4 | Serious | Surrounding context and destination/next state |
| Semantic | `button-label-mismatch` | An element with the button role has a label or accessible name, but it does not accurately describe the action or result produced by activating it. | 2.4.6 | Critical | Button context and resulting/next state |
| Semantic | `form-label-mismatch` | A form control has a label, but the label does not accurately describe the control's purpose or the information expected from the user. | 2.4.6 | Critical | Form control, surrounding context, and expected input |
| Semantic | `widget-label-purpose-mismatch` | An element with a widget role other than button (e.g., `tab`, `menuitem`, `treeitem`, `option`, `switch`) has a label that does not accurately describe its content, purpose, or resulting action. | 2.4.6, 4.1.2 | Serious | Widget context and resulting/next state |
| Semantic | `heading-not-descriptive` | A heading is present but does not accurately describe the topic or purpose of the content it introduces. | 2.4.6 | Moderate | Heading and associated section content |
| Semantic | `landmark-purpose-mismatch` | A landmark is structurally valid, but its role (e.g., `role="search"`, `<nav>`, `<aside>`) or accessible label does not describe the actual purpose of the region. | 1.3.1, 2.4.6 | Serious | Landmark content and surrounding document structure |
| Semantic | `page-title-not-descriptive` | A page title is present but does not accurately describe the topic or purpose of the page. | 2.4.2 | Serious | Entire page content and purpose |
| Semantic | `autocomplete-purpose-mismatch` | An input has a syntactically valid `autocomplete` value, but that value does not correspond to the actual purpose of the field. | 1.3.5 | Serious | Form-field label, expected input, and form context |
| Semantic | `aria-state-mismatch` | A valid ARIA state or property is present, but its value does not correspond to the actual state of the interface, e.g., `aria-expanded="false"` for content that is currently expanded. | 4.1.2 | Serious | Current visual/interactive state |
| Semantic | `table-header-association-mismatch` | Table header associations are syntactically present but associate data cells with headers that do not represent their actual row or column meaning. | 1.3.1 | Serious | Entire table and header/data relationships |
| Semantic | `error-message-mismatch` | An error message is present but identifies the wrong field, describes the wrong problem, or does not correspond to the actual invalid input. | 3.3.1 | Serious | Form values, validation state, and error message |

---

## Layout Violations

| **Category** | **Violation Name** | **Description** | **WCAG** | **Impact** | **Supplementary Information** |
| --- | --- | --- | --- | --- | --- |
| Layout | `meta-viewport` | Ensure `<meta name="viewport">` does not disable text scaling and zooming | 1.4.4 | Critical | |
| Layout | `meta-viewport-large` | Ensure `<meta name="viewport">` can scale a significant amount | 1.4.4 | Minor | |
| Layout | `color-contrast` | Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds | 1.4.3 | Serious | Color information (background and foreground) |
| Layout | `avoid-inline-spacing` | Ensure that text spacing set through style attributes can be adjusted with custom stylesheets | 1.4.12 | Serious | |
| Layout | `target-size` | Ensure touch targets have sufficient size and space | 2.5.5 | Serious | |
| Layout | `color-contrast-enhanced` | Ensure the contrast between foreground and background colors meets WCAG 2 AAA enhanced contrast ratio thresholds | 1.4.6 | Serious | Color information (background and foreground) |

---

## Syntactic Violations

| **Category** | **Violation Name** | **Description** | **WCAG** | **Impact** |
| --- | --- | --- | --- | --- |
| Syntax | `blink` | Ensure `<blink>` elements are not used | 2.2.2 | Serious |
| Syntax | `scope-attr-valid` | Ensure the scope attribute is used correctly on tables | 1.3.1 | Moderate |
| Syntax | `aria-allowed-attr` | Ensure an element's role supports its ARIA attributes | 4.1.2 | Critical |
| Syntax | `aria-allowed-role` | Ensure role attribute has an appropriate value for the element | 4.1.2 | Minor |
| Syntax | `aria-valid-attr` | Ensure attributes that begin with aria- are valid ARIA attributes | 4.1.2 | Critical |
| Syntax | `aria-valid-attr-value` | Ensure all ARIA attributes have valid values | 4.1.2 | Critical |
| Syntax | `autocomplete-valid` | Ensure the autocomplete attribute is correct and suitable for the form field | 1.3.5 | Serious |
| Syntax | `role-img-alt` | Ensure `[role="img"]` elements have alternative text | 1.1.1 | Serious |
| Syntax | `td-headers-attr` | Ensure that each cell in a table that uses the headers attribute refers only to other `<th>` elements in that table | 1.3.1 | Serious |
| Syntax | `area-alt` | Ensure `<area>` elements of image maps have alternative text | 2.4.4, 4.1.2 | Critical |
| Syntax | `object-alt` | Ensure `<object>` elements have alternative text | 1.1.1 | Serious |
| Syntax | `svg-img-alt` | Ensure `<svg>` elements with an img, graphics-document or graphics-symbol role have an accessible text | 1.1.1 | Serious |
| Syntax | `input-image-alt` | Ensure `<input type="image">` elements have alternative text | 1.1.1 | Critical |
| Syntax | `image-alt` | Ensure `<img>` elements have alternative text or a role of none or presentation | 1.1.1 | Critical |
| Syntax | `html-lang-valid` | Ensure the lang attribute of the `<html>` element has a valid value | 3.1.1 | Serious |
| Syntax | `html-xml-lang-mismatch` | Ensure that HTML elements with both valid lang and xml:lang attributes agree on the base language of the page | 3.1.1 | Moderate |
| Syntax | `duplicate-id-aria` | Ensure every id attribute value used in ARIA and in labels is unique | 4.1.2 | Critical |
| Syntax | `tabindex` | Ensure tabindex attribute values are not greater than 0 | 2.1.1 | Serious |
| Syntax | `valid-lang` | Ensure lang attributes have valid values | 3.1.2 | Serious |
| Syntax | `aria-required-attr` | Ensure elements with ARIA roles have all required ARIA attributes | 4.1.2 | Critical |
| Syntax | `aria-required-parent` | Ensure elements with an ARIA role that require parent roles are contained by them | 1.3.1 | Critical |
| Syntax | `aria-required-children` | Ensure elements with an ARIA role that require child roles contain them | 1.3.1 | Critical |
| Syntax | `aria-deprecated-role` | Ensure elements do not use deprecated roles | 4.1.2 | Minor |
| Syntax | `presentation-role-conflict` | Ensure elements marked as presentational do not have global ARIA or tabindex so that all screen readers ignore them | 1.3.1, 4.1.2 | Minor |
| Syntax | `aria-prohibited-attr` | Ensure ARIA attributes are not prohibited for an element's role | 4.1.2 | Serious |
| Syntax | `list` | Ensure that lists are structured correctly | 1.3.1 | Serious |
| Syntax | `frame-focusable-content` | Ensure `<frame>` and `<iframe>` elements with focusable content do not have tabindex=-1 | 2.1.1 | Serious |
| Syntax | `meta-refresh` | Ensure `<meta http-equiv="refresh">` is not used for delayed refresh | 2.2.1 | Critical |
| Syntax | `marquee` | Ensure `<marquee>` elements are not used | 2.2.2 | Serious |
| Syntax | `skip-link` | Ensure all skip links have a focusable target | 2.4.1 | Moderate |
| Syntax | `landmark-no-duplicate-contentinfo` | Ensure the document has at most one contentinfo landmark | 1.3.1 | Moderate |
| Syntax | `landmark-contentinfo-is-top-level` | Ensure the contentinfo landmark is at top level | 1.3.1 | Moderate |
| Syntax | `landmark-one-main` | Ensure the document has a main landmark | 1.3.1 | Moderate |
| Syntax | `landmark-unique` | Ensure landmarks are unique | 1.3.1 | Moderate |
| Syntax | `landmark-banner-is-top-level` | Ensure the banner landmark is at top level | 1.3.1 | Moderate |
| Syntax | `landmark-main-is-top-level` | Ensure the main landmark is at top level | 1.3.1 | Moderate |
| Syntax | `landmark-no-duplicate-main` | Ensure the document has at most one main landmark | 1.3.1 | Moderate |
| Syntax | `landmark-no-duplicate-banner` | Ensure the document has at most one banner landmark | 1.3.1 | Moderate |
| Syntax | `document-title` | Ensure each HTML document contains a non-empty `<title>` element | 2.4.2 | Serious |
| Syntax | `label` | Ensure every form element has a label | 4.1.2 | Critical |
| Syntax | `label-title-only` | Ensure that every form element has a visible label and is not solely labeled using hidden labels, or the title or aria-describedby attributes | 3.3.2 | Serious |
| Syntax | `summary-name` | Ensure summary elements have discernible text | 4.1.2 | Serious |
| Syntax | `definition-list` | Ensure `<dl>` elements are structured correctly | 1.3.1 | Serious |
| Syntax | `dlitem` | Ensure `<dt>` and `<dd>` elements are contained by a `<dl>` | 1.3.1 | Serious |
| Syntax | `th-has-data-cells` | Ensure that `<th>` elements and elements with role=columnheader/rowheader have data cells they describe | 1.3.1 | Serious |
| Syntax | `empty-table-header` | Ensure table headers have discernible text | 1.3.1, 2.4.6 | Minor |
| Syntax | `empty-heading` | Ensure headings have discernible text | 1.3.1, 2.4.6 | Minor |
| Syntax | `listitem` | Ensure `<li>` elements are used semantically | 1.3.1 | Serious |
| Syntax | `image-redundant-alt` | Ensure image alternative is not repeated as text | 1.1.1 | Minor |
| Syntax | `link-name` | Ensure links have discernible text | 2.4.4, 2.4.9 | Serious |
| Syntax | `link-in-text-block` | Ensure links are distinguished from surrounding text in a way that does not rely on color | 1.4.1 | Serious |
| Syntax | `input-button-name` | Ensure input buttons have discernible text | 4.1.2 | Critical |
| Syntax | `aria-text` | Ensure role="text" is used on elements with no focusable descendants | 4.1.2 | Serious |
| Syntax | `aria-tooltip-name` | Ensure every ARIA tooltip node has an accessible name | 4.1.2 | Serious |
| Syntax | `aria-command-name` | Ensure every ARIA button, link and menuitem has an accessible name | 4.1.2 | Serious |
| Syntax | `aria-input-field-name` | Ensure every ARIA input field has an accessible name | 4.1.2 | Serious |
| Syntax | `aria-meter-name` | Ensure every ARIA meter node has an accessible name | 1.1.1 | Serious |
| Syntax | `aria-progressbar-name` | Ensure every ARIA progressbar node has an accessible name | 1.1.1 | Serious |
| Syntax | `aria-dialog-name` | Ensure every ARIA dialog and alertdialog node has an accessible name | 4.1.2 | Serious |
| Syntax | `aria-toggle-field-name` | Ensure every ARIA toggle field has an accessible name | 4.1.2 | Serious |
| Syntax | `aria-hidden-body` | Ensure aria-hidden="true" is not present on the document body | 1.3.1, 4.1.2 | Critical |
| Syntax | `aria-hidden-focus` | Ensure aria-hidden elements are not focusable nor contain focusable elements | 4.1.2 | Serious |
| Syntax | `nested-interactive` | Ensure interactive controls are not nested as they are not always announced by screen readers or can cause focus problems for assistive technologies | 4.1.2 | Serious |
| Syntax | `scrollable-region-focusable` | Ensure elements that have scrollable content are accessible by keyboard | 2.1.1, 2.4.3 | Serious |
| Syntax | `no-autoplay-audio` | Ensure `<video>` or `<audio>` elements do not autoplay audio for more than 3 seconds without a control mechanism to stop or mute the audio | 1.4.2 | Moderate |
| Syntax | `region` | Ensure all page content is contained by landmarks | 1.3.1 | Moderate |
| Syntax | `frame-title` | Ensure `<iframe>` and `<frame>` elements have an accessible name | 4.1.2, 2.4.2 | Serious |
| Syntax | `frame-title-unique` | Ensure `<iframe>` and `<frame>` elements contain a unique title attribute | 4.1.2, 2.4.2 | Moderate |
| Syntax | `video-caption` | Ensure `<video>` elements have captions | 1.2.2 | Critical |
| Syntax | `heading-order` | Ensure the order of headings is semantically correct | 1.3.1 | Moderate |
| Syntax | `accesskeys` | Ensure every accesskey attribute value is unique | 2.1.1, 2.4.1 | Serious |
| Syntax | `page-has-heading-one` | Ensure that the page, or at least one of its frames contains a level-one heading | 2.4.6 | Moderate |
| Syntax | `bypass` | Ensure each page has at least one mechanism for a user to bypass navigation and jump straight to the content | 2.4.1 | Serious |
| Syntax | `server-side-image-map` | Ensure that server-side image maps are not used | 1.1.1 | Minor |
| Syntax | `button-name` | Ensure buttons have discernible text | 4.1.2 | Critical |
| Syntax | `aria-roles` | Ensure all elements with a role attribute use a valid value | 4.1.2 | Critical |
| Syntax | `html-has-lang` | Ensure every HTML document has a lang attribute | 3.1.1 | Serious |
| Syntax | `select-name` | Ensure select element has an accessible name | 4.1.2 | Critical |

<!-- This is commented out.
| Syntax      | `status-updates`     | Status changes are not announced to assistive technologies.                                           | 4.1.3             | Serious  |  
| Syntax      | `hover-focus`        | Content triggered by hover or focus is inaccessible or non-dismissible.                               | 1.4.13            | Serious |  
| Syntax      | `error-correction`   | No accessible suggestions for correcting input errors.                                                | 3.3.3             | Serious  |  Error context and input requirements  |
| Syntax      | `single-key-shortcut-no-modifier`   | A character key shortcut is active without a modifier key or a way to disable/remap it, which may interfere with assistive technologies. | 2.1.4             |  Serious    | Input  |
| Syntax      | `sensory-instructions`| Instructions rely on sensory characteristics without alternatives.                                    | 1.3.3             |  Serious |   |
| Syntax      | `single-navigation-method`          | Page provides only one way to locate other pages within the site, limiting user flexibility and discoverability. | 2.4.5             |  Minor    | Navigation |
| Syntax      | `frame-tested`      |   Ensure <iframe> and <frame> elements contain the axe-core script          |     4.1.2, 2.4.2 ,       |  Critical |

| Semantic      | `sensory-instructions`| Instructions rely on sensory characteristics without alternatives.                                    | 1.3.3             |  Serious |   |
| Semantic      | `error-messages`     | Errors are not clearly described, leaving users unable to fix them.                                   | 3.3.1             | Serious  |  Error context (e.g., input validation rules) |
| Semantic      | `error-correction`   | No accessible suggestions for correcting input errors.                                                | 3.3.3             | Serious  |  Error context and input requirements  |
| Semantic      | `error-consistency`  | Error messages lack consistency or clarity across interactions.                                       | 3.3.4             | Serious  |  All error messages on the page |
| Semantic      | `status-updates`     | Status changes are not announced to assistive technologies.                                           | 4.1.3             | Serious  |   |
| Semantic      | `hover-focus`        | Content triggered by hover or focus is inaccessible or non-dismissible.                               | 1.4.13            | Serious |   |
 -->

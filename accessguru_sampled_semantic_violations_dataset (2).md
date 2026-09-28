# Semantic Accessibility Violations Dataset

This table presents 35 semantic accessibility violations along with associated HTML and image context where applicable.

<table border="1" >
  <tr style="text-align: right;">
      <th ># <br/> ____</th>
      <th >Violation Type <br/>________________ <br/></th>
      <th >Impact <br/>______</th>
      <th >Description <br/>__________ </th>
      <th style="width: 250px; word-break: break-word; white-space: pre-wrap;">Affected HTML <br/>_______________</th>
      <th style="width: 400px;">Preview of the Web Page with Accessibility Violation<br/>_______________________________________________________________</th>
  </tr>  
<tr>
      <td>1</td>
      <td>`image-alt-not-descriptive`</td>
      <td>Critical</td>
      <td>Alternative text is present but is inaccurate, misleading, or does not correctly describe the content or purpose of the image.</td>
      <td>
          <pre>&lt;html lang=&quot;en&quot;&gt; &#10; &lt;img alt=&quot;ERCIM logo&quot; src=&quot;image.png&quot;/&gt; &#10; &lt;/html&gt;</pre>
      </td>
      <td>
          <html lang="en"><img alt="ERCIM logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/W3C%C2%AE_Icon.svg/1200px-W3C%C2%AE_Icon.svg.png" width="40%"></html>
      </td>
  </tr>
<tr>
    <td>2</td>
    <td>`image-alt-not-descriptive`</td>
    <td>Critical</td>
    <td>Alternative text is present but is inaccurate, misleading, or does not correctly describe the content or purpose of the image.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;svg aria-label=&quot;W3C&quot; role=&quot;img&quot; viewbox=&quot;0 0 512 512&quot;&gt;&#10;&lt;path d=&quot;M108.46&quot;&gt;&lt;/path&gt;&#10;&lt;path d=&quot;M107.6 &quot; fill=&quot;#e44d26&quot;&gt;&lt;/path&gt;&#10;&lt;path d=&quot;M256 &quot; fill=&quot;#f16529&quot;&gt;&lt;/path&gt;&#10;&lt;path d=&quot;M142 176&quot; fill=&quot;#ebebeb&quot;&gt;&lt;/path&gt;&#10;&lt;path d=&quot;M369.613.6v47.2l93-25.8&quot; fill=&quot;#fff&quot;&gt;&lt;/path&gt;&#10;&lt;/svg&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://i.ibb.co/mFYM2Ft/image.png"width="40%" ></td>
</tr>
<tr>
    <td>3</td>
    <td>`image-alt-not-descriptive`</td>
    <td>Critical</td>
    <td>Alternative text is present but is inaccurate, misleading, or does not correctly describe the content or purpose of the image.</td>
    <td>
        <pre> &lt;!DOCTYPE html&gt; &#10;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;&#10; &lt;head&gt;&#10;&#10; &lt;meta charset=&quot;UTF-8&quot;&gt; &#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt; &#10;&lt;title&gt; Canvas Image Example&lt;/title&gt; &#10;&#10;&lt;/head&gt; &#10;&#10;&lt;body&gt; &#10;&#10;&lt;canvas aria-label=&quot;HTML 5 logo&quot; height=&quot;48&quot; id=&quot;logo&quot; role=&quot;img&quot; width=&quot;72&quot;&gt;&#10;&#10;&lt;/canvas&gt; &#10;&#10;&lt;script&gt; &#10;&#10;const img = new Image(); img.src = &#x27;/logo.png&#x27;; img.onload = function() { const ctx = document.querySelector(&#x27;#logo&#x27;).getContext(&#x27;2d&#x27;); ctx.drawImage(img, 0, 0, 72, 48); } &lt;/script&gt; &#10;&#10;&lt;/body&gt; &#10;&#10;&lt;/html&gt;</pre>
    </td>
    <td>
        <!DOCTYPE html>                
        <html lang="en"><img alt="ERCIM logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/W3C%C2%AE_Icon.svg/1200px-W3C%C2%AE_Icon.svg.png" width="40%"/></html>
    </td>
</tr>
<tr>
    <td>4</td>
    <td>`lang-mismatch`</td>
    <td>Serious</td>
    <td>A valid page-level lang attribute is present, but its value does not match the actual language of the page content.</td>
    <td>
        <pre> &lt;!-- Accessibility Violation Starts Here --&gt; &#10;&lt;html lang=&quot;da&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;ACT Rules Format 1.0 - Abstract&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;p&gt;&#10;The Accessibility Conformance Testing (ACT) Rules Format 1.0 defines a format for writing accessibility test&#10;rules. These test rules can be used for developing automated testing tools and manual testing methodologies. It&#10;provides a common format that allows any party involved in accessibility testing to document and share their&#10;testing procedures in a robust and understandable manner. This enables transparency and harmonization of testing&#10;methods, including methods implemented by accessibility test tools.&#10;&lt;/p&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/4.png" ></td>
</tr>
<tr>
    <td>5</td>
    <td>`lang-mismatch`</td>
    <td>Serious</td>
    <td>A valid page-level lang attribute is present, but its value does not match the actual language of the page content.</td>
    <td>
        <pre>&lt;!-- Accessibility Violation Starts Here --&gt;                &#10;&lt;html lang=&quot;nl&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Happy&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&#10;&lt;p&gt;The Dutch word &quot;gelukkig&quot; has no equivalent in English.&lt;/p&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/6.png" ></td>
</tr>
<tr>
    <td>6</td>
    <td>`lang-mismatch`</td>
    <td>Serious</td>
    <td>A valid page-level lang attribute is present, but its value does not match the actual language of the page content.</td>
    <td>
        <pre>&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;html lang=&quot;es&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt; Stranddorp &lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;article&gt;&#10;Zij liepen een vreemde Tiki bar binnen, aan de rand van een dorpje aan het strand.&#10;&lt;/article&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/9.png" ></td>
</tr>
<tr>
    <td>7</td>
    <td>`language-of-parts-mismatch`</td>
    <td>Serious</td>
    <td>A valid language declaration is present on a passage or component, but it does not match the actual language of that content.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Dutch idioms&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;p&gt;&#10;The Dutch phrase &#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;span lang=&quot;fr&quot;&gt;&quot;&#10;Hij ging met de kippen &#10;op stok&quot;&lt;/span&gt;&#10;&#10;literally translates into &quot;He went to&#10;roost with the chickens&quot;, &#10;but it means that he went to bed early.&#10;&lt;/p&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/18.png" ></td>
</tr>
<tr>
    <td>8</td>
    <td>`language-of-parts-mismatch`</td>
    <td>Serious</td>
    <td>A valid language declaration is present on a passage or component, but it does not match the actual language of that content.</td>
    <td>
        <pre>&lt;html lang=&quot;fr&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Feu d&#x27;artifice du nouvel an&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&#10; &lt;div lang=&quot;fr&quot;&gt;&#10;&lt;img alt=&quot;Feu d&#x27;artifice au-dessus de Paris&quot; src=&quot;https://www.bvjhostelparis.com/wp-content/uploads/2017/07/PARIS-FIRE-WORKS.jpg &quot; /&gt; &#10; &lt;/div&gt;&#10;&#10;&#10; &lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;p lang=&quot;nl&quot;&gt; &#10;Bonne année !&#10;&lt;/p&gt;&#10;&#10;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/20.png" width="50%"></td>
</tr>
<tr>
    <td>9</td>
    <td>`link-text-mismatch`</td>
    <td>Serious</td>
    <td>Link text or its accessible name is present but does not accurately describe the destination or purpose of the link.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt; &#10;&lt;a href=&quot;#desc&quot;&gt;Contact us&lt;/a&gt;&#10;&#10;&lt;p id=&quot;desc&quot;&gt;This product consists of several web pages.&lt;/p&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/22.png" width="80%" ></td>
</tr>
<tr>
    <td>10</td>
    <td>`link-text-mismatch`</td>
    <td>Serious</td>
    <td>Link text or its accessible name is present but does not accurately describe the destination or purpose of the link.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt; &#10;&lt;div onclick=&quot;document.location+=&#x27;#main&#x27;&quot; &#10;role=&quot;link&quot; tabindex=&quot;0&quot;&gt;Skip to footer&lt;/div&gt;&#10;&#10;&lt;main&gt;&#10;&lt;p id=&quot;main&quot;&gt;This is the main content.&lt;/p&gt;&#10;&lt;/main&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/23.png" width="60%"></td>
</tr>
<tr>
    <td>11</td>
    <td>`link-text-mismatch`</td>
    <td>Serious</td>
    <td>Link text or its accessible name is present but does not accurately describe the destination or purpose of the link.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;svg x=&quot;0&quot; xmlns=&quot;http://www.w3.org/2000/svg&quot; y=&quot;0&quot;&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;a href=&quot;#main&quot;&gt;&#10;&#10;&lt;text x=&quot;20&quot; y=&quot;20&quot;&gt;&#10;Open search&#10;&lt;/text&gt;&#10;&lt;/a&gt;&#10;&lt;/svg&gt;&#10;&lt;main&gt;&#10;&lt;p id=&quot;main&quot;&gt;This is the main content.&lt;/p&gt;&#10;&lt;/main&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/24.png" width="50%"></td>
</tr>
<tr>
    <td>12</td>
    <td>`link-text-mismatch`</td>
    <td>Serious</td>
    <td>Link text or its accessible name is present but does not accurately describe the destination or purpose of the link.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;p&gt;See the description of &#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;a href=&quot;#desc&quot;&gt;&#10;&#10;shipping costs&lt;/a&gt;.&lt;/p&gt;&#10;&lt;p id=&quot;desc&quot;&gt;This product consists of several web pages.&lt;/p&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/25.png" width="70%"></td>
</tr>
<tr>
    <td>13</td>
    <td>`link-text-mismatch`</td>
    <td>Serious</td>
    <td>Link text or its accessible name is present but does not accurately describe the destination or purpose of the link.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;ul&gt;&#10;&lt;li&gt;&#10;Ulysses&#10;&lt;ul&gt;&#10;&#10;&lt;li&gt;&lt;a href=&quot;https://www.gutenberg.org/files/4300/4300-h/4300-h.html &quot; &gt; HTML &#10; &lt;/a&gt; &lt;/li&gt; &#10;&#10;&#10; &lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;li&gt;&#10;&lt;a href=&quot;https://www.gutenberg.org/ebooks/4300.epub.images&quot; &gt; &#10; Plain text &#10; &lt;/a&gt; &#10; &lt;/li&gt; &#10; &#10; &lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;li&gt;&lt;a href=&quot;https://www.gutenberg.org/files/4300/4300-0.txt&quot;&gt; &#10;EPUB &#10; &lt;/a&gt; &lt;/li&gt; &#10;&#10;&#10; &lt;/ul&gt; &#10; &lt;/li&gt; &#10; &lt;/ul&gt; &#10; &lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/26.png" width="30%" ></td>
</tr>
<tr>
    <td>14</td>
    <td>`link-text-mismatch`</td>
    <td>Serious</td>
    <td>Link text or its accessible name is present but does not accurately describe the destination or purpose of the link.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;p&gt;&#10;The W3C held a workshop on June 9-10, 2005 at DERI &#10;Innsbruck (Austria), to gather information about potential &#10;standardization work on Semantics in Web Services.&#10;&lt;/p&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;p&gt;&lt;a href=&quot;https://www.workshop-report.html&quot; &gt; Register for the workshop &lt;/a&gt; &lt;/p&gt; &#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/30.png" ></td>
</tr>
<tr>
    <td>15</td>
    <td>`link-text-mismatch`</td>
    <td>Serious</td>
    <td>Link text or its accessible name is present but does not accurately describe the destination or purpose of the link.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;table&gt;&#10;&lt;tr&gt;&#10;&lt;th colspan=&quot;3&quot;&gt;Books&lt;/th&gt;&#10;&lt;/tr&gt;&#10;&lt;tr&gt;&#10;&lt;td&gt;Ulysses&lt;/td&gt; &#10;&#10; &lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;td&gt;&lt;a href=&quot;https://www.gutenberg.org/files/4300/4300-h/4300-h.html &quot;&gt;Buy paperback edition &lt;/a&gt; &lt;/td&gt; &#10; &lt;td&gt; 1.61MB &lt;/td&gt; &#10; &lt;/tr&gt; &#10; &lt;/table&gt; &#10; &lt;/body&gt; &#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/32.png" ></td>
</tr>
<tr>
    <td>16</td>
    <td>`form-label-mismatch`</td>
    <td>Critical</td>
    <td>A form control has a label, but the label does not accurately describe the control's purpose or the information expected from the user.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;label&gt;Date&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;input id=&quot;fname&quot; name=&quot;fname&quot; type=&quot;text&quot;/&gt;&lt;/label&gt;&#10;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/33.png" ></td>
</tr>
<tr>
    <td>17</td>
    <td>`form-label-mismatch`</td>
    <td>Critical</td>
    <td>A form control has a label, but the label does not accurately describe the control's purpose or the information expected from the user.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;label for=&quot;address&quot;&gt;Age&lt;/label&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;input id=&quot;address&quot; name=&quot;address&quot; type=&quot;text&quot;/&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/34.png" ></td>
</tr>
<tr>
    <td>18</td>
    <td>`form-label-mismatch`</td>
    <td>Critical</td>
    <td>A form control has a label, but the label does not accurately describe the control's purpose or the information expected from the user.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;fieldset&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;h2 style=&quot;position: absolute; top: -9999px; left: -9999px;&quot;&gt;Shipping address&lt;/h2&gt;&#10;&lt;label&gt;First Name:: &lt;input name=&quot;shipping-street&quot; type=&quot;text&quot;/&gt;&lt;/label&gt;&#10;&lt;label&gt;Last Name:: &lt;input name=&quot;shipping-street&quot; type=&quot;text&quot;/&gt;&lt;/label&gt;&#10;&#10;&lt;/fieldset&gt;&#10;&lt;fieldset&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;h2 style=&quot;position: absolute; top: -9999px; left: -9999px;&quot;&gt;Contact Information&lt;/h2&gt;&#10;&lt;label&gt;House Number: &lt;input name=&quot;contact-info&quot; type=&quot;text&quot;/&gt;&lt;/label&gt;&#10;&lt;label&gt;Street: &lt;input name=&quot;contact-info&quot; type=&quot;text&quot;/&gt;&lt;/label&gt;&#10;&#10;&#10;&lt;/fieldset&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/36.png" ></td>
</tr>
<tr>
    <td>19</td>
    <td>`heading-not-descriptive`</td>
    <td>Moderate</td>
    <td>A heading is present but does not accurately describe the topic or purpose of the content it introduces.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;h1&gt;Weather&lt;/h1&gt;&#10;&#10;&lt;p&gt;We are open Monday through Friday from 10 to 16&lt;/p&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/38.png" ></td>
</tr>
<tr>
    <td>20</td>
    <td>`heading-not-descriptive`</td>
    <td>Moderate</td>
    <td>A heading is present but does not accurately describe the topic or purpose of the content it introduces.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;span aria-level=&quot;1&quot; role=&quot;heading&quot;&gt;Weather&lt;/span&gt;&#10;&#10;&lt;p&gt;We are open Monday through Friday from 10 to 16&lt;/p&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/39.png" ></td>
</tr>
<tr>
    <td>21</td>
    <td>`heading-not-descriptive`</td>
    <td>Moderate</td>
    <td>A heading is present but does not accurately describe the topic or purpose of the content it introduces.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;span aria-level=&quot;1&quot; role=&quot;heading&quot; style=&quot;position: absolute; top: -9999px; left: -9999px;&quot;&gt;&#10;Weather&#10;&lt;/span&gt;&#10;&#10;&lt;p&gt;&#10;We are open Monday through Friday from 10 to 16&#10;&lt;/p&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/40.png" ></td>
</tr>
<tr>
    <td>22</td>
    <td>`page-title-not-descriptive`</td>
    <td>Serious</td>
    <td>A page title is present but does not accurately describe the topic or purpose of the page.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;title&gt;Apple harvesting season&lt;/title&gt;&#10;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;p&gt;&#10;Clementines will be ready to harvest from late October &#10;through February.&#10;&lt;/p&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/42.png" ></td>
</tr>
<tr>
    <td>23</td>
    <td>`page-title-not-descriptive`</td>
    <td>Serious</td>
    <td>A page title is present but does not accurately describe the topic or purpose of the page.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;title&gt;Cucumber and Tomato Harvest&lt;/title&gt;&#10;&#10;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;p&gt;&#10;Clementines will be ready to harvest from late October &#10;through February.&#10;&lt;/p&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/43.png" ></td>
</tr>
<tr>
    <td>24</td>
    <td>`page-title-not-descriptive`</td>
    <td>Serious</td>
    <td>A page title is present but does not accurately describe the topic or purpose of the page.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;title&gt;Campus map – University of Arkham&lt;/title&gt;&#10;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&lt;h1&gt;Search results for &quot;accessibility&quot; at the University of Arkham&lt;/h1&gt;&#10;&lt;p&gt;None&lt;/p&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/44.png" ></td>
</tr>
<tr>
    <td>25</td>
    <td>`button-label-mismatch`</td>
    <td>Critical</td>
    <td>An element with the button role has a label or accessible name, but it does not accurately describe the action or result produced by activating it.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;input alt=&quot;Clear Form&quot; src=&quot;/WAI/content-assets/wcag-act-rules/test-assets/shared/icon.svg&quot; type=&quot;image&quot;/&gt;&#10;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/45.png" ></td>
</tr>
<tr>
    <td>26</td>
    <td>`button-label-mismatch`</td>
    <td>Critical</td>
    <td>An element with the button role has a label or accessible name, but it does not accurately describe the action or result produced by activating it.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;input aria-label=&quot;Search&quot; src=&quot;/WAI/content-assets/wcag-act-rules/test-assets/shared/icon.svg&quot; type=&quot;image&quot;/&gt;&#10;&#10;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/46.png" ></td>
</tr>
<tr>
    <td>27</td>
    <td>`button-label-mismatch`</td>
    <td>Critical</td>
    <td>An element with the button role has a label or accessible name, but it does not accurately describe the action or result produced by activating it.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;input src=&quot;/WAI/content-assets/wcag-act-rules/test-assets/shared/icon.svg&quot; title=&quot;Back&quot; type=&quot;image&quot;/&gt;&#10;&#10;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/47.png" ></td>
</tr>
<tr>
    <td>28</td>
    <td>`button-label-mismatch`</td>
    <td>Critical</td>
    <td>An element with the button role has a label or accessible name, but it does not accurately describe the action or result produced by activating it.</td>
    <td>
        <pre>&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;&lt;title&gt;Example page&lt;/title&gt;&#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;input aria-labelledby=&quot;id1&quot; src=&quot;/WAI/content-assets/wcag-act-rules/test-assets/shared/icon.svg&quot; type=&quot;image&quot;/&gt;&#10;&lt;div id=&quot;id1&quot;&gt;Upload&lt;/div&gt;&#10;&#10;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/48.png" ></td>
</tr>
<tr>
    <td>29</td>
    <td>`button-label-mismatch`</td>
    <td>Critical</td>
    <td>An element with the button role has a label or accessible name, but it does not accurately describe the action or result produced by activating it.</td>
    <td>
        <pre>&lt;button id=&quot;iconButton&quot; &#10;class=&quot;icon-button&quot; &#10;title=&quot;Upload Document&quot;&gt; &#10; &lt;img alt=&quot;&quot; src=&quot;https://example.com/icon.png&quot;&gt; &#10;&lt;/button&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/49.png" ></td>
</tr>
<tr>
    <td>30</td>
    <td>`image-alt-not-descriptive`</td>
    <td>Critical</td>
    <td>Alternative text is present but is inaccurate, misleading, or does not correctly describe the content or purpose of the image.</td>
    <td>
        <pre>&lt;!DOCTYPE html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;    &lt;meta charset=&quot;UTF-8&quot;&gt;&#10;    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;&#10;    &lt;meta name=&quot;description&quot; content=&quot;A simple webpage about climate change featuring a graph image with accessibility considerations.&quot;&gt;&#10;    &lt;title&gt;Climate Change Insights&lt;/title&gt;&#10;  &#10;&lt;/head&gt;&#10;&lt;body&gt;&#10;    &lt;header&gt;&#10;        &lt;h1&gt;Understanding Climate Change&lt;/h1&gt;&#10;        &lt;p&gt;This page highlights the impact of climate change through data visualization.&lt;/p&gt;&#10;    &lt;/header&gt;&#10;&#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;    &lt;main&gt;&#10;        &lt;img src=&quot;graphblog-1.png &quot; alt=&quot;A pie chart showing the percentage distribution of diabetes prevalence by age group. &quot; /&gt;&#10;    &lt;/main&gt;&#10;    &lt;footer&gt; &#10;  &lt;p&gt; Data sourced from Global Climate Watch  &lt;a href= &quot;#&quot; aria-label=&quot;Learn more about climate change&quot;&gt;Learn more&lt;/a&gt;&lt;/p&gt;&#10;    &lt;/footer&gt; &#10; &lt;/body&gt; &#10; &lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/50.png" ></td>
</tr>
<tr>
    <td>31</td>
    <td>`image-alt-not-descriptive`</td>
    <td>Critical</td>
    <td>Alternative text is present but is inaccurate, misleading, or does not correctly describe the content or purpose of the image.</td>
    <td>
        <pre>&lt;!DOCTYPE html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;    &lt;meta charset=&quot;UTF-8&quot;&gt;&#10;    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;&#10;    &lt;meta name=&quot;description&quot; content=&quot;A simple webpage discussing renewable energy sources with a focus on solar power.&quot;&gt;&#10;    &lt;title&gt;Renewable Energy Spotlight&lt;/title&gt;&#10;   &lt;/head&gt;&#10;&lt;body&gt;&#10;    &lt;header&gt;&#10;        &lt;h1&gt;Renewable Energy Sources&lt;/h1&gt;&#10;        &lt;p&gt;Exploring the future of clean and sustainable energy&lt;/p&gt;&#10;    &lt;/header&gt;&#10;&#10;    &lt;nav&gt;&#10;        &lt;a href=&quot;#solar&quot;&gt;Solar Power&lt;/a&gt;&#10;        &lt;a href=&quot;#wind&quot;&gt;Wind Energy&lt;/a&gt;&#10;        &lt;a href=&quot;#hydro&quot;&gt;Hydropower&lt;/a&gt;&#10;    &lt;/nav&gt;&#10;&#10;    &lt;div class=&quot;container&quot;&gt;&#10;        &lt;main&gt;&#10;            &lt;h2 id=&quot;solar&quot;&gt;Solar Power&lt;/h2&gt;&#10;            &lt;p&gt;Solar energy is one of the most abundant and clean sources of renewable energy. It uses photovoltaic cells to convert sunlight directly into electricity.&lt;/p&gt;&#10;        &#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;    &lt;img src=&quot;https://images.stockcake.com/public/b/7/a/b7a38663-0207-4222-932a-d25a576f5dd7_large/solar-power-generation-stockcake.jpg&quot; alt=&quot;Wind turbines at sunset.&quot; /&gt;&#10;&#10;&#10;&#10;            &lt;h2 id=&quot;wind&quot;&gt;Wind Energy&lt;/h2&gt;&#10;            &lt;p&gt;Wind turbines harness the kinetic energy of the wind and transform it into electricity. Wind energy is growing rapidly as a sustainable alternative to fossil fuels.&lt;/p&gt;&#10;&#10;            &lt;h2 id=&quot;hydro&quot;&gt;Hydropower&lt;/h2&gt;&#10;            &lt;p&gt;Hydropower generates electricity by capturing the energy of moving water, usually from rivers or dams. It is a reliable and proven source of renewable energy.&lt;/p&gt;&#10;        &lt;/main&gt;&#10;    &lt;/div&gt;&#10;&#10;    &lt;footer&gt;&#10;        &lt;p&gt;&amp;copy; 2025 Renewable Insights  &lt;a href= &quot;#&quot; style= &quot;color: #fff;&quot; &gt;Contact Us &lt;/a&gt; &lt;/p&gt; &#10;  &lt;/footer&gt; &#10; &lt;/body&gt; &#10; &lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/51.png" ></td>
</tr>
<tr>
    <td>32</td>
    <td>`image-alt-not-descriptive`</td>
    <td>Critical</td>
    <td>Alternative text is present but is inaccurate, misleading, or does not correctly describe the content or purpose of the image.</td>
    <td class="wrap-cell">
        <pre>&lt;!DOCTYPE html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;    &lt;meta charset=&quot;UTF-8&quot;&gt;&#10;    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;&#10;    &lt;meta name=&quot;description&quot; content=&quot;A simple webpage promoting mental health awareness and well-being.&quot;&gt;&#10;    &lt;title&gt;Mental Health Awareness&lt;/title&gt;&#10;    &lt;/head&gt;&#10;&lt;body&gt;&#10;    &lt;header&gt;&#10;        &lt;h1&gt;Mental Health Matters&lt;/h1&gt;&#10;        &lt;p&gt;Promoting awareness, reducing stigma, and encouraging self-care&lt;/p&gt;&#10;    &lt;/header&gt;&#10;&#10;    &lt;nav&gt;&#10;        &lt;a href=&quot;#importance&quot;&gt;Importance&lt;/a&gt;&#10;        &lt;a href=&quot;#tips&quot;&gt;Self-Care Tips&lt;/a&gt;&#10;        &lt;a href=&quot;#resources&quot;&gt;Resources&lt;/a&gt;&#10;    &lt;/nav&gt;&#10;&#10;    &lt;div class=&quot;container&quot;&gt;&#10;        &lt;main&gt;&#10;            &lt;h2 id=&quot;importance&quot;&gt;The Importance of Mental Health&lt;/h2&gt;&#10;            &lt;p&gt;Mental health is vital to overall well-being. It affects how we think, feel, and act in our daily lives. \n Recognizing its importance helps reduce stigma and promotes a supportive community.&lt;/p&gt;&#10;            &#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;img src=&quot;https://thumbs.dreamstime.com/b/mental-health-infographic-diagram-chart-illustration-banner-presentation-has-managing-stress-meaning-purpose-staying-active-315756097.jpg&quot; \n
          alt=&quot;A diagram of unrelated objects and ideas, possibly showcasing the lifecycle of a butterfly, an exercise routine, or random abstract symbols.&quot; /&gt;&#10;&#10;            &#10;&#10;&lt;h2 id=&quot;tips&quot;&gt;Self-Care Tips&lt;/h2&gt;&#10;            &lt;p&gt;Taking care of your mental health is essential. Here are a few tips:&lt;/p&gt;&#10;            &lt;ul&gt;&#10;                &lt;li&gt;Practice mindfulness or meditation&lt;/li&gt;&#10;                &lt;li&gt;Stay physically active&lt;/li&gt;&#10;                &lt;li&gt;Maintain a balanced diet&lt;/li&gt;&#10;                &lt;li&gt;Connect with loved ones&lt;/li&gt;&#10;                &lt;li&gt;Seek professional help when needed&lt;/li&gt;&#10;            &lt;/ul&gt;&#10;&#10;            &lt;h2 id=&quot;resources&quot;&gt;Helpful Resources&lt;/h2&gt;&#10;            &lt;p&gt;If you&#x27;re struggling with your mental health, don&#x27;t hesitate to reach out for help. Here are some trusted resources:&lt;/p&gt;&#10;            &lt;ul&gt;&#10;                &lt;li&gt;&lt;a href=&quot;#&quot;&gt;National Mental Health Hotline&lt;/a&gt;&lt;/li&gt;&#10;                &lt;li&gt;&lt;a href=&quot;#&quot;&gt;Mindfulness and Meditation Apps&lt;/a&gt;&lt;/li&gt;&#10;                &lt;li&gt;&lt;a href=&quot;#&quot;&gt;Support Groups in Your Area&lt;/a&gt;&lt;/li&gt;&#10;            &lt;/ul&gt;&#10;        &lt;/main&gt;&#10;    &lt;/div&gt;&#10;&#10;    &lt;footer&gt;&#10;        &lt;p&gt;&amp;copy; 2025 Mental Health Awareness  &lt;a href= &quot;#&quot; style= &quot;color: #fff; &quot; &gt;Contact Us &lt;/a&gt; &lt;/p&gt; &#10;    &lt;/footer&gt; &#10; &lt;/body&gt; &#10; &lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/52.png" ></td>
</tr>
<tr>
    <td>33</td>
    <td>`button-label-mismatch`</td>
    <td>Critical</td>
    <td>An element with the button role has a label or accessible name, but it does not accurately describe the action or result produced by activating it.</td>
    <td>
        <pre>&lt;!DOCTYPE html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;    &lt;meta charset=&quot;UTF-8&quot;&gt;&#10;    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;&#10;    &lt;meta name=&quot;description&quot; content=&quot;A webpage promoting sustainable living with an interactive feature to display eco-friendly tips.&quot;&gt;&#10;    &lt;title&gt;Sustainable Living&lt;/title&gt;&#10;    &lt;/head&gt;&#10;&lt;body&gt;&#10;    &lt;header&gt;&#10;        &lt;h1&gt;Sustainable Living&lt;/h1&gt;&#10;        &lt;p&gt;Small steps for a greener planet.&lt;/p&gt;&#10;    &lt;/header&gt;&#10;&#10;    &lt;div class=&quot;container&quot;&gt;&#10;        &lt;main&gt;&#10;            &lt;h2&gt;Eco-Friendly Tips&lt;/h2&gt;&#10;            &lt;p&gt;Click the button below to reveal practical tips for sustainable living:&lt;/p&gt;&#10;         &#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;   &lt;button id=&quot;revealTips&quot; role=&quot;button&quot; aria-label=&quot;Submit Form&quot;&gt;Show Tips&lt;/button&gt;&#10;&#10;&#10;            &lt;div id=&quot;tips&quot; class=&quot;tips&quot;&gt;&#10;                &lt;h3&gt;Eco-Friendly Tips&lt;/h3&gt;&#10;                &lt;ul&gt;&#10;                    &lt;li&gt;Reduce, reuse, and recycle wherever possible.&lt;/li&gt;&#10;                    &lt;li&gt;Conserve water by fixing leaks and using water-efficient appliances.&lt;/li&gt;&#10;                    &lt;li&gt;Opt for energy-efficient lighting and appliances.&lt;/li&gt;&#10;                    &lt;li&gt;Support local and sustainable products.&lt;/li&gt;&#10;                    &lt;li&gt;Plant trees or grow your own garden to offset your carbon footprint.&lt;/li&gt;&#10;                &lt;/ul&gt;&#10;            &lt;/div&gt;&#10;        &lt;/main&gt;&#10;    &lt;/div&gt;&#10;&#10;    &lt;footer&gt;&#10;        &lt;p&gt;&amp;copy; 2025 Sustainable Living Initiative  &lt;a href=&quot;#&quot; style=&quot;color: #fff;&quot;&gt;Contact Us&lt;/a&gt;&lt;/p&gt;&#10;    &lt;/footer&gt;&#10;&#10;    &lt;script&gt;&#10;        const button = document.getElementById(&#x27;revealTips&#x27;);&#10;        const tips = document.getElementById(&#x27;tips&#x27;);&#10;&#10;        button.addEventListener(&#x27;click&#x27;, () =&gt; {&#10;            tips.style.display = tips.style.display === &#x27;block&#x27; ? &#x27;none&#x27; : &#x27;block&#x27;;&#10;        });&#10;    &lt;/script&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/53.png" ></td>
</tr>
<tr>
    <td>34</td>
    <td>`button-label-mismatch`</td>
    <td>Critical</td>
    <td>An element with the button role has a label or accessible name, but it does not accurately describe the action or result produced by activating it.</td>
    <td>
        <pre>&lt;!DOCTYPE html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;    &lt;meta charset=&quot;UTF-8&quot;&gt;&#10;    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;&#10;    &lt;meta name=&quot;description&quot; content=&quot;A webpage promoting healthy eating habits with interactive tips on balanced diets.&quot;&gt;&#10;    &lt;title&gt;Healthy Eating Habits&lt;/title&gt;&#10;    &lt;/head&gt;&#10;&lt;body&gt;&#10;    &lt;header&gt;&#10;        &lt;h1&gt;Healthy Eating&lt;/h1&gt;&#10;        &lt;p&gt;Simple steps to build better eating habits.&lt;/p&gt;&#10;    &lt;/header&gt;&#10;&#10;    &lt;div class=&quot;container&quot;&gt;&#10;        &lt;main&gt;&#10;            &lt;h2&gt;Healthy Eating Tips&lt;/h2&gt;&#10;            &lt;p&gt;Click the button below to learn more about maintaining a balanced diet:&lt;/p&gt;&#10;            &#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;&lt;button id=&quot;revealTips&quot; aria-label=&quot;Click to go back to the homepage&quot; title=&quot;Click to go back to the homepage&quot;&gt;Show Tips&lt;/button&gt;&#10;&#10;            &lt;div id=&quot;tips&quot; class=&quot;tips&quot;&gt;&#10;                &lt;h3&gt;Tips for a Balanced Diet&lt;/h3&gt;&#10;                &lt;ul&gt;&#10;                    &lt;li&gt;Incorporate more fruits and vegetables into your meals.&lt;/li&gt;&#10;                    &lt;li&gt;Stay hydrated by drinking plenty of water.&lt;/li&gt;&#10;                    &lt;li&gt;Choose whole grains over refined grains.&lt;/li&gt;&#10;                    &lt;li&gt;Limit your intake of added sugars and saturated fats.&lt;/li&gt;&#10;                    &lt;li&gt;Practice portion control to avoid overeating.&lt;/li&gt;&#10;                &lt;/ul&gt;&#10;            &lt;/div&gt;&#10;        &lt;/main&gt;&#10;    &lt;/div&gt;&#10;&#10;    &lt;footer&gt;&#10;        &lt;p&gt;&amp;copy; 2025 Healthy Eating Initiative  &lt;a href=&quot;#&quot; style=&quot;color: #fff;&quot;&gt;Contact Us&lt;/a&gt;&lt;/p&gt;&#10;    &lt;/footer&gt;&#10;&#10;    &lt;script&gt;&#10;        const button = document.getElementById(&#x27;revealTips&#x27;);&#10;        const tips = document.getElementById(&#x27;tips&#x27;);&#10;&#10;        button.addEventListener(&#x27;click&#x27;, () =&gt; {&#10;            tips.style.display = tips.style.display === &#x27;block&#x27; ? &#x27;none&#x27; : &#x27;block&#x27;;&#10;        });&#10;    &lt;/script&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/54.png" ></td>
</tr>
<tr>
    <td>35</td>
    <td>`button-label-mismatch`</td>
    <td>Critical</td>
    <td>An element with the button role has a label or accessible name, but it does not accurately describe the action or result produced by activating it.</td>
    <td>
        <pre>&lt;!DOCTYPE html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;&lt;head&gt;&#10;    &lt;meta charset=&quot;UTF-8&quot;&gt;&#10;    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;&#10;    &lt;meta name=&quot;description&quot; content=&quot;A webpage promoting climate change awareness and actionable steps.&quot;&gt;&#10;    &lt;title&gt;Climate Change Action&lt;/title&gt;&#10;    &lt;/head&gt;&#10;&lt;body&gt;&#10;    &lt;header&gt;&#10;        &lt;h1&gt;Take Action on Climate Change&lt;/h1&gt;&#10;        &lt;p&gt;Simple actions for a sustainable future.&lt;/p&gt;&#10;    &lt;/header&gt;&#10;&#10;    &lt;div class=&quot;container&quot;&gt;&#10;        &lt;main&gt;&#10;            &lt;h2&gt;Get Involved&lt;/h2&gt;&#10;            &lt;p&gt;Click the button below to submit your pledge for climate action:&lt;/p&gt;&#10;        &#10;&lt;!-- Accessibility Violation Starts Here --&gt;  &#10;    &lt;button id=&quot;pledgeButton&quot; aria-label=&quot;Upload Document&quot;&gt;Learn More&lt;/button&gt;&#10;            &#10;&#10;            &lt;div id=&quot;formContainer&quot; class=&quot;form-container&quot;&gt;&#10;                &lt;h3&gt;Your Climate Pledge&lt;/h3&gt;&#10;                &lt;form&gt;&#10;                    &lt;label for=&quot;name&quot;&gt;Your Name:&lt;/label&gt;&#10;                    &lt;input type=&quot;text&quot; id=&quot;name&quot; name=&quot;name&quot; placeholder=&quot;Enter your name&quot;&gt;&#10;&#10;                    &lt;label for=&quot;email&quot;&gt;Your Email:&lt;/label&gt;&#10;                    &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; placeholder=&quot;Enter your email&quot;&gt;&#10;&#10;                    &lt;button type=&quot;submit&quot;&gt;Submit Pledge&lt;/button&gt;&#10;                &lt;/form&gt;&#10;            &lt;/div&gt;&#10;        &lt;/main&gt;&#10;    &lt;/div&gt;&#10;&#10;    &lt;footer&gt;&#10;        &lt;p&gt;&amp;copy; 2025 Climate Change Initiative  &lt;a href=&quot;#&quot; style=&quot;color: #fff;&quot;&gt;Contact Us&lt;/a&gt;&lt;/p&gt;&#10;    &lt;/footer&gt;&#10;&#10;    &lt;script&gt;&#10;        const button = document.getElementById(&#x27;pledgeButton&#x27;);&#10;        const formContainer = document.getElementById(&#x27;formContainer&#x27;);&#10;&#10;        button.addEventListener(&#x27;click&#x27;, () =&gt; {&#10;            formContainer.style.display = formContainer.style.display === &#x27;block&#x27; ? &#x27;none&#x27; : &#x27;block&#x27;;&#10;        });&#10;    &lt;/script&gt;&#10;&lt;/body&gt;&#10;&lt;/html&gt;</pre>
        </p>            
    </td>
    <td><img src="https://github.com/NadeenAhmad/AccessGuruLLM/blob/main/data/accessguru_dataset/accessguru_semantic_violations_sampled_dataset_supp_material/55.png" ></td>
</tr>
</table>

import os
import re
import ast
import pandas as pd
from bs4 import BeautifulSoup

import os
import re
import ast
import pandas as pd
from bs4 import BeautifulSoup

# Path where all your scraped HTML files are stored
html_base_path = "/workspace/FullPipeline/html_pages_async"



def find_matching_ul(soup, snippet_html):
    snippet_soup = BeautifulSoup(snippet_html, 'html.parser')
    snippet_ul = snippet_soup.find('ul')
    if not snippet_ul:
        return None

    snippet_classes = set(snippet_ul.get('class', []))

    for ul in soup.find_all('ul'):
        ul_classes = set(ul.get('class', []))
        if snippet_classes.issubset(ul_classes):
            return str(ul)

    return None


def get_landmark_container_for_tag(soup, tag_name='main'):
    tag = soup.find(lambda tag: tag.name == tag_name or tag.get('role', '').lower() == tag_name)
    if not tag:
        return None, f"No <{tag_name}> tag or role='{tag_name}' found"

    landmark_roles = {'banner', 'complementary', 'main', 'contentinfo', 'navigation', 'region'}
    current = tag.parent

    while current:
        role = current.get('role', '').lower()
        if role in landmark_roles or current.name in landmark_roles:
            return current, None
        current = current.parent if hasattr(current, 'parent') else None

    return tag, None


def role_or_tag(role_value, tag_name):
    return lambda tag: tag.name == tag_name or tag.attrs.get("role") == role_value


def extract_supplementary_info(row):
    html_base_path = "/content"
    # Skip if supplementary_information already exists and is non-empty
    if pd.notna(row.get("supplementary_information")) and str(row.get("supplementary_information")).strip():
        return row["supplementary_information"]

    violation = row["violation_name"]
    filename = row.get('html_file_name', '')
    
    if not filename.endswith(('.html', '.txt')):
        filename += '.html'

    html_file = os.path.join(html_base_path, filename)
    snippet = row["affected_html_elements"]

    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')
    except Exception as e:
        return f"HTML load error: {e}"

    # ---------- Violation-Specific Logic ----------

    if "color-contrast" in violation or "contrast-enhanced" in violation:
        return row["supplementary_information"]

    # elif any(v in violation for v in ["image-alt", "input-image-alt", "image-alt-not-descriptive", "image-redundant-alt"]):
    #     matches = []
    #     try:
    #         tag_list = ast.literal_eval(snippet) if isinstance(snippet, str) else []
    #     except Exception:
    #         tag_list = []

    #     if isinstance(tag_list, list) and tag_list:
    #         all_imgs = soup.find_all("img")
    #         for tag_html in tag_list:
    #             snippet_clean = re.sub(r'\s+', ' ', tag_html.strip().replace("'", '"'))
    #             for img_tag in all_imgs:
    #                 img_str_clean = re.sub(r'\s+', ' ', str(img_tag).strip().replace("'", '"'))
    #                 if snippet_clean in img_str_clean or img_str_clean in snippet_clean:
    #                     parent = img_tag.find_parent()
    #                     context = str(parent) if parent else str(img_tag)
    #                     matches.append(f"Image src: {img_tag.get('src')} | Context: {context[:500]}")
    #                     break
    #     return "\n\n".join(matches) if matches else ""

    elif any(v in violation for v in ["ambiguous-heading", "empty-heading", "heading-order"]):
        headings = soup.find_all(re.compile(r'^h[1-6]$'))
        results = []

        for heading in headings:
            if not heading.get_text(strip=True):
                next_elements = []
                sibling = heading.find_next_sibling()
                while sibling and len(next_elements) < 3:
                    if sibling.name in ["p", "ul", "ol", "div", "section"]:
                        next_elements.append(str(sibling))
                    sibling = sibling.find_next_sibling()
                results.append(f"{str(heading)}\n\n" + "\n\n".join(next_elements))

        return "\n\n---\n\n".join(results) if results else ""

    elif "empty-table-header" in violation:
        headers = soup.find_all("th")
        results = []

        for th in headers:
            if not th.get_text(strip=True):
                next_elements = []
                sibling = th.find_next_sibling()
                while sibling and len(next_elements) < 3:
                    if sibling.name in ["td", "th", "tr"]:
                        next_elements.append(str(sibling))
                    sibling = sibling.find_next_sibling()
                results.append(f"{str(th)}\n\n" + "\n\n".join(next_elements))

        return "\n\n---\n\n".join(results) if results else ""

    elif "page-has-heading-one" in violation:
        title_html = str(soup.title) if soup.title and soup.title.string else ""
        h1_tags = soup.find_all("h1")
        h1_html = "\n\n".join(str(h) for h in h1_tags[:3]) if h1_tags else ""
        return f"{title_html}\n\n---\n\n{h1_html}"

    elif "page-title-not-descriptive" in violation:
        title_html = str(soup.title) if soup.title and soup.title.string else ""
        headings = soup.find_all(re.compile(r"^h[1-6]$"))
        heading_html = [str(h) for h in headings[:10]]
        return f"{title_html}\n\n---\n\n" + "\n\n".join(heading_html) if heading_html else title_html

    elif "document-title" in violation:
        title_html = str(soup.title) if soup.title and soup.title.string and soup.title.string.strip() else ""
        # title_html = str(soup.title) if soup.title and soup.title.string.strip() else ""
        headings = soup.find_all(re.compile(r"^h[1-6]$"))
        heading_html = [str(h) for h in headings[:10]]
        return f"{title_html}\n\n---\n\n" + "\n\n".join(heading_html) if heading_html else title_html

    elif any(v in violation for v in [
        "duplicate-id", "duplicate-id-aria", "duplicate-id-active",
        "landmark-no-duplicate-contentinfo", "landmark-no-duplicate-main",
        "landmark-no-duplicate-banner", "landmark-unique"
    ]):
        report = []

        # Duplicate ID check
        if any(v in violation for v in ["duplicate-id", "duplicate-id-aria", "duplicate-id-active"]):
            id_map = {}
            for tag in soup.find_all(attrs={"id": True}):
                id_map.setdefault(tag["id"], []).append(tag)

            duplicates = {k: v for k, v in id_map.items() if len(v) > 1}
            for dup_id, elements in list(duplicates.items())[:5]:
                report.append(f"ID '{dup_id}' is used {len(elements)} times:")
                for el in elements[:3]:
                    snippet = str(el)
                    report.append(snippet if len(snippet) <= 500 else snippet[:500] + "...")

        # Duplicate landmarks
        if "landmark-no-duplicate-contentinfo" in violation:
            contentinfos = soup.find_all(role_or_tag("contentinfo", "footer"))
            if len(contentinfos) > 1:
                report.append(f"{len(contentinfos)} <footer> or role='contentinfo' elements found:\n" +
                              "\n---\n".join(str(tag) for tag in contentinfos))

        if "landmark-no-duplicate-main" in violation:
            mains = soup.find_all(role_or_tag("main", "main"))
            if len(mains) > 1:
                report.append(f"{len(mains)} <main> or role='main' elements found:\n" +
                              "\n---\n".join(str(tag) for tag in mains))

        if "landmark-no-duplicate-banner" in violation:
            banners = soup.find_all(role_or_tag("banner", "header"))
            if len(banners) > 1:
                report.append(f"{len(banners)} <header> or role='banner' elements found:\n" +
                              "\n---\n".join(str(tag) for tag in banners))

        if "landmark-unique" in violation:
            roles = ["main", "banner", "contentinfo", "navigation", "search", "complementary", "form"]
            for role in roles:
                tags = soup.find_all(attrs={"role": role})
                if len(tags) > 1:
                    report.append(f"Role '{role}' found {len(tags)} times:\n" +
                                  "\n---\n".join(str(tag) for tag in tags))

        return "\n\n".join(report) if report else ""

    # elif "list" in violation:
    #     try:
    #         tag_list = ast.literal_eval(snippet) if isinstance(snippet, str) else []
    #     except Exception:
    #         tag_list = []

    #     matched_lists = [find_matching_ul(soup, ul_snippet) for ul_snippet in tag_list]
    #     matched_lists = [ul for ul in matched_lists if ul]
    #     return "\n\n---\n\n".join(matched_lists) if matched_lists else ""

    elif violation in [
        "landmark-main-is-top-level", "landmark-banner-is-top-level", "landmark-complementary-is-top-level"
    ]:
        tag_map = {
            "landmark-main-is-top-level": "main",
            "landmark-banner-is-top-level": "banner",
            "landmark-complementary-is-top-level": "complementary"
        }
        tag_role = tag_map.get(violation, "main")
        container, error = get_landmark_container_for_tag(soup, tag_role)
        return str(container) if container else ""

    elif any(v in violation for v in [
        "lang-mismatch", "missing-lang-tag", "html-lang-valid",
        "html-xml-lang-mismatch", "valid-lang", "html-has-lang"
    ]):
        title = soup.title.string.strip() if soup.title and soup.title.string else "No <title> tag or title is empty"
        headings = soup.find_all(re.compile(r'^h[1-6]$'))
        heading_texts = [f"{h.name.upper()}: {h.get_text(strip=True)}" for h in headings if h.get_text(strip=True)]
        return f"Title: {title} | Headings: {' | '.join(heading_texts[:10])}" if heading_texts else f"Title: {title}"

    return ""


def check_if_htmlpathExist():
    base_dir = "WebAccessibility/data/raw_html/"
    final_df["full_path"] = final_df["html_file_name"].apply(
        lambda name: os.path.join(base_dir, name) if isinstance(name, str) else None
    )
    final_df["file_exists"] = final_df["full_path"].apply(
        lambda path: os.path.exists(path) if path else False
    )
    missing = final_df[~final_df["file_exists"]]
    print(f"Missing HTML files: {len(missing)}")
    print(missing[["web_url", "html_file_name"]].head())
    print(list(missing["web_url"]))


# violation_df = pd.read_csv("2_Extended_havingColorSupplimentary.csv")
# violation_df['supplementary_information'] = violation_df.apply(extract_supplementary_info, axis=1)
# violation_df.to_csv("Extended_havingAllSupplimentary.csv", index=False)

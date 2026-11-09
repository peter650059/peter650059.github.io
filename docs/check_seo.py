#!/usr/bin/env python3
"""Check Jekyll's generated SEO output using only the Python standard library.

Run after `JEKYLL_ENV=production bundle exec jekyll build`:
    python3 docs/check_seo.py
Optionally compare the rendered body with a saved pre-change index.html:
    python3 docs/check_seo.py --baseline /path/to/previous/index.html
"""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
URL = "https://peter650059.github.io/"
TITLE = "Jun-Hsiang Yao (姚闰翔) | Homepage"
DESCRIPTION = (
    "Jun-Hsiang Yao (姚闰翔) is a PhD student at Fudan University. "
    "His research focuses on Augmented and Virtual Reality (AR/VR), "
    "Human-Computer Interaction (HCI), Data Visualization (VIS), and AI."
)
SCHOLAR = "https://scholar.google.com/citations?user=NbqwkFcAAAAJ"
VERIFICATION = "google613fd477ba4be6bd.html"


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def select(self, tag, **attrs):
        return [a for t, a in self.tags if t == tag and all(a.get(k) == v for k, v in attrs.items())]


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def one(nodes, message):
    require(len(nodes) == 1, message)
    return nodes[0]


def check(baseline=None):
    output = ROOT / "_site"
    html = (output / "index.html").read_text(encoding="utf-8")
    require(len(re.findall(r"<head\b", html)) == 1 and html.count("</head>") == 1, "exactly one head")
    head = html.split("<head>", 1)[1].split("</head>", 1)[0]
    parsed = Document(head)
    title = one(re.findall(r"<title>(.*?)</title>", head, re.S), "one title")
    require(title == TITLE, "homepage title")
    expected = {
        "description": DESCRIPTION, "og:title": TITLE, "og:description": DESCRIPTION,
        "og:url": URL, "og:type": "website", "og:site_name": "Jun-Hsiang Yao (姚闰翔)",
        "twitter:card": "summary", "twitter:title": TITLE, "twitter:description": DESCRIPTION,
    }
    for name, value in expected.items():
        attr = "property" if name.startswith("og:") else "name"
        node = one(parsed.select("meta", **{attr: name}), "one " + name)
        require(node.get("content") == value, name + " content")
    require(one(parsed.select("link", rel="canonical"), "one canonical")["href"] == URL, "canonical URL")
    require(one(parsed.select("base"), "one base target").get("target") == "_blank", "preserve link behavior")
    require(not re.search(r"\b(noindex|nofollow|none)\b", " ".join(
        a.get("content", "").lower() for a in Document(html).select("meta")
        if a.get("name", "").lower() in {"robots", "googlebot"}
    )), "homepage permits indexing and following")

    data = one(re.findall(r'<script type="application/ld\+json">(.*?)</script>', head, re.S), "one JSON-LD graph")
    graph = json.loads(data)
    require(graph["@context"] == "https://schema.org", "schema context")
    entities = graph["@graph"]
    require(len(entities) == 2, "exactly WebSite and Person")
    website = one([e for e in entities if e["@type"] == "WebSite"], "one WebSite")
    person = one([e for e in entities if e["@type"] == "Person"], "one Person")
    require(website["name"] == "Jun-Hsiang Yao (姚闰翔)" and website["url"] == URL, "website identity")
    require(set(website["alternateName"]) == {"Jun-Hsiang Yao", "Jun Hsiang Yao", "姚闰翔"}, "website aliases")
    require(website["publisher"]["@id"] == person["@id"] == URL + "#person", "linked person identity")
    require(person["name"] == "Jun-Hsiang Yao" and person["url"] == URL, "person identity")
    require(set(person["alternateName"]) == {"姚闰翔", "Jun Hsiang Yao"}, "person aliases")
    require(person["jobTitle"] == "PhD Student", "academic position")
    require(person["affiliation"]["name"] == "School of Data Science", "school")
    require(person["affiliation"]["parentOrganization"]["name"] == "Fudan University", "university")
    require(person["description"] == DESCRIPTION and len(person["knowsAbout"]) == 4, "research description")
    require(person["sameAs"] == [SCHOLAR], "only the confirmed Scholar profile")
    require(any(a.get("href") == SCHOLAR for a in Document(html).select("a")), "sameAs is a visible profile link")
    require((output / urlparse(person["image"]).path.lstrip("/")).is_file(), "person image exists")
    require(not Document(html).select("div", itemtype="http://schema.org/Person"), "no duplicate empty Person microdata")

    robots = RobotFileParser()
    robots.parse((output / "robots.txt").read_text().splitlines())
    require(robots.can_fetch("Googlebot", URL), "robots permits homepage crawl")
    require(robots.site_maps() == [URL + "sitemap.xml"], "absolute sitemap in robots")
    sitemap = ElementTree.parse(output / "sitemap.xml")
    urls = [n.text for n in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    require(URL in urls and len(urls) == len(set(urls)), "homepage in sitemap without duplicates")
    require(all(u.startswith(URL) for u in urls), "absolute HTTPS sitemap URLs")
    require(URL + VERIFICATION not in urls, "verification token excluded from sitemap")
    require((output / VERIFICATION).read_bytes() == (ROOT / VERIFICATION).read_bytes(), "verification file preserved exactly")
    for alias in ("about/index.html", "about.html"):
        redirect = Document((output / alias).read_text())
        require(one(redirect.select("link", rel="canonical"), alias + " canonical")["href"] == URL, "redirect canonical")
        require("noindex" in one(redirect.select("meta", name="robots"), alias + " robots")["content"], "redirect aliases remain noindex")
    require(not (output / "docs/check_seo.py").exists(), "checks are excluded from publication")

    if baseline:
        def body(text):
            text = text.split("<body>", 1)[1].split("</body>", 1)[0]
            # Liquid also expands site.description inside legacy HTML comments.
            text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
            text = re.sub(r"\?v=\d+", "?v=BUILD", text)
            return text.replace(' itemscope itemtype="http://schema.org/Person"', '')
        require(body(html) == body(Path(baseline).read_text(encoding="utf-8")), "body unchanged except comments, empty schema attributes and asset timestamp")
        print("PASS: rendered body, content and interactions preserved")
    print("PASS: metadata, JSON-LD, canonical, crawl access, sitemap, redirects and verification file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path)
    check(parser.parse_args().baseline)

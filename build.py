"""
python port of https://github.com/wooorm/html-element-attributes/blob/main/build.js
"""
from bs4 import BeautifulSoup
import requests
import re
import sys
import collections

sys.setrecursionlimit(10000)
from HtmlElementAttributes import html_element_attributes

if "*" not in html_element_attributes:
    html_element_attributes["*"] = []

global_attribs = html_element_attributes["*"]

page = requests.get("https://html.spec.whatwg.org/multipage/indices.html")
soup = BeautifulSoup(page.content, "html5lib")

for row in soup.select("#attributes-1 tbody  tr"):
    name = row.find("th").get_text().strip()
    value = row.find("td").get_text().strip()

    if re.search(r"custom elements", value, re.I):
        continue

    elements = (
        ["*"]
        if re.search(r"HTML elements", value, re.I)
        else [re.sub(r"\([^)]+\)", "", x).strip() for x in value.split(";")]
    )

    for element in elements:
        # print(element)
        element = element.lower()

        if element not in html_element_attributes:
            html_element_attributes[element] = []

        if name not in html_element_attributes[element]:
            html_element_attributes[element].append(name)

# sort values
final_list = {}
for x in html_element_attributes:
    sorted_attributes = list(
        sorted(
            (
                filter(
                    lambda g: g not in global_attribs or x == "*",
                    html_element_attributes[x],
                )
            )
        )
    )
    if sorted_attributes:
        final_list[x] = sorted_attributes

# sort keys
html_element_attributes = dict(collections.OrderedDict(sorted(final_list.items())))

with open(
    "HtmlElementAttributes/html_element_attributes.py", "w+", encoding="utf8"
) as built:
    built.write(
        f"""\"\"\"
List of known HTML attributes names.
\"\"\"

html_element_attributes = {html_element_attributes}"""
    )

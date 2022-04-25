<h1 align="center">HTML Element Attributes</h1>

<h4 align="center">List of known HTML tag attribute names.</h4>

<h5 align="center">Python port of npm package <a href="https://www.npmjs.com/package/html-element-attributes" target="_blank">html-element-attributes</a>.</h5>

<p align="center">
  <a href="https://pypi.org/project/html-element-attributes/">
    <img src="https://badgen.net/pypi/v/html-element-attributes" alt="Pypi Version">
  </a>
  <a href="https://pepy.tech/project/html-element-attributes">
    <img src="https://static.pepy.tech/badge/html-element-attributes" alt="Downloads">
  </a>
</p>

## 🤔 What is this?

This is a list of HTML tag attribute names.

## 💾 Install

```sh
pip install html-element-attributes
```

## ✨ How to Use

```py
from HtmlTagNames import html_element_attributes

print(html_element_attributes["*"])
```

Yields:

```py
[
  'accesskey',
  'autocapitalize',
  'autofocus',
  'class',
  // …
  'style',
  'tabindex',
  'title',
  'translate'
]
```
## License

- [GPL][license] © Riverside Healthcare
- Ported from `html-element-attributes` [MIT][LICENSE] © [Titus Wormer](https://github.com/wooorm)

[license]: LICENSE

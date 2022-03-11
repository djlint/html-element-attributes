# HtmlElementAttributes

Python port of npm package [html-element-attributes](https://www.npmjs.com/package/html-element-attributes).

List of known HTML tag attribute names.

## What is this?

This is a list of HTML tag attribute names.

## Install

```sh
pip install html-element-attributes
```

## Use

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

[GPL][license] © Riverside Healthcare
Ported from `html-element-attributes` [MIT][LICENSE] © [Titus Wormer][https://github.com/wooorm]

[license]: LICENSE
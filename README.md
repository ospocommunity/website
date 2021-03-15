# ApacheCon hugo site

This repository contains a Hugo based site for ApacheCon.

To test it locally, run:

```
hugo server -b http://localhost:1313/acasia2021
```

To generate final site, use:


```
hugo  -b https://apachecon.com/acasia2021/ -d <destination_directory>
```

## FAQ

### How can I modify the content of the main page:

It's under `content/_index.md`

### How can I have translations:

Add new language to the `config.toml`:

```
[languages.zh]
languageName = "中文"
weight = 2
```

And create language specific version for each content file:

```
content/_index.md
content/_index.zh.md
content/cfp.md
content/cfp.zh.md
```

### How can I modify the menu?

For simple links, add the menu entry to the `config.toml`:

(Note: add it for all the active languages)

```
[[languages.en.menu.main]]
name = "t-shirt"
url = "https://s.apache.org/apache-tshirt"
weight = -110
```

For a page, it's enough to add a menu entry to the markdown (For example `content/cfp.md`):


```
---
title: Call for Presentations
menu:
  main:
    weight: -300
---
...
...
```

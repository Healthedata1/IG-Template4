---
title: General Guidance and Definitions in Markdown
layout: default
toc: True
---

### Introduction
{:.self-link}

This is how an markdown file is rendered using this set of templates

The YAML frontmatter include the following parameters:

- `title` -  the title for this page
- `layout` - fixed to 'default' which tells the Jekyll publisher where to insert this content into the page
- `toc` - which if True toggles on the page Contents to appear at the top

and it looks like this.

~~~
  ---
  title: More General Guidance and Definitions in HTML
  layout: default
  toc: True
  ---
~~~

Note that to remove a header from the page toc, we apply a class called no_toc, in Kramdown  as "\{:.no_toc\}" right after the header.  This is done below...

#### Here is an example button to accordion fold the long example for easier page navigation:
{:.no_toc}

{% include examplebutton.html example="example" b_title = "Example Button bar" %}

blah blah blah

### More Stuff

inline json example exploiting Rouge to highlight inline comment (errors in json):

~~~json
{
"foo":  "bar"  \\adding comment here is shown as a error in jekyll,
"foo2":  "bar2"
}
~~~

#### And More Stuff

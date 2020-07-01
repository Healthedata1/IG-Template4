### Introduction
{:.self-link}

This is based on {{page.f}}index.html


{% include examplebutton.html example="example" b_title = "Example Button bar" %}


### My list

- list 1
- list 2
  {% include nestedlist3.md %}
      {% include nestedlist3.md %}


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

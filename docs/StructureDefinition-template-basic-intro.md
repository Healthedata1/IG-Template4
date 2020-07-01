
#### MY INTRO

{% assign id = include.id %}

include.id = {{include.id}}<br />
include.type = {{include.type}}<br />

{%raw%}{% assign id = include.id %}{%endraw%}
{% assign id = include.id %}
id = {{id}}<br />

source file: source/pages/\_includes/{{id}}-intro.md

{{site.data.structuredefinitions.[id].description}}

#### Scope and Usage

scope and usage text here

#### Mandatory Data Elements and Terminology

The following data-elements are mandatory (i.e data MUST be present). blah blah blah

**must have:**

1. blah
1. blah
1. blah

**Additional Profile specific implementation guidance:**

#### Examples

- list examples here

Template Notes:

Name =  Jekyll-Kramdown-Liquid approach  JKL

Advantages

No prior knowledge of html, XML
Use pre-existing, well documented tools
Any internal ant processing that is needed can be done using JS (including calling java modules) instead of stylesheets.

Option 1:

use onLoad to update:

- ig.xml resources
- ig.xml pages
- _config.yml parameters
- menu.xml
- logo.md

using ant + js

Option 2 :  pre-process using python

 to update logo and menu interactively?


see /Users/ehaas/Documents/ant_tests for more
~~~
<project>
 <script language="javascript">
  println("hello, world");
 </script>
</project>
~~~

issues to getting builds to work:

parameter are not boolean but string true and false document in confluence.

When using the HL7 template, the IG id must start with "hl7." and some fucking family... ala 'hl7.fhir.us....' for stupid Jira

includes put in includes folder so need to update the rel link for image to <img src="{{include.img}}  images gets dumped into flat temp file.

file:///Users/ehaas/Documents/FHIR/IG-Template4/output/images/cat.jpg

using spreadsheets and listing in ig.json is duplicative.  convewrt spreadsheets to json for now. spreadsheets are f'd up with the ImplementationGuide

all the f'ing markdown is fucked

removing   {::options parse_block_html="true" /}  makes the markdownify work ...
what does it do?...

add in css locally to page begin for ie.

tried to fix this first

update file tree to be like Jekyll docs tree




1. add in layouts for the templates
1. considate the templates
1. add in front matter for the markdown pages
1. add in front matter for the html pages
   1. this means update the stylesheets to add in after validation.

fix the section numbering for sub pages.  - done
checking across browsers

if ends in .0 then works get 3.0 appended.  so need to remove the .0
if ends in .1 etc then skips

e.g. want to to be 4.1 not 4 etc

do QA on IG Template4

notes and intro are leaking into the output folder...! and I don't know why.

output/StructureDefinition-identifier-status-intro.md
output/operations.md
output/StructureDefinition-template-basic-notes.md
output/profiles.md
output/guidance.md
output/capstatements.md
output/StructureDefinition-template-profile-on-profile-intro.md
output/StructureDefinition-ext-complex-intro.md
output/StructureDefinition-ext-identifier-status-intro.md
output/terminology.md
output/StructureDefinition-ext-blah-intro.md
output/StructureDefinition-identifier-status-notes.md
output/index.md
output/ifr-intro.md
output/StructureDefinition-template-basic-intro.md
output/downloads.md
output/StructureDefinition-template-profile-on-profile-notes.md
output/all-examples.md
output/ifr-search.md
output/searchparameters.md



then add the tabs
then the Downloads
then the copy me
then the icons
ignore the ugly toc but option to turn off when not needed using a page parameter in markdown :-)
fix breadcrumbs to actually mimic the menu bar or remove
option to turn off the constraints, term, example tabs as all white noise.
redo artifacts page
custom logos.
temp/includes lists are generating local links???
add front matter to templates so can reference the {{[id]}} and {{[type]}} parameters or and as include variables.  e.g description.. ( description in ig.yml = description in SD )
ie section numbering broken



issue when xml page i the ig resource page.generation code define it be "xml" not "html" which is how ig-pub is implemented.  

so the input/pagecontent/file.xml is in ig resource is ...

~~~
- nameUrl: file.html
  title: File
  generation: html
~~~

I think is confusing to have the xml and generation different...


================================================
renaming intro and notes files:

#### remove diff2

find input/includes  -name "extension-*-diff2.md" -print
find input/includes  -name "extension-*-diff2.md" -exec rm -f {} \;
find input/includes  -name "extension-*-diff2.md" -print
~~~
move input/includes/template-basic-intro.md  to input/pagecontent/StrucureDefinition-template-basic-intro.md
~~~


#### move input/includes/(.*?)-intro.md  to input/pagecontent/StructureDefinition-$1-intro.md

#### ove input/includes/template-basic-search.md  to input/pagecontent/StrucureDefinition-template-basic-notes.md

#### move input/includes/(.*?)-search.md  to input/pagecontent/StrucureDefinition-$1-notes.md

move
~~~
find . -regex '\./input/includes/\(.*\)-search.md' -exec mv -f {} input/pagecontent/ \;
~~~
rename with regex

?

#### move input/includes/extension-complex-intro.md to input/pagecontent/StrucureDefinition-ext-complex-intro.md



#### move input/includes/extension-(.*?)-intro.md to input/pagecontent/StrucureDefinition-ext-$1-intro.md

~~~
find input/includes  -name "extension-*-intro.md" -print
~~~

#### remove input/includes/extension-identifier-status-search.md

~~~
find input/includes  -name "extension-*-search.md" -print
find input/includes  -name "extension-*-search.md" -exec rm -f {} \;
find input/includes  -name "extension-*-search.md" -print
~~~


unable to load template from fork to show rendering output onine.  see zulip:

https://chat.fhir.org/#narrow/stream/179252-IG-creation/topic/running.20templates.20of.20branch.20not.20working.20for.20me

Where is front matter inserted?

>Front Matter Variables Are Optional
If you want to use Liquid tags and variables but don’t need anything in your front matter, just leave it empty! The set of triple-dashed lines with nothing in between will still get Jekyll to process your file. (This is useful for things like CSS and RSS feeds!)

use layouts

add _layouts file to be updated to the temp file

make the section css script an include file

redo the markdown pages to use layouts!

update the toc

update the  base template file tree

from


.
├── README.md
├── cache.ini
├── config
  └── _config.yml
├── config.json
├── content
├── includes
├── layouts
├── my-notes
├── package
├── package-list.json
└── scripts

TO match Jekyll:

├── README.md
├── cache.ini
├── config.json
├── content
│   ├──  _config.yml <-- from folder config above
│   ├── _includes
│   ├── _layouts
│   ├── assets
│   └── jquery.js  <-- do we even need this out here instead of in assets?
│   └── templates
├── my-notes
├── package
├── package-list.json
└── scripts

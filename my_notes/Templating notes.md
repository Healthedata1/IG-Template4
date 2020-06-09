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

1. add in layouts for the templates
1. considate the templates
1. add in front matter for the markdown pages
1. add in front matter for the html pages
1. this means update the stylesheets to add in after validation.
fix the section numbering for sub pages.
if ends in .0 then works get 3.0 appended.  so need to remove the .0
if ends in .1 etc then skips

e.g. want to to be 4.1 not 4 etc - done

it turns out ...

removing   {::options parse_block_html="true" /}  makes the markdownify work ...
what does it do?...

issues:

####  section numbering not working for ie.

checking across browsers

tried to fix this first  ... not working and is a to do see below...

#### notes and intro md pages leaking into the output
 - messes up github pages and I imagine the ig pub too

 for example all these files in my test IG are in output:
~~~
> find output -name "*.md" -print
~~~

-  output/StructureDefinition-identifier-status-intro.md
-  output/operations.md
-  output/StructureDefinition-template-basic-notes.md
-  output/profiles.md
-  output/guidance.md
-  output/capstatements.md
-  output/StructureDefinition-template-profile-on-profile-intro.md
-  output/StructureDefinition-ext-complex-intro.md
-  output/StructureDefinition-ext-identifier-status-intro.md
-  output/terminology.md
-  output/StructureDefinition-ext-blah-intro.md
-  output/StructureDefinition-identifier-status-notes.md
-  output/index.md
-  output/ifr-intro.md
-  output/StructureDefinition-template-basic-intro.md
-  output/downloads.md
-  output/StructureDefinition-template-profile-on-profile-notes.md
-  output/all-examples.md
-  output/ifr-search.md
-  output/searchparameters.md


#### issue when xml page in the ig resource page.generation code define it be "xml" not "html" which is how ig-pub is implemented.  

so the input/pagecontent/file.xml is in ig resource is ...

~~~
- nameUrl: file.html
  title: File
  generation: html
~~~

I think is confusing to have the xml and generation different...

#### markdownify filter can produces invalid (and inappropriate) HTML

When Markdown is used for section headings, for example, the markdownify filter produces invalid (and inappropriate) HTML by wrapping the output in a paragraph tag. if your markdown start with a heading the add a line break - that solves the rendering issue


todo update file tree to be like Jekyll docs tree

1. [X] do QA on IG Template4

tests:
try updated ig-template-base on:
1. [x] IG Template4
1. [x] ig-sampler
1. [x] using autopublishing
      -  need to commit ig-template-base and use that in the ig.ini file:
      `https://github.com/Healthedata1/ig-template-base/tree/update_for_md_rendering`
      - fucking github would not download include file had to delete and add and recommit in for to work!!!
1. [X] sushi - my copy of subscriptions.

commit PR for for ig-template-base !!!


- [ ] **adding pretty tabs for examples**

Issues:

issue - operationdefinition is using example.template and not base like it should.

assume if marked false in ig.json then is defaulting to base.
~~~
- reference:
    reference: OperationDefinition/example
  description: Limited implementation of the Populate Questionnaire implementation
  name: Populate Questionnaire
  exampleBoolean: false
~~~

### lots of QA errors of the type:
~~~
StructureDefinition-backport-heartbeat-period.profile.json.html#/html/body/div/div/div/div/div/p/a at Line 225, column 18	error	The link 'StructureDefinition-backport-heartbeat-period.{}' for "{}" cannot be resolved
~~~

which is referring to this line of html in the file:

~~~
223 <!-- ============ default xml or json view  CONTENT=============== -->
224 <p>
225 Download Raw <a href="StructureDefinition-backport-heartbeat-period.json" download>json</a>
226 </p>
  ...
~~~

???

download latest publisher....

    tests:
    try updated ig-template-base on:
    1. [X] IG Template4
    1. [X] ig-sampler
    1. [ ] using autopublishing - error on the remote template due to security concerns
    1. [X] sushi - my copy of subscriptions.

commit PR for for ig-template-base !!!

├── cache.ini
├── config
├── config.json  <--- **updated to reflected the consolidated "layouts"**
├── content
│   ├── _layouts
│   │   └── fhir-artifact.html  <--- ** added an actual Jekyll layout to handle all the common stuff for the "layouts"**
│   ├── assets
├── includes
│   ├── fragment-css.html
│   ├── fragment-footer.html
│   ├── fragment-header.html
│   ├── fragment-pagebegin.html <--***** minor updates here ******
│   ├── fragment-pageend.html
│   ├── nav-tabs.html <--***** new to handle tabs across all pages ******
│   ├── template-page-md.html
│   └── template-page.html
├── layouts  <---**** consolidated the "layouts" to remove redundant code ****
│   ├── base.html
│   ├── example.html
│   ├── extension.html
│   ├── format.html
│   ├── profile-definitions.html
│   ├── profile-examples.html
│   ├── profile-mappings.html
│   └── profile.html
├── package
│   └── package.json
├── package-list.json
└── scripts


- [ ] then the downloads link
- [ ] then the copy me
- [ ] then the icons
- [ ] ignore the ugly toc but option to turn off when not needed using a page parameter in markdown :-)
- [ ] fix breadcrumbs to actually mimic the menu bar or remove
- [ ] option to turn off the constraints, term, example tabs as all white noise.
- [ ] redo artifacts page
- [ ] custom logos.
- [ ] temp/includes lists are generating local links???
- [ ] add front matter to templates so can reference the {{[id]}} and {{[type]}} parameters or and as include variables.  e.g description.. ( description in ig.yml = description in SD )
- [ ] ie section numbering broken
- [ ] addin open api



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


## adding pretty tabs for examples:

issue - operationdefinition is using example.template and not base like it should.

assume if marked false in ig.json then is defaulting to base.
~~~
- reference:
    reference: OperationDefinition/example
  description: Limited implementation of the Populate Questionnaire implementation
  name: Populate Questionnaire
  exampleBoolean: false
~~~

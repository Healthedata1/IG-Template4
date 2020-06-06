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



fix this first

1. add in layouts for the templates
1. considate the templates
1. add in front matter for the markdown pages
1. add in front matter for the html pages
   1. this means update the stylesheets to add in after validation.


then add the tabs
then the Downloads
then the copy me
then the icons
ignore the ugly toc but turn them off when not needed using a page parameter in markdown :-)

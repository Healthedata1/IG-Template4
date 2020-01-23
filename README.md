see https://wiki.hl7.org/FHIR_IG_publisher_templates

## TODOS
1. autoload_resources  - test this native functionality does it load the pages test pending
1. autoload_pages - test if pages load natively from directory that mimics the menu - no relative links get messed up.
1. autoload resource into pages - file name based - test pending
1. check if html works too. - it does indeed and fixed toc-for-pages to work in the layout
1. check out all parameters or extra Parameters -  todo error on qa
1. bash should error if no front matter in pages - todo
1. menu should have fixed and variable parts. - done see below
   -  use yaml file to define menu. variable parts of it?
1. fix markdown friendly images in lloyd's template
   - issue with not following boot strap and spurious tags - discuss
1. add logo variable - done
1. Discuss with Lloyd:
    1. update css to test modify locally
    2. add section numbering for ie - todo
    3. update look and feel -
    4. add copy me, and external and download icons
    5. update and simplify layout
    6. suggest new file tree structure


## Using Lloyds template
-  need to rename directories:
  - `source` to `include`
  - `_includes` to `includes` and move to input dir  this is not how Jekyll spec defines this!
  - 'pages' to 'pagecontent'
  - this file to input folder 'ignoreWarnings.tx'
  - note that temp/input-cache all outside of generated_files directory
- need to add extensions for each spreadsheet to ig.xml (need to do this for for my template as well )
     -add extensions for spreadsheets that go in ig.xml or ig.yml

    ~~~
    <extension url="http://hl7.org/fhir/StructureDefinition/igpublisher-spreadsheet">
      <valueUri value="structuredefinition-sdc-profile-spreadsheet.xml"/>
    </extension>
    ~~~

- file names need to match ids !!  stoopid!!
- remove toc.html from IG since being created 2x by lloyd scripts Arggghhhh...
- menu.xml is missing since is menu.md changed to xml and add a stupid namespace !!!
    - see my solution using yaml
- moved example-list-generator.md and schematron-list-generator example button files and image files to includes directory  these are framework things that should not be mixed with the user data
- strip out front matter
  - antipattern to Jekyll
- ### Result is IG with several rendering issues.
- ### saved as branch and start over with my own templates :-)

## JKL branch

The approach here is to use my existing framework and no ant scripting.
Use bash script tooling on the front end to create and install the
config files and run ig-pub without internal scripting

notes to using publish.sh:
- to use load template use -l parameter
- to use local (test) template use -u parameter
- to use loaded template no -l or -u parameters

Assemble all the configuration and menu on the front using scripting tools and/or hand editing of source files and default menu (navigation.yml).  To use online scripts will need to be able to access files from a GitRepro or upload files to the online tool.  file will need to be downloaded locally to update your ig.

*NOTE can't overwrite _data files in source. need create separate file and use control logic in templates.. *

**project logo**

Default template logo can't be overwritten locally. Add custom logo as "source/pages/assets/images/custom_org_logo.jpg" and the template will use it instead of default template project logo. Also need a paramenter for the logo url.  not sure that is always  {{site.data.fhir.ig.contact[0].telecom[0]}}

See header.html for liquid code

**custom menu**

Default template menu can't be overwritten locally. Add custom menu in source as "source/pages/_data/ig_navigation.yml" and the template will use it instead of default template project menu.

See navbar.html for liquid code

### get all parameters in ig and test.

#### list the static and dynamic configs.
~~~
Erics-Air-2:IG-Template4 ehaas$ tree -L 2 -I '*.png|*.gif|*.js|docs|my_notes'
.
├── generated_output
│   ├── qa
│   ├── temp
│   └── txCache
├── ig.ini  **** 1. dynamic from bash
├── ig.ini.bak
├── my_framework
│   ├── config.json 3. *** this should be static based on templates
│   ├── content
│   │   ├── 2._config.yml add parameters from ig resource or let data file do this?
│   │   └── _data
│   │   │   └── 5. navigation.yml - defines top bar menu using YML - define at beginning along with ig resource
│   ├── package 4. package.json file  -this is template specific and static
│   └── templates
├── publish.sh
├── source
│   ├── examples
│   ├── history
│   ├── html_pages
│   ├── pages
│   └── resources  5. ig resource which will treat like the grandaddy config file
├── temp
│   ├── _data
│   ├── _includes
│   ├── fhir.css
│   └── link.svg
└── template
    ├── _config.yml
    ├── config.json
    ├── content
    ├── package
    └── templates  -->
~~~

1. ig.ini  modified by bash file publish.sh locally

    ~~~
    [IG]
    ig = source/resources/ig.xml  # fixed location
    #template = hl7.fhir.template to load from repository  # based on publish.sh for standard template
    #template = /Users/ehaas/Documents/FHIR/IG-Template2  # based on publish.sh  to load locally for local dev
    template = /Users/ehaas/Documents/FHIR/IG-Template4/my_framework  # based on publish.sh default dev option
    usage-stats-opt-out = true  # not sure if works but make option from publish.sh
    #guidename must match the id of the implementation guide
    guidename=healthedatainc.ig-template4-0.0.0  ???do we really need this seems to work without it?
    #copyrightyear=2015+  # move to ig.xml
    #license=CC0-1.0  # move to ig.xml
    #version=0.0.0  # move to ig.xml
    #ballotstatus=CI Build  # move to ig.xml
    #fhirspec=http://build.fhir.org/ # not needed
    #excludexml=Yes  # move to ig.xml
    #excludejson=No  # move to ig.xml
    #excludettl=Yes  # move to ig.xml
    ~~~

2.  _config.yml

   - add parameters from ig resource or let data file do this?
   - need to see whether parameter populate the data files or not
     - assume not and populate this as well
     - may need to update template accordingly depending if is site or site.data...

3. config.json *** this should be static based on set of templates

4.  package.json  - this is needed
   - what does it do:

     Package manifest
     A package manifest is a json file called 'package.json'. It conforms to the npm package.json format, but contains only a subset of properties. Other properties are allowed, but should be ignored by a FHIR package consumer.

   - it is not the same as the ig package but is the *template* package manifest
      - see Zulip chat.

   - https://wiki.hl7.org/FHIR_IG_publisher_templates
     ~~~
     {
       "name": "[package-id]",
       "version": "[ver]",
       "type": "fhir.template",
       "license": "[license]",
       "description": "[description]",
       "author": "[url]",
       "canonical" : "[canonical]"
     }
     ~~~
     - [package-id] must be chosen in accordance with the FHIR package naming convention
     - [ver] is under manual control of the author. Use semver. You will have to update the version to get IG publisher to pick up new versions
     - [license] - license of author's choice. Use CC0-1.0 for HL7 published templates
     - [description] - whatever
     - [url] - project website (e.g. contact details)
     - [canonical] - For IGs authored in GitHub, the GitHub repository URL.

      for this set of templates is...
        ~~~
        {
          "name": "healthedata.fhir.template",
          "version": "0.0.0",
          "type": "fhir.template",
          "license": "CC0-1.0",
          "description": "Health eData Inc FHIR Test Template",
          "author": "mailto::healthedatainc.com",
          "canonical": "http://www.fhir.org/guides/test4"
        }
        ~~~

5. ImplementationGuide (ig.xml) resource

   - enter all config parameters in ig resource

    - IG Parameters:
      ~~~
      logging:
      - init
      - progess
      - tx
      - generate
      - html
      generate:
      - example-narratives
      - genExamples
      path_resources: []
      path_liquid: []
      path_html: []
      path_md: []
      path_pages: []
      path_qa: []
      path_tx_cache: []
      path_output: []
      path_temp: []
      path_history: []
      path_expansion_params: []
      path_suppressed_warnings: []
      autoload_resources: false
      codesystem_property: []
      html_exempt: []
      extension_domain: []
      active_tables: false
      ig_expansion_parameters: []
      special_url: []
      template_openapi: null
      template_html: null
      template_md: null
      apply_contact: false
      apply_copyright: false
      apply_context: false
      apply_jurisdiction: false
      apply_license: false
      apply_publisher: false
      apply_version: false
      validation:
      - check-must-support
      - allow-any-extensions
      - check-aggregation
      - no-broken-links
      - show-reference-messages
      copyrightyear: 2015+
      releaselabel: CI Build
      excludexml: 'Yes'
      excludejson: 'No'
      excludettl: 'Yes'
      ~~~

      - add my parameters in here from _config.yml too:

        ~~~
        exclude:
        - templates
        - README.md
        title: IG-Template2
        copyrightyear: "2019" # copyright date for footer
        historypath: "#" # complete path to IG history file use "history" for an example of what this page would look like
        changelink: https://github.com/Healthedata1/IG-Template2/issues #http://hl7.org/fhir-issues  # for hl7 guides
        summaries: false #true if want custom profile summaries in summary tab
        diff2: false # true if want to show intermediate differentials - probably never use this.
        build: ci  # choice of ci|ballot|commentballot|version
        ballot:    #STU version of IG ( if needed for publishing HL7 guides)
        hl7_version:  # not sure what this is for
        hl7_ig: #  'true'  if HL7 ig
        showXML: true  #'true' if want xml tab'
        showTTL: true  #'true' if want ttl tab'
        showMappings: false  # 'true' if want to display mappings tab'
        showDefs: false  # 'true' if want to display Definitions tab'
        showExamples: false  # 'true' if want to display Examples tab -currently no template for it'
        showPsuedoJson: true # 'true' if want to display Psuedo JSON profile view'
        showPsuedoXML: true # 'true' if want to display Psuedo JSON profile view'
        showIntro:  # 'true' if want to display Custom Introduction in profile view'
        showQuickStart:  # 'true' if want to display QuickStarts in profile view'
        showDevView: # 'true' if only want to display summary view in profile view'
        default_profile_view: 1  # choice of 0|1|2|3 for summary|differential|full|all views in profile
        ~~~

   - build ig.xml via script using as input either:
      1. spreadsheet
      2. YAML

   - for narrative use YAML code block

## ig package manifest:

~~~
{
 "name": "hl7.fhir.us.acme",
 "version" : "0.1.0",
 "canonical" : "http://hl7.org/fhir/us/acme",
 "url" : "http://hl7.org/fhir/us/acme/Draft1",
 "title" : "ACME project IG",
 "description": "Describes how the ACME project uses FHIR for it's primary API",
 "dependencies": {
    "hl7.fhir.core": "3.0.0",
    "hl7.fhir.us.core": "1.1.0"
 },
 "keywords": [
   "us",
   "United States",
   "ACME"
 ],
 "author": "hl7",
 "maintainers": [
   {
     "name": "US Steering Committee",
     "email": "ussc@lists.hl7.com"
   }
 ],
 "license": "CC0-1.0"
}
~~~

Package Manifest properties for IGs:  
- name = ImplementationGuide.packageId
- version = ImplementationGuide.version - note: Semver SHALL be used for packages published by HL7 or the FHIR Foundation
- canonical = ImplementationGuide.url - required for IGs. This matches the name, and is constant through the life cycle of the IG
- url = ImplementationGuide.manifest.rendering - required for IGs
- title = ImplementationGuide.title
- description = ImplementationGuide.description
- dependencies = from ImplementationGuide.dependsOn
- author = ImplementationGuide.publisher
- maintainers = ImplementationGuide.contacts
- license = ImplementationGuide.license - mandatory for packages published by HL7 or the FHIR Foundation

see https://wiki.hl7.org/FHIR_IG_publisher_templates

## TODOS
1. create IG resource tooling
1. autoload_resources  - test this native functionality does it load the pages test pending
>If true, scan the locations in which resources might be found (above) looking for resources, and auto-loading them. Else, only load what is in the IG.

**It seems to work well with resources!!!**  

**!!! need spreadsheet extensions if use them**

**weird groupings generated as well?  keep base**

1. load templates from git hub
1. autoload_pages - test if pages load natively from directory that mimics the menu - no relative links get messed up.
1. autoload resource into pages - file name based - tested and working well but doesn't become part of the data files so ig is incomplete.
    - need to add the spreadsheet extension for all spreadsheets though - by hand or by inspecting the directory
    - keep the base group as default`
    - doesn't autoload the pages but has extensions?
Generate IG resources and pages before run
    - hand update ( YML template/Spreadsheets )
    - run script to update ig resource and pages like now.
      - have a default page layout like now
      - source - directly from directory as do now.
      - alternatatively from package.json after run the first time after autoload ?
      - ant-script
1. check if html works too. - it does indeed and fixed toc-for-pages to work in the layout
1. check out all parameters or extra Parameters -  todo error on qa
1. bash should error if no front matter in pages - todo
1. menu should have fixed and variable parts. - done see below
   -  use yaml file to define menu. variable parts of it?
1. Test with various IGs
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

*NOTE can't overwrite _data files in source. need create separate file and use control logic in templates...*

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
│   ├── temp  ** everything that gos into building the static web pages ends up
|   |   |          here all nice a pretty like thanks to the ig-pub **
│   │   ├── _data
│   │   ├── _includes
│   │   ├── fhir.css
│   │   └── link.svg
│   └── txCache
├── ig.ini  **** 1. dynamically updated from bash and the first place the
|                 ig-pub looks to for where to grab the template ****
├── ig.ini.bak  **** little bash feature to save the last ini file
├── my_framework  ****  This is the static "templated folder and where
|   |            all the magic happens from a templating standpoint****
│   ├── config.json 3. *** this should be static based on templates ***
│   ├── content
│   │   ├── *** 2._config.yml add parameters from ig resource or
|   |   |        let data file do this?  ***
│   │   └── _data
│   │       └── *** 5. navigation.yml - defines default top bar menu using YML
|   |               can overide with custom menue ****
│   ├── package *** 4. package.json is template specific and static****
│   └── templates
├── publish.sh  ** bash script for starting off the build - lots of parameters
|                  to optimize your exerience **
├── source  - *** this is where all the authoring and editing is done ***
│   ├── examples
│   ├── history
│   ├── html_pages ** a file for liquid testing only in my test IG
│   ├── pages
│   └── resources  **** 5. ig resource which will treat like the
|                      grandaddy config file ****
└── template **** this folder is reloaded with each and every build from the nominated template in ig.ini ****

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
     - or remove and the ImplementationGuide resources directly

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

This resource is essentially a big ole configuration file for generating an ig. Hence using a format like yaml to represent it and enter the data is natural fit ( see example below).  Will also provide a spreadsheet version for entering the data as well.

Enter all config parameters in ig resource either manually or with aid of tooling to input data from YAML files, spreadsheets and/or scraping directories.

  - There will be a default ig.xml (shown below) that should get you going with minimal data entry.

  ig resource builder

  inputs:
  YAML, spreadsheets,

  Need default template with full set of parameters

Use FHIR R5 Model in Python... _ make sure is up to date otherwise use a dictionary!!!

>how to populate _config.yml file  ??
>  need io in ANT ughh.
>  look at how lloyd is doing it or us js hook to JAva...:-(
>
>http://ant.apache.org/manual/Types/filterchain.html#headfilter  - read file
>
>  The echo task in ANT is able to write to files
>  <echo file="output.txt" append="true">
>     abc=${abc}
>  </echo>
>
>http://ant.apache.org/manual/Tasks/echo.html - write file
>
>  ...or... just write a new one each time
>

  ...or... just use the ig.json as a data file or strip out the meta and or text and convert to yaml and get rid of _config.yml. So all the site variable are now available out of the box... :-)

  to get parameter for list of name value pairs using liquid

e.g.:   
  code: path-resource  
  value: source/examples
~~~
{% raw %}{% assign param = site.data.ig.definition.parameter \| where: "code", "path-resource" | first %}{{ param.value }}{% endraw %}
~~~

  - build ig.xml via script using as input either:
     1. spreadsheet
     2. YAML  
  - data consists of:
       - meta data
         - manually entered
       - dependencies data
         - manually entered
       - conformance resources
         - manually entered or scraped from a directory
       - non-conformance  in other words examples
         - manually entered or scraped from a directory
       - pages
         - manually entered or scraped from a directory
       - IG Parameters:
          - manually entered

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

   - for narrative use YAML code block

### Exampe ImplementationGuide in YAML format:
~~~
resourceType: ImplementationGuide
id: healthedatainc.ig-template4-0.0.0
text:
  status: generated
  div: '<div xmlns="http://www.w3.org/1999/xhtml"><h2>IGTest3</h2><p>The official
    URL for this implementation guide is: </p><pre>http://www.fhir.org/guides/test4/ImplementationGuide/healthedatainc.ig-template4-0.0.0</pre></div>'
extension:
- url: http://hl7.org/fhir/StructureDefinition/igpublisher-spreadsheet
  valueUri: patient-on-usprofile-spreadsheet.xml
- url: http://hl7.org/fhir/StructureDefinition/igpublisher-spreadsheet
  valueUri: template-profile-spreadsheet.xml
url: http://www.fhir.org/guides/test4/ImplementationGuide/healthedatainc.ig-template4-0.0.0
version: 0.0.0
name: IGTest3
title: IG Test3
status: draft
date: '2020-01-21T16:34:14-08:00'
publisher: Health eData Inc
contact:
- telecom:
  - system: email
    value: mailto:ehaas@healthedatainc.com
- telecom:
  - system: url
    value: http://foobar.com
copyright: Used by permission of Health eData Inc, all rights reserved Creative Commons
  License
packageId: healthedatainc.ig-template4
license: CC0-1.0
fhirVersion:
- 4.0.1
dependsOn:
- id: uscore
  uri: http://hl7.org/fhir/us/core
  packageId: hl7.fhir.us.core
  version: 3.1.0
- id: qicore
  uri: http://hl7.org/fhir/us/qicore
  packageId: hl7.fhir.us.qicore
  version: current
definition:
  grouping:
  - name: base
  - id: template-profile-spreadsheet.xml
    name: Template-basic
  resource:
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: Basic
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: Basic-diet.html
    reference:
      reference: Basic/diet
    exampleBoolean: true
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: Patient
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: Patient-example.html
    reference:
      reference: Patient/example
    exampleBoolean: true
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: Patient
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: Patient-example2.html
    reference:
      reference: Patient/example2
    exampleBoolean: true
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: StructureDefinition:extension
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: StructureDefinition-extension-complex.html
    reference:
      reference: StructureDefinition/extension-complex
    name: Complex Extension
    description: an example of a complex extension.
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: StructureDefinition:extension
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: StructureDefinition-extension-blah.html
    reference:
      reference: StructureDefinition/extension-blah
    name: Simple Extension
    description: an example of a simple extension.
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: OperationDefinition
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: OperationDefinition-opdef-test.html
    reference:
      reference: OperationDefinition/opdef-test
    description: Limited implementation of the Populate Questionnaire implementation
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: StructureDefinition:complex-type
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: StructureDefinition-ifr.html
    reference:
      reference: StructureDefinition/ifr
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: ValueSet
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: ValueSet-bar-codes.html
    reference:
      reference: ValueSet/bar-codes
    name: Bar Value Set
    description: A bunch of example codes
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: CapabilityStatement
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: CapabilityStatement-server.html
    reference:
      reference: CapabilityStatement/server
    description: 'This resource defines the expected capabilities '
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: CodeSystem
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: CodeSystem-blah-codes.html
    reference:
      reference: CodeSystem/blah-codes
    description: A bunch of example codes
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: CapabilityStatement
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: CapabilityStatement-client.html
    reference:
      reference: CapabilityStatement/client
    description: 'This resource defines the expected capabilities '
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: StructureDefinition:resource
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: StructureDefinition-template-profile-on-profile.html
    reference:
      reference: StructureDefinition/template-profile-on-profile
    name: Template Profile on Profile
    description: Template-Profile-on-Profile
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: ValueSet
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: ValueSet-foo-codes.html
    reference:
      reference: ValueSet/foo-codes
    name: Foo Value Set
    description: A bunch of example codes
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: StructureDefinition:resource
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: StructureDefinition-template-basic.html
    reference:
      reference: StructureDefinition/template-basic
    name: Health eData Template Profile
    description: This is a simple example Template
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: ValueSet
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: ValueSet-blah-codes.html
    reference:
      reference: ValueSet/blah-codes
    description: A bunch of example codes
    exampleBoolean: false
  - extension:
    - url: http://hl7.org/fhir/tools/StructureDefinition/resource-information
      valueString: StructureDefinition:extension
    - url: http://hl7.org/fhir/StructureDefinition/implementationguide-page
      valueUri: StructureDefinition-extension-blah2.html
    reference:
      reference: StructureDefinition/extension-blah2
    name: blah2
    description: an example of a simple extension.
    groupingId: template-profile-spreadsheet.xml
  page:
    nameUrl: index.html
    title: Home
    generation: markdown
    page:
    - nameUrl: guidance.html
      title: General Guidance
      generation: markdown
    - nameUrl: profiles.html
      title: Profiles and Extensions
      generation: markdown
      page:
      - nameUrl: StructureDefinition-ifr.html
        title: StructureDefinition Ifr
        generation: generated
      - nameUrl: StructureDefinition-template-profile-on-profile.html
        title: StructureDefinition Template Profile On Profile
        generation: generated
      - nameUrl: StructureDefinition-template-basic.html
        title: StructureDefinition Template Basic
        generation: generated
      - nameUrl: StructureDefinition-extension-complex.html
        title: StructureDefinition Extension Complex
        generation: generated
      - nameUrl: StructureDefinition-extension-blah.html
        title: StructureDefinition Extension Blah
        generation: generated
    - nameUrl: operations.html
      title: Operations
      generation: markdown
      page:
      - nameUrl: OperationDefinition-opdef-test.html
        title: OperationDefinition Opdef Test
        generation: generated
    - nameUrl: terminology.html
      title: Terminology
      generation: markdown
      page:
      - nameUrl: ValueSet-bar-codes.html
        title: ValueSet Bar Codes
        generation: generated
      - nameUrl: ValueSet-foo-codes.html
        title: ValueSet Foo Codes
        generation: generated
      - nameUrl: ValueSet-blah-codes.html
        title: ValueSet Blah Codes
        generation: generated
      - nameUrl: CodeSystem-blah-codes.html
        title: CodeSystem Blah Codes
        generation: generated
    - nameUrl: searchparameters.html
      title: Search Parameters
      generation: markdown
    - nameUrl: capstatements.html
      title: Capability Statements
      generation: markdown
      page:
      - nameUrl: CapabilityStatement-server.html
        title: CapabilityStatement Server
        generation: generated
      - nameUrl: CapabilityStatement-client.html
        title: CapabilityStatement Client
        generation: generated
    - nameUrl: security.html
      title: Security
      generation: markdown
    - nameUrl: downloads.html
      title: Downloads
      generation: markdown
    - nameUrl: all-examples.html
      title: All Examples
      generation: markdown
    - nameUrl: toc.html
      title: Table of Contents
      generation: html
  parameter:
  - code: path-resource
    value: source/examples
  - code: path-resource
    value: source/resources
  - code: path-pages
    value: source/pages
  - code: path-pages
    value: template/content/pages
  - code: path-qa
    value: generated_output/qa
  - code: path-temp
    value: generated_output/temp
  - code: path-tx-cache
    value: generated_output/txCache
  - code: path-output
    value: docs
  - code: path-history
    value: http://www.fhir.org/guides/test4/history.html
~~~

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

## Other FYI information (from confluence):
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

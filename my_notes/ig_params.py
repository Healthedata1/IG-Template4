ig_params = dict(  # note:change to '_' to '-' in serialized format
    logging = ['init','progess','tx','generate','html'], # default = none
    generate = ['example-narratives','genExamples'], # default = none
    path_resources = [], #your paths here, default = resources
    path_liquid = [], #your paths here, default = resources
    path_html = [], #your paths here, default = resources
    path_md = [], #your paths here, default = resources
    path_pages = [], #your paths here, default = resources
    path_qa = [], #your paths here, default = resources
    path_tx_cache = [], #your paths here, default = resources
    path_output = [], #your paths here, default = resources
    path_temp = [], #your paths here, default = resources
    path_history = [], #your paths here, default = resources
    path_expansion_params = [], #your paths here, default = resources
    path_suppressed_warnings = [], #your paths here, default = resources
    autoload_resources = False, # default= False
    codesystem_property = [], # your urls here, default = none
    html_exempt = [], # your masks that identifies specific HTML files exempt from having header / footer etc. here, default = name`
    extension_domain = [],  # your urls here, default = none
    active_tables = False, # default = False
    ig_expansion_parameters = [], # broken
    special_url = [], # your urls here, default = none
    template_openapi = None, # your path here default = none
    template_html = None, # your path here, default = none
    template_md = None, # your path here, default = none
    apply_contact = False, # default = False
    apply_copyright = False, # default = False
    apply_context = False, # default = False
    apply_jurisdiction = False, # default = False
    apply_license = False, # default = False
    apply_publisher = False, # default = False
    apply_version = False, # default = False
    validation = ['check-must-support','allow-any-extensions','check-aggregation', 'no-broken-links',
    'show-reference-messages'], #default = None
    copyrightyear ='2015+', # from ig.ini
    releaselabel='CI Build', # from ig.ini
    excludexml='Yes',# from ig.ini
    excludejson='No',# from ig.ini
    excludettl='Yes',# from ig.ini
)

#sorted
new_dict ={k:v for k,v in sorted(ig_params.items())}
from pprint import pprint
pprint(new_dict)

'''
{'active_tables': False,
 'apply_contact': False,
 'apply_context': False,
 'apply_copyright': False,
 'apply_jurisdiction': False,
 'apply_license': False,
 'apply_publisher': False,
 'apply_version': False,
 'autoload_resources': False,
 'codesystem_property': [],
 'default': None,
 'extension_domain': [],
 'generate': ['example-narratives', 'genExamples'],
 'html_exempt': [],
 'ig_expansion_parameters': [],
 'logging': ['init', 'progess', 'tx', 'generate', 'html'],
 'path_expansion_params': [],
 'path_history': [],
 'path_html': [],
 'path_liquid': [],
 'path_md': [],
 'path_output': [],
 'path_pages': [],
 'path_qa': [],
 'path_resources': [],
 'path_suppressed_warnings': [],
 'path_temp': [],
 'path_tx_cache': [],
 'special_url': [],
 'template_html': None,
 'template_md': None,
 'template_openapi': None,
 'validation': ['check-must-support',
                'allow-any-extensions',
                'check-aggregation',
                'no-broken-links',
                'show-reference-messages']}
'''

# convert to yaml

from yaml import load as y_load, dump as y_dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

yig_params = y_dump(ig_params, Dumper=Dumper, sort_keys=False)
print(yig_params)

ig_json = {
  "resourceType": "ImplementationGuide",
  "id": "healthedatainc.ig-template4",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><h2>IGTest4</h2><p>The official URL for this implementation guide is: </p><pre>http://www.fhir.org/guides/test4/ImplementationGuide/healthedatainc.ig-template4</pre></div>"
  },
  "extension": [
    {
      "url": "http://hl7.org/fhir/StructureDefinition/igpublisher-spreadsheet",
      "valueUri": "patient-on-usprofile-spreadsheet.xml"
    },
    {
      "url": "http://hl7.org/fhir/StructureDefinition/igpublisher-spreadsheet",
      "valueUri": "template-profile-spreadsheet.xml"
    }
  ],
  "url": "http://www.fhir.org/guides/test4/ImplementationGuide/healthedatainc.ig-template4",
  "version": "0.0.0",
  "name": "IGTest4",
  "title": "IG Test4",
  "status": "draft",
  "date": "2020-01-23T16:30:49-08:00",
  "publisher": "Health eData Inc",
  "contact": [
    {
      "telecom": [
        {
          "system": "email",
          "value": "mailto:ehaas@healthedatainc.com"
        }
      ]
    },
    {
      "telecom": [
        {
          "system": "url",
          "value": "http://foobar.com"
        }
      ]
    }
  ],
  "copyright": "Used by permission of Health eData Inc, all rights reserved Creative Commons License",
  "packageId": "healthedatainc.ig-template4",
  "license": "CC0-1.0",
  "fhirVersion": [
    "4.0.1"
  ],
  "dependsOn": [
    {
      "id": "uscore",
      "uri": "http://hl7.org/fhir/us/core/ImplementationGuide/hl7.fhir.us.core",
      "packageId": "hl7.fhir.us.core",
      "version": "3.1.0"
    },
    {
      "id": "qicore",
      "uri": "http://hl7.org/fhir/us/qicore/ImplementationGuide/hl7.fhir.us.qicore",
      "packageId": "hl7.fhir.us.qicore",
      "version": "current"
    }
  ],
  "definition": {
    "grouping": [
      {
        "name": "base"
      },
      {
        "id": "template-profile-spreadsheet.xml",
        "name": "Template-basic"
      }
    ],
    "resource": [
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "Basic"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "Basic-diet.html"
          }
        ],
        "reference": {
          "reference": "Basic/diet"
        },
        "exampleBoolean": True
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "Patient"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "Patient-example.html"
          }
        ],
        "reference": {
          "reference": "Patient/example"
        },
        "exampleBoolean": True
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "Patient"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "Patient-example2.html"
          }
        ],
        "reference": {
          "reference": "Patient/example2"
        },
        "exampleBoolean": True
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "StructureDefinition:extension"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "StructureDefinition-extension-complex.html"
          }
        ],
        "reference": {
          "reference": "StructureDefinition/extension-complex"
        },
        "name": "Complex Extension",
        "description": "an example of a complex extension.",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "StructureDefinition:extension"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "StructureDefinition-extension-blah.html"
          }
        ],
        "reference": {
          "reference": "StructureDefinition/extension-blah"
        },
        "name": "Simple Extension",
        "description": "an example of a simple extension.",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "OperationDefinition"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "OperationDefinition-opdef-test.html"
          }
        ],
        "reference": {
          "reference": "OperationDefinition/opdef-test"
        },
        "description": "Limited implementation of the Populate Questionnaire implementation",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "StructureDefinition:complex-type"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "StructureDefinition-ifr.html"
          }
        ],
        "reference": {
          "reference": "StructureDefinition/ifr"
        },
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "ValueSet"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "ValueSet-bar-codes.html"
          }
        ],
        "reference": {
          "reference": "ValueSet/bar-codes"
        },
        "name": "Bar Value Set",
        "description": "A bunch of example codes",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "CapabilityStatement"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "CapabilityStatement-server.html"
          }
        ],
        "reference": {
          "reference": "CapabilityStatement/server"
        },
        "description": "This resource defines the expected capabilities ",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "CodeSystem"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "CodeSystem-blah-codes.html"
          }
        ],
        "reference": {
          "reference": "CodeSystem/blah-codes"
        },
        "description": "A bunch of example codes",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "CapabilityStatement"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "CapabilityStatement-client.html"
          }
        ],
        "reference": {
          "reference": "CapabilityStatement/client"
        },
        "description": "This resource defines the expected capabilities ",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "StructureDefinition:resource"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "StructureDefinition-template-profile-on-profile.html"
          }
        ],
        "reference": {
          "reference": "StructureDefinition/template-profile-on-profile"
        },
        "name": "Template Profile on Profile",
        "description": "Template-Profile-on-Profile",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "ValueSet"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "ValueSet-foo-codes.html"
          }
        ],
        "reference": {
          "reference": "ValueSet/foo-codes"
        },
        "name": "Foo Value Set",
        "description": "A bunch of example codes",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "StructureDefinition:resource"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "StructureDefinition-template-basic.html"
          }
        ],
        "reference": {
          "reference": "StructureDefinition/template-basic"
        },
        "name": "Health eData Template Profile",
        "description": "This is a simple example Template",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "ValueSet"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "ValueSet-blah-codes.html"
          }
        ],
        "reference": {
          "reference": "ValueSet/blah-codes"
        },
        "description": "A bunch of example codes",
        "exampleBoolean": False
      },
      {
        "extension": [
          {
            "url": "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString": "StructureDefinition:extension"
          },
          {
            "url": "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
            "valueUri": "StructureDefinition-extension-blah2.html"
          }
        ],
        "reference": {
          "reference": "StructureDefinition/extension-blah2"
        },
        "name": "blah2",
        "description": "an example of a simple extension.",
        "groupingId": "template-profile-spreadsheet.xml"
      }
    ],
    "page": {
      "nameUrl": "index.html",
      "title": "Home",
      "generation": "markdown",
      "page": [
        {
          "nameUrl": "guidance.html",
          "title": "General Guidance",
          "generation": "markdown"
        },
        {
          "nameUrl": "more-guidance.html",
          "title": "More General Guidance",
          "generation": "html"
        },
        {
          "nameUrl": "profiles.html",
          "title": "Profiles and Extensions",
          "generation": "markdown",
          "page": [
            {
              "nameUrl": "StructureDefinition-ifr.html",
              "title": "StructureDefinition Ifr",
              "generation": "generated"
            },
            {
              "nameUrl": "StructureDefinition-template-profile-on-profile.html",
              "title": "StructureDefinition Template Profile On Profile",
              "generation": "generated"
            },
            {
              "nameUrl": "StructureDefinition-template-basic.html",
              "title": "StructureDefinition Template Basic",
              "generation": "generated"
            },
            {
              "nameUrl": "StructureDefinition-extension-complex.html",
              "title": "StructureDefinition Extension Complex",
              "generation": "generated"
            },
            {
              "nameUrl": "StructureDefinition-extension-blah.html",
              "title": "StructureDefinition Extension Blah",
              "generation": "generated"
            }
          ]
        },
        {
          "nameUrl": "operations.html",
          "title": "Operations",
          "generation": "markdown",
          "page": [
            {
              "nameUrl": "OperationDefinition-opdef-test.html",
              "title": "OperationDefinition Opdef Test",
              "generation": "generated"
            }
          ]
        },
        {
          "nameUrl": "terminology.html",
          "title": "Terminology",
          "generation": "markdown",
          "page": [
            {
              "nameUrl": "ValueSet-bar-codes.html",
              "title": "ValueSet Bar Codes",
              "generation": "generated"
            },
            {
              "nameUrl": "ValueSet-foo-codes.html",
              "title": "ValueSet Foo Codes",
              "generation": "generated"
            },
            {
              "nameUrl": "ValueSet-blah-codes.html",
              "title": "ValueSet Blah Codes",
              "generation": "generated"
            },
            {
              "nameUrl": "CodeSystem-blah-codes.html",
              "title": "CodeSystem Blah Codes",
              "generation": "generated"
            }
          ]
        },
        {
          "nameUrl": "searchparameters.html",
          "title": "Search Parameters",
          "generation": "markdown"
        },
        {
          "nameUrl": "capstatements.html",
          "title": "Capability Statements",
          "generation": "markdown",
          "page": [
            {
              "nameUrl": "CapabilityStatement-server.html",
              "title": "CapabilityStatement Server",
              "generation": "generated"
            },
            {
              "nameUrl": "CapabilityStatement-client.html",
              "title": "CapabilityStatement Client",
              "generation": "generated"
            }
          ]
        },
        {
          "nameUrl": "security.html",
          "title": "Security",
          "generation": "markdown"
        },
        {
          "nameUrl": "downloads.html",
          "title": "Downloads",
          "generation": "markdown"
        },
        {
          "nameUrl": "all-examples.html",
          "title": "All Examples",
          "generation": "markdown"
        },
        {
          "nameUrl": "toc.html",
          "title": "Table of Contents",
          "generation": "html"
        }
      ]
    },
    "parameter": [
      {
        "code": "path-resource",
        "value": "source/examples"
      },
      {
        "code": "path-resource",
        "value": "source/resources"
      },
      {
        "code": "path-pages",
        "value": "source/pages"
      },
      {
        "code": "path-pages",
        "value": "template/content/pages"
      },
      {
        "code": "path-qa",
        "value": "generated_output/qa"
      },
      {
        "code": "path-temp",
        "value": "generated_output/temp"
      },
      {
        "code": "path-tx-cache",
        "value": "generated_output/txCache"
      },
      {
        "code": "path-output",
        "value": "docs"
      },
      {
        "code": "path-history",
        "value": "http://www.fhir.org/guides/test4/history.html"
      },
      {
        "code": "foo",
        "value": "bar"
      }
    ]
  }
}


ig_yml = y_dump(ig_json, Dumper=Dumper, sort_keys=False)
print(ig_yml)

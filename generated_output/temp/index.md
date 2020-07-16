---
title: Home Page
layout: default
toc: True
---

### Cat Facts (To Show How the Text Wraps around the Contents Block) {#cat-facts}

 The domestic cat[1][5] (Latin: Felis catus) is a small, typically furry, carnivorous mammal. They are often called house cats when kept as indoor pets or simply cats when there is no need to distinguish them from other felids and felines.[6] Cats are often valued by humans for companionship and for their ability to hunt vermin. There are more than 70 cat breeds, though different associations proclaim different numbers according to their standards.

Cats are similar in anatomy to the other felids, with a strong flexible body, quick reflexes, sharp retractable claws, and teeth adapted to killing small prey. Cat senses fit a crepuscular and predatory ecological niche. Cats can hear sounds too faint or too high in frequency for human ears, such as those made by mice and other small animals. They can see in near darkness. Like most other mammals, cats have poorer color vision and a better sense of smell than humans. Cats, despite being solitary hunters, are a social species and cat communication includes the use of a variety of vocalizations (mewing, purring, trilling, hissing, growling, and grunting), as well as cat pheromones and types of cat-specific body language.[7]

Cats have a high breeding rate.[8] Under controlled breeding, they can be bred and shown as registered pedigree pets, a hobby known as cat fancy. Failure to control the breeding of pet cats by neutering, as well as the abandonment of former household pets, has resulted in large numbers of feral cats worldwide, requiring population control.[9] In certain areas outside cats' native range, this has contributed, along with habitat destruction and other factors, to the extinction of many bird species. Cats have been known to extirpate a bird species within specific regions and may have contributed to the extinction of isolated island populations.[10] Cats are thought to be primarily responsible for the extinction of 33 species of birds, and the presence of feral and free-ranging cats makes some otherwise suitable locations unsuitable for attempted species reintroduction.[11]

Since cats were venerated in ancient Egypt, they were commonly believed to have been domesticated there,[12] but there may have been instances of domestication as early as the Neolithic from around 9,500 years ago (7,500 BC).[13] A genetic study in 2007 concluded that domestic cats are descended from Near Eastern wildcats, having diverged around 8,000 BC in the Middle East.[12][14] A 2016 study found that leopard cats were undergoing domestication independently in China around 5,500 BC, though this line of partially domesticated cats leaves no trace in the domesticated populations of today.[15][16]

As of a 2007 study, cats are the second most popular pet in the US by number of pets owned, behind freshwater fish.[17] In a 2010 study they were ranked the third most popular pet in the UK, after fish and dogs, with around 8 million being owned.[18]

Figure 1 is a picture of a cat to show how to insert an image using markdown.

{% include img.html img="cat.jpg" caption="Figure 1: Meow" %}



### Jekyll Site Variables

Now can use variables directly based on the ImplementationGuide Resource since the resource is represented in Jekyll as a [Jekyll Data File](https://jekyllrb.com/docs/datafiles/).  The are the (old) site variables defined [here](http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation# Jekyll).
We can replace them directly with the data from the ImplementationGuide Resource:

**The following table summarizes the current and new way to access variables using {% raw %} {{liquid object syntax}} {% endraw %}.**

<div class="row">
<div class="col-sm-6" markdown="1" style="background-color: Lightcyan;">

**Currently accessed via data.fhir data file which is derived from both the configuration file ('ig.json') and the ImplementationGuide Resource**

- IG Package ID (defined in ig.json config file)- {% raw %}{{site.data.fhir.packageId}}{% endraw %} = {{site.data.fhir.packageId}}

-  IG Business version specification (defined in ig.json)- {% raw %}{{site.data.fhir.ig.version}} {% endraw %} = {{site.data.fhir.ig.version}}

- IG status (defined in ig.xml)- {% raw %}{{site.data.fhir.ig.status}} {% endraw %} = {{site.data.fhir.ig.status}}

- Whether is experimental IG (defined in ig.xml) - {% raw %}{{site.data.fhir.ig.experimental}} {% endraw %} = {{site.data.fhir.ig.experimental}}

- IG Publisher name (defined in ig.xml) - {% raw %}{{site.data.fhir.ig.publisher}} {% endraw %} = {{site.data.fhir.ig.publisher}}

- dependency url - e.g. "uscore" : Base url of a dependency implementation Guide (defined in ig.json) -  {% raw %} {{site.data.fhir.uscore}} {% endraw %}= {{site.data.fhir.uscore}}

     - link to {{site.data.fhir.uscore}} in markdown is  {% raw %}\[{{site.data.fhir.uscore}}\]({{site.data.fhir.uscore}}){% endraw %} = [{{site.data.fhir.uscore}}]({{site.data.fhir.uscore}})

     - current link to {{site.data.fhir.uscore}} home in markdown is  {% raw %}\[{{site.data.fhir.uscore}}index.html\]({{site.data.fhir.uscore}}index.html){% endraw %} = [{{site.data.fhir.uscore}}index.html]({{site.data.fhir.uscore}}index.html)


- ig Name : computer friendly name of the implementation Guide - used as human friendly name in STU3 (defined in ig.xml) -  {% raw %} {{site.data.fhir.ig.name}} {% endraw %}= {{site.data.fhir.ig.name}}

- ig Title : human friendly name of the implementation Guide - R4 and above (defined in ig.xml) -  {% raw %} {{site.data.fhir.ig.title}} {% endraw %}= {{site.data.fhir.ig.title}}

-  path : path to the main FHIR specification (defined in ig.json)-  {% raw %} {{site.data.fhir.path}} {% endraw %}= {{site.data.fhir.path}}

     - link to {{site.data.fhir.path}} in markdown is  {% raw %}\[{{site.data.fhir.path}}index.html\]({{site.data.fhir.path}}index.html){% endraw %} = [{{site.data.fhir.path}}index.html]({{site.data.fhir.path}}index.html)

-  canonical : canonical path to this specification (defined in ig.json)-  {% raw %} {{site.data.fhir.canonical}} {% endraw %} = {{site.data.fhir.canonical}}

    -  link to {{site.data.fhir.canonical}} in markdown is  {% raw %}\[{{site.data.fhir.canonical}}\]({{site.data.fhir.canonical}}){% endraw %} = [{{site.data.fhir.canonical}}]({{site.data.fhir.canonical}})

-  errorCount : number of errors in the build file (not including HTML validation errors) -  {% raw %} {{site.data.fhir.errorCount}} {% endraw %} = {{site.data.fhir.errorCount}}

-  version : version of FHIR -  {% raw %} {{site.data.fhir.version}} {% endraw %} = {{site.data.fhir.version}}

-  revision : revision of FHIR -  {% raw %} {{site.data.fhir.revision}} {% endraw %} = {{site.data.fhir.revision}}

-  versionFull : version-revision -  {% raw %} {{site.data.fhir.versionFull}} {% endraw %} = {{site.data.fhir.versionFull}}

-  totalFiles : total number of files found by the build -  {% raw %} {{site.data.fhir.totalFiles}} {% endraw %} = {{site.data.fhir.totalFiles}}

-  processedFiles : number of files genrated by the build -  {% raw %} {{site.data.fhir.processedFiles}} {% endraw %} = {{site.data.fhir.processedFiles}}

-  genDate : date of generation (so date stamps in the pages can match those in the conformance resources) -  {% raw %} {{site.data.fhir.genDate}} {% endraw %} = {{site.data.fhir.genDate}}

----

</div>
<div class="col-sm-6" markdown = "1" style="background-color: WhiteSmoke;">

**New Way accessed directly from the ImplementationGuide Resource which represented as the ig.fhir data file in the Jekyll build**

- IG Package ID - {% raw %}{{site.data.ig.packageId}}{% endraw %} = {{site.data.ig.packageId}}

-  IG Business version specification- {% raw %}{{site.data.ig.version}} {% endraw %} = {{site.data.ig.version}}

- IG status - {% raw %}{{site.dat.ig.status}} {% endraw %} = {{site.data.ig.status}}

- Whether is experimental IG - {% raw %}{{site.ig.experimental}} {% endraw %} = {{site.ig.experimental}}

- IG Publisher name  - {% raw %}{{site.data.ig.publisher}} {% endraw %} = {{site.data.ig.publisher}}

- dependency url - e.g. "uscore" : Base url of a dependency implementation Guide  -  {% raw %}{% assign var = site.data.ig.dependsOn \| where: "id", "uscore" %}{{ var[0].uri }}{% endraw %}= {% assign var = site.data.ig.dependsOn | where: "id", "uscore" %}{{ var[0].uri }}

     - link to {{ var[0].uri }} in markdown is  {% raw %}\[{{ var[0].uri }}\]({{ var[0].uri }}){% endraw %} = [{{ var[0].uri }}]({{ var[0].uri }})

     - current link to {{ var[0].uri }} home in markdown is  {% raw %}\[{{{ var[0].uri }}index.html\]({{ var[0].uri }}/index.html){% endraw %} = [{{ var[0].uri }}index.html]({{ var[0].uri }}/index.html)


- ig Name : computer friendly name of the implementation Guide(used as human friendly name STU3) -  {% raw %} {{site.data.ig.name}} {% endraw %}= {{site.data.ig.name}}

- ig Title : human friendly name of the implementation Guide - R4 and above  -  {% raw %} {{site.data.ig.title}} {% endraw %}= {{site.data.ig.title}}

-  *this is still the best way* path : path to the main FHIR specification-  {% raw %} {{site.data.fhir.path}} {% endraw %}= {{site.data.fhir.path}}

     - link to {{site.data.fhir.path}} in markdown is  {% raw %}\[{{site.data.fhir.path}}index.html\]({{site.data.fhir.path}}index.html){% endraw %} = [{{site.data.fhir.path}}index.html]({{site.data.fhir.path}}index.html)

-  *this is still the best way* canonical : canonical path to this specification -  {% raw %} {{site.data.fhir.canonical}} {% endraw %} = {{site.data.fhir.canonical}}

    -  link to {{site.data.fhir.canonical}} in markdown is  {% raw %}\[{{site.data.fhir.canonical}}\]({{site.data.fhir.canonical}}){% endraw %} = [{{site.data.fhir.canonical}}]({{site.data.fhir.canonical}})

-  *this is still the only way* errorCount : number of errors in the build file (not including HTML validation errors) -  {% raw %} {{site.data.fhir.errorCount}} {% endraw %} = {{site.data.fhir.errorCount}}

-  version : version of FHIR -  {% raw %} {{site.data.ig.fhirVersion}} {% endraw %} = {{site.data.ig.fhirVersion}}

-  *this is still the only way* revision : revision of FHIR -  {% raw %} {{site.data.fhir.revision}} {% endraw %} = {{site.data.fhir.revision}}

-  *this is still the only way* versionFull : version-revision -  {% raw %} {{site.data.fhir.versionFull}} {% endraw %} = {{site.data.fhir.versionFull}}

-  *this is still the only way* totalFiles : total number of files found by the build -  {% raw %} {{site.data.fhir.totalFiles}} {% endraw %} = {{site.data.fhir.totalFiles}}

-  *this is still the only way* processedFiles : number of files genrated by the build -  {% raw %} {{site.data.fhir.processedFiles}} {% endraw %} = {{site.data.fhir.processedFiles}}

-  *this is still the only way* genDate : date of generation (so date stamps in the pages can match those in the conformance resources) -  {% raw %} {{site.data.fhir.genDate}} {% endraw %} = {{site.data.fhir.genDate}}

---

</div>

</div>



### Introduction

blah blah blah

### More Stuff

and more stuff

#### And More Stuff

add link list to bottom of each page....
<!-- {% raw %}>{% include link-list.md %} {% endraw %}-->

{% include link-list.md %}
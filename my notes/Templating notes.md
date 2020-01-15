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

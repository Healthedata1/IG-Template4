n#!/bin/bash

#folder articles contains a lot of markdown files
files=./input/pagecontent/*

for f in $files;
do
    #filename
    echo "${f##*/}"
    #replace frontmatter title attribute to "title"
    sed -i -r '1{/^---$/!q;};1,/^---$/d' $f
    #...
done

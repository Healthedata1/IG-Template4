#!/bin/bash
# exit when any command fails
set -e
echo '================================='
echo 'revert to upstream - THIS WILL OVERWRITE YOUR LOCAL CHANGES'
echo '================================='
git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master --force

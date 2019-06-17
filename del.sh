#!/bin/bash 
git filter-branch --force --index-filter  'git rm --cached -r --ignore-unmatch \
document/Spring in Action'  --prune-empty --tag-name-filter cat -- --all

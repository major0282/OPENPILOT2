#!/bin/sh

# Cleanup all remote branches except docs

git fetch --prune
git push --delete origin $(git branch -r | grep -v "origin/docs" | sed 's/origin\///')

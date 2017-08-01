#!/bin/bash
git pull origin master
python3 kindle2markdown.py
git add .
git commit -m 'generate new file'
git push origin master


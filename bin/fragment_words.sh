#!/bin/bash

cd `dirname $BASH_SOURCE`/..

rm -f results/words/* 
rm -f results/meta/*

python src/fragment_words.py tests/Mnatobi-009-cropped.png


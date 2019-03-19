#!/bin/bash
pdflatex prab.tex
bibtex prab.aux
bibtex prab.aux
bibtex prab.aux
pdflatex prab.tex


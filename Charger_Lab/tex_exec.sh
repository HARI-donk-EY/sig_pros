texfot pdflatex main.tex
texfot pdflatex main.tex
rm main.aux main.log main.out main.toc
rm main.fdb_latexmk main.fls
rm 'main.synctex(busy)'
figlet "DONE"
# evince main.pdf

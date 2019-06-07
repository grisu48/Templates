
default:	all

all:	Presentation.tex
	pdflatex -synctex=1 -interaction=nonstopmode Presentation.tex
	pdflatex -synctex=1 -interaction=nonstopmode Presentation.tex
	pdflatex -synctex=1 -interaction=nonstopmode Presentation.tex
	pdflatex -synctex=1 -interaction=nonstopmode Presentation.tex

clean:
	rm -f *.aux
	rm -f *.toc
	rm -f *.log
	rm -f *.bbl
	rm -f *.blg
	rm -f *.out
	rm -f *.bib~?
	rm -f *.nav
	rm -f *.snm
	rm -f *.synctex.gz


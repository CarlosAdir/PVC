all: compilar referencia compilar pdf

compilar:
	pdflatex main

referencia:
	bibtex main

pdf:
	evince main.pdf

clean:
	rm *.aux
	rm *.log
	rm *.blg
	rm *.bbl
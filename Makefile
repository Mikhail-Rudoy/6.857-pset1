LATEX=latex
DVIPS=dvips
PS2PDF=ps2pdf

INPUT=mrudoy_presbrey_qlong_pset1_problem3
OUTPUT=mrudoy_presbrey_qlong_pset1_problem3


all: dviclean $(OUTPUT).ps $(OUTPUT).pdf

$(OUTPUT).pdf: $(OUTPUT).ps
	$(PS2PDF) $(OUTPUT).ps > $(OUTPUT).pdf

$(OUTPUT).ps: $(INPUT).dvi
	$(DVIPS) -t letter -f $(INPUT).dvi > $(OUTPUT).ps

$(INPUT).dvi: $(INPUT).tex
	$(LATEX) $(INPUT).tex

clean:
	/bin/rm -f *.dvi *.aux *~ *.log *.lot *.lof *.toc *.blg *.bbl  *.ps
dviclean:
	/bin/rm -f *.dvi 

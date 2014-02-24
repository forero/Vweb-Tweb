LATEX = pdflatex
MAIN  = main

$(MAIN).pdf: 	$(MAIN).tex  
	$(LATEX) $(MAIN).tex 
	bibtex $(MAIN)
	$(LATEX) $(MAIN).tex 
	$(LATEX) $(MAIN).tex 


clean:
	rm -f $(MAIN).{aux,bbl,ps,pdf,dvi,blg,log,out}

view: 
	open $(MAIN).pdf &


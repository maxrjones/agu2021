.PHONY: clean
BLACK_FILES=$(PROJECT) *.py
BLACKDOC_OPTIONS=--line-length 79
DOCFORMATTER_FILES=$(PROJECT) *.py
DOCFORMATTER_OPTIONS=--recursive --pre-summary-newline --make-summary-multi-line --wrap-summaries 79 --wrap-descriptions 79

help:
	@echo "  clean        clean up built and generated files"
	@echo "  format       run black, blackdoc, docformatter and isort to automatically format the code"

format:
	isort *.py
	docformatter --in-place $(DOCFORMATTER_OPTIONS) $(DOCFORMATTER_FILES)
	black $(BLACK_FILES)
	blackdoc $(BLACKDOC_OPTIONS) $(BLACK_FILES)

clean:
	rm *.nc *.tif *.txt
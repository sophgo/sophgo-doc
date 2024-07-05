# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -t sg2000
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

PROJECT      = sg2000
DOC_TYPE     = trm
DOC_LANG     = cn
RELEASE      = 1.01
RELEASE_DATE = 2024-07-05
COPYRIGHT    = "2024 SOPHGO Co., Ltd"
AUTHOR       = Sophgo

PDF_FILENAME = $(PROJECT)_$(DOC_TYPE)_$(DOC_LANG).pdf

BUILD_CONFIG  = \
	CONFIG_PROJECT=$(PROJECT) \
	CONFIG_TYPE=$(DOC_TYPE) \
	CONFIG_LANG=$(DOC_LANG) \
	CONFIG_COPYRIGHT=$(COPYRIGHT) \
	CONFIG_AUTHOR=$(AUTHOR) \
	CONFIG_RELEASE=$(RELEASE) \
	CONFIG_RELEASEDATE=$(RELEASE_DATE)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(BUILD_CONFIG) $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

pdf: latexpdf
	@mv $(BUILDDIR)/latex/$(PROJECT).pdf $(BUILDDIR)/"${PDF_FILENAME}"

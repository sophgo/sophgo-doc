# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

project = os.getenv('CONFIG_PROJECT', 'sgXXXX').upper()
copyright = os.getenv('CONFIG_COPYRIGHT', 'YYYY SOPHGO Co., Ltd')
author = os.getenv('CONFIG_AUTHOR', 'Sophgo')
release = os.getenv('CONFIG_RELEASE', '?.?')
release_date = os.getenv('CONFIG_RELEASEDATE', 'yyyy-mm-dd')

language = os.getenv('CONFIG_LANG', 'en')

#print("----> project is:" + project)
#print("----> copyright is:" + copyright)
#print("----> author is:" + author)
#print("----> release is:" + release)
#print("----> release_date is:" + release_date)
#print("----> language is:" + language)

if language == 'cn':
	language = 'zh_CN'

if language == 'zh_CN':
	title = '技术参考手册'
	text_version = '版本 : '
	text_releasedate = '发布日期 : '
else:
	title = 'Technical Reference Manual'
	text_version = 'Version : '
	text_releasedate = 'Release Date : '
	

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
# eliminate "WARNING: duplicate label" when include rst files
# ALL *.rst files to be included should be renamed to *.table.rst.
exclude_patterns = ['**/*table.rst', 'contents-share']

#language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []

latex_maketitle = r'''
		\begin{titlepage}
		\begin{center}
		\includegraphics[width=0.4\textwidth]{SOPHON-LOGO.png}
		\vspace*{2cm}

		\Huge \textbf{'''+ project + r'''} \par
		\vspace*{1cm}
		\Huge \textbf{'''+ title + r'''} \par
		\vspace*{4cm}
		\end{center}
		\noindent \Large ''' + text_version + release + r'''\par
		\noindent \Large ''' + text_releasedate + release_date + r'''\par
		\vspace*{2cm}
		\noindent \normalsize Copyright © ''' + copyright + r'''. All rights reserved.\\
		\end{titlepage}'''

latex_preamble = r'''
		\usepackage{tocloft}
		\usepackage[document]{ragged2e}
		\newcommand{\sectionbreak}{\clearpage}
		\renewcommand\cftfignumwidth{4em}
		\renewcommand\cfttabnumwidth{4em}
		\renewcommand\cftsecnumwidth{4em}
		\renewcommand\cftsubsecnumwidth{6em}
		\renewcommand\cftparanumwidth{6em}
		\usepackage{fancyhdr}
		\setlength\headheight{14pt}
		\fancypagestyle{normal}{
			\fancyhead[R]{}
			\fancyhead[C]{\leftmark}
			\fancyfoot[C]{Copyright © ''' + copyright + r'''}
			\fancyfoot[R]{\thepage}
			\renewcommand{\headrulewidth}{0.4pt}
			\renewcommand{\footrulewidth}{0pt}
		}'''

latex_elements = {
	'maketitle': latex_maketitle,

	'preamble': latex_preamble,

	# latex figure (float) alignment. Default is htbp(Here, Top, Bottom,
	# individual Page), so the figure may be moved/float to next page
	# and make the figure appear at wrong position.
	# Below configuration makes the figure located at where the code programmed.
	'figure_align': 'H',
}

# see https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-latex_table_style
# Because of the resolution problem, when 'colorrows' is enabled, the black
# border of the table is not displayed clearly on the pdf, so use default style.
latex_table_style = []

# auto numbering the figure/table/code-block
number_figures = True
numfig = True
numfig_secnum_depth = 1
if language == 'zh_CN':
	numfig_format = {'figure': '图%s', 'code-block': '程序清单%s', 'table': '表%s'}
else:
	numfig_format = {'figure': 'Diagram %s', 'code-block': 'Source Code %s', 'table': 'Table %s'}

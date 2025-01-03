# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SG2042_Benchmark'
copyright = '2024, Dongjing Song'
author = 'Dongjing Song'
release = 'v1.0(运行步骤还未经过严格验证,pdf排版还有些问题)'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for LaTeX outpu三t ------------------------------------------------
master_doc = 'index'

latex_engine = 'xelatex'
latex_elements = {
    # Papersize ('letterpaper' or 'a4paper'), default is letterpaper
    'papersize': 'a4paper',
    # 设置页边距大小
    'geometry': r' \usepackage[left=2.8cm,right=2.6cm,top=3.7cm,bottom=3.5cm]{geometry}',
    # The font size ('10pt', '11pt' or '12pt'), default is '10pt'.
    'pointsize': '11pt',
    # \setCJKmainfont[BoldFont=Heiti SC Medium]{Heiti SC Light}
    # \setCJKmonofont[BoldFont=Times Regular]{Times Italic}
    # `\setmainfont`、`\setsansfont{}`、`\setmonofont{}`
    # 分别设置正文字体、无衬线字体：标题、等宽字体：用于抄录内容
    'fontpkg': r'''
    \setmainfont{FandolSong}
    \setsansfont{FandolHei}
    \setmonofont{FandolFang}
    ''',
    # 设置章节标题样式
    # \usepackage[Lenny]{fncychap}  Bjarne, Sonny, Lenny, Glenn, Conny, Rejne
    'fncychap': '\\usepackage[Sonny]{fncychap}',
    # 图片严格出现在文字处
    # 'figure_align': 'H',
    # preamble 样式
    # 目录样式：tocloft
    # 每节从新页面开始：newcommand{\sectionbreak}{\clearpage}
    # 全文文本左对齐：\usepackage[document]{ragged2e}
    'preamble':r'''
    \usepackage[UTF8]{ctex}
    \usepackage{tocloft}
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
        \fancyfoot[C]{Copyright © SOPHGO}
        \fancyfoot[R]{\thepage}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0pt}

    }

    ''',



    'extraclassoptions': 'openany,oneside',

    # 'classoptions': ',zh_CN',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# latex_logo = '../../common/images/logo.png'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, project + u'.tex', u'SG2042 benchmark测试手册',
     author, 'manual'),
]
# Guide on how to setup build env on Ubuntu and create pdf for TRM.

Install Sphinx:

```bash
sudo apt-get update
sudo apt-get install python3-sphinx
```

Install PDF generation tools:

```bash
sudo apt-get install texlive-latex-recommended
sudo apt-get install texlive-latex-extra
sudo apt-get install latexmk
```

Create pdf:
```bash
cd SG2042/TRM 
make latexpdf
```

You can see pdf is generated as `./build/latex/SG2042TechnicalReferenceManual.pdf`


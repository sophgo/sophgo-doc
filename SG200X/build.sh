#! /bin/bash

ROOT=$(pwd)

document_list=(
    TRM/sg2000_cn
    TRM/sg2000_en
    TRM/sg2002_cn
    TRM/sg2002_en
)

build_html() {
	make -C $1 clean
    
	make -C $1 html
    
	mkdir -p out/$1
	mv $1/build/html ${ROOT}/out/$1

	make -C $1 clean
}

build_pdf() {
	make -C $1 clean
    
	make -C $1 pdf
    
	mkdir -p out/$1
	mv $1/build/*.pdf ${ROOT}/out/$1

	make -C $1 clean
}

build() {
	build_pdf $1
#	build_html $1
}


# Start executing ...
rm -rf ${ROOT}/out
mkdir ${ROOT}/out

if [ -n "$1" ]; then
	build $1
	exit
fi

for dir_name in ${document_list[*]}
do
	build $dir_name
done

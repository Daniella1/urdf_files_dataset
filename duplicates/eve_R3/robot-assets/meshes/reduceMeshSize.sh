#!/bin/sh

for img in `ls *png`; do
	w=`convert $img -print "%w" /dev/null`
	if [ $w -gt 1024 ]; then
		convert -verbose -resize 50% $img $img
	fi
done

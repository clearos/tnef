#! /bin/bash
# /usr/bin/tnef.sh
# 
# nautilus helper to extract a tnef file's contents into a subfolder of the 
#     tnef file's location.
#   todo: 
# error checking (disk space, unwritable etc).
# how could the calling nautilus window be told to refresh it's contents so the
#    extracted folder becomes visible straight away. (for paths with spaces).
filefullpath="$1"
file=`basename "$filefullpath"`
filepath="`dirname "$filefullpath"`/"$file".extract"
#echo $filefullpath
#echo $file
#echo $filepath
if ! [ -d "$filepath" ]; then
  echo "  creating folder $filepath..."
  mkdir "$filepath"
  echo "  extracting $file tnef contents..."
  tnef --verbose --save-body -C "$filepath" "$filefullpath"
  echo "  complete."
  sleep 4
else
  echo "  default extract folder $filepath"
  echo "      already exists, extraction aborted."
  sleep 6
fi


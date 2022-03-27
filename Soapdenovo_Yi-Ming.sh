#! /bin/bash

# Usage
# soapdenovo.sh -i [input_dir] -o [output_dir] -h

# Process flags

while getopts "i:o:h" options; do

case "${options}" in
    i)
        if ${OPTARG} == "" ; then echo "No input directory specified. Exiting", exit; fi
        IDIR=${OPTARG}
        ;;
    o)
        if ${OPTARG} == null ; then echo "No output directory specified. Exiting";exit; fi
        ODIR=${OPTARG}
        ;;
    h)
         echo "Usage: $0 [ -i Top Level Data Directory ] [ -o output directory ]"
        exit
        ;;
    :)
        echo "Usage: $0 [ -i Top Level Data Directory ] [ -o output directory ]"
        exit
        ;;
esac

done

# chage directory to the -i location

cd $IDIR
# process all of the files in the input directory

TMP="CGT_tmp"
for FILE in *
        do
         vi ../Soap_config +$":%s/$TMP/${FILE}/g" +w +q
         SOAPdenovo-127mer all -s ../Soap_config -K 63 -R -o ${ODIR}/${FILE}/${FILE}
         TMP=${FILE}
        done

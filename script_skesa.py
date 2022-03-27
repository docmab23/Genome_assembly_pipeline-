#!/usr/bin/env python3

# script to run assembly tool skesa 
# command ./script_skesa.py -i input/file/path -o output/file/path -c core[optional; by default = 1]


import re
import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description="Skesa Genome Assembly")
parser.add_argument("-o", "--outputpath", help="path to the output sequence directory", required=True)
parser.add_argument("-i", "--inputpath", help="path to the input sequence directory", required=True)
parser.add_argument("-c", "--cores", help="number of cores; by default = 1", type=str, default="1")

args = parser.parse_args()

# to list all the sequence directories in the directory
all_seq_directories = os.listdir(args.inputpath)



# to iterate all the sequence directories and read their paired reads
for directory in all_seq_directories: 
	
	print("inside directory =", directory)
	for file in os.listdir(args.inputpath+"/"+directory): # list of paired reads in the directory
		if file.endswith("_1.fq"):
			print("inside _1.fq and file =", file)
			read1 = file
		if file.endswith("_2.fq"):
			print("inside _2.fastq and file =", file)
			read2 = file
		
	print("read 1: ", read1) 
	print("read 2: ", read2)

	read_1_loc = args.inputpath+"/"+directory+"/"+read1 #defining location of read1 for skesa
	read_2_loc = args.inputpath+"/"+directory+"/"+read2 #defining location of read2 for skesa

	contig_file_name = read1.split("_1.")[0]+"."+"fa" #defining output config file name as "readfile prefix + .fa"
	assembled_read_loc = args.outputpath+"/"+contig_file_name #defining location of output file as given by user

	print("assembled_read_loc", assembled_read_loc) 
	subprocess.call(["skesa", "--fastq", read_1_loc, read_2_loc, "--cores",	args.cores, "--contigs_out", assembled_read_loc])

	

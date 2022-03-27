#!/usr/bin/env python3

# script to run quality control tool QUAST
# command: ./script_quast.py -i <path to the directory containing assembled contig files/ fasta files> -o <output directory path, the path should not have space in the directories name>
# This script uses Quast to automatically make directory,to output the results, for each contig, inside the ouput directory path specified by the user


import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description="QC using QUAST")
parser.add_argument("-o", "--outputpath", help="path to the output sequence directory", required=True)
parser.add_argument("-i", "--inputpath", help="path to the input sequence directory", required=True)

args = parser.parse_args()


for file in os.listdir(args.inputpath): # taking one assembled read at a time
	if file.endswith(".fa") or file.endswith(".fasta"): 
		print("Working with file =", file)

		assembled_read_loc = args.inputpath+"/"+file #defining location of input file

		print("assembled_read_loc", assembled_read_loc) 
		
		quast_report_folder_name = file.split(".")[0]+"_quast"
		quast_report_folder_location = args.outputpath+"/"+quast_report_folder_name
		subprocess.call(["quast.py", "-o", quast_report_folder_location, assembled_read_loc])

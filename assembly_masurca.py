#!/home/alterego/anaconda3/bin/python

###############################################################################
#Since Masurca takes really long time, I wrote multiprocessing for parallel   #
#execution. To run this assembly file, please first generate a sample.txt file#
#that contains a list of samples you want to do the assembly. It should look  #
#like "CGTXXXX\nCGTXXXX\n". Then, change the destination dir path to your     #
#dir you want to do the assembly, and change source_dir if needed. To run the #
#script, in the command line type "python3 assembly_masurca.py sample.txt"    #
###############################################################################
import subprocess
import argparse
import os
import sys
import re
import multiprocessing as mp
import copy

#Path to output dir
destination_dir = ""
#Path to source dir
source_dir = "/home/groupa/trimming/trimmed/"

#Function for running single sample
def masurca(sample):
	#clean out the \n at the end for read sample "CGTXXXX"
	sample = re.sub(pattern = "\n", string = sample, repl = "")
	#change directory to the destination directory
	os.chdir(destination_dir)
	#Create a directory named after sample
	os.system("mkdir "+sample)
	os.chdir(sample)
	#In the sample subdirectory, create the sample config file that needs further modification
	os.system("masurca -g run.txt")
	os.system("chmod 755 run.txt")

	#The following paragraph change the path to the file in the config and write the modified content into a new file called "new.txt"
	with open("run.txt","r") as file:	
		content = file.readlines()
		newcontent = []
		for line in content:
			line = re.sub(pattern="PE= pe 500 50  /FULL_PATH/frag_1.fastq  /FULL_PATH/frag_2.fastq",repl="PE= pe 500 50  /home/groupa/trimming/trimmed/"+sample+"/"+sample+"_1.fq /home/groupa/trimming/trimmed/"+sample+"/"+sample+"_2.fq",string = line)
			line = re.sub(pattern="JUMP= sh 3600 200  ", repl="#JUMP= sh 3600 200  ",string = line)
			newcontent.append(line)
	with open("new.txt","a") as file2:
		for line in newcontent:
			file2.write(line)

	file.close()
	file2.close()

	#masurca configure the txt and generate a bash script
	os.system("masurca new.txt")
	#masurca actually run
	os.system("nohup /bin/bash assemble.sh &")

#Open file for reading samplelist
with open(sys.argv[1],"r") as samplelist:
	samples = samplelist.readlines()

#The following paragraph uses multiprocessing for parallel execution of masurca
pool = mp.Pool(mp.cpu_count())

result = pool.map(masurca, [sample for sample in samples])

pool.close()

	

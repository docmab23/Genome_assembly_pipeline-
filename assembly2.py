#!/home/alterego/anaconda3/bin/python

import subprocess
import argparse
import os
import glob

parser = argparse.ArgumentParser(description='Run Spades')
parser.add_argument('trimmed',
                    help='')
parser.add_argument('out',
                    help='',default="../pilot")

args = parser.parse_args()
output= args.out
trimmed_dir=args.trimmed
samples=list(glob.glob("{t}*".format(t=trimmed_dir)))
print(samples)
samples = [s.split("/")[-1] for s in samples]
for s in samples:
    name=str(s)
    read1= "{t}{n}/{n}_1.fq".format(t=trimmed_dir,n=name)
    read2= "{t}{n}/{n}_2.fq".format(t=trimmed_dir,n=name)
    os.mkdir("{i}/{n}".format(i=output,n=name))
    subprocess.call("spades.py --pe1-1 {re1} --pe1-2 {re2} -o {i}/{n}".format(re1=read1,re2=read2,i=output,n=name),shell=True)


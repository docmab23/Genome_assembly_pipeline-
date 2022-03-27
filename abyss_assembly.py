#!/usr/bin/env python3

import subprocess
import os
import shlex

inputfiles_path = '/home/groupa/trimming/trimmed/'
outputfiles_path = '/home/assembly/results/'

pairedend_forward = []
pairedend_reverse = []
k_value = 25
read_name = inputfiles_path.split("/")[-1]

for file in os.listdir(inputfiles_path):
    if file.endswith('_1.fq'):
        pairedend_forward.append(file)
       #print(pairedend_forward)
    if file.endswith('_2.fq'):
        pairedend_reverse.append(file)
       #print(pairedend_reverse)

forward_read = str(pairedend_forward)
#print(forward_read)
reverse_read = str(pairedend_reverse)
#print(reverse_read)

abyss_result = subprocess.call(shlex.split(f"abyss-pe k={k_value}.format(k_value) name={read_name}.format(read_name) in={forward_read} {reverse_read}.format(forward_read reverse_read"))
print(abyss_result)



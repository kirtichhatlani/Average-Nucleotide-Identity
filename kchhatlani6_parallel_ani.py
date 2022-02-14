#!/usr/bin/env python3
import argparse
import sys
import os
import subprocess
from multiprocessing import Pool

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--threads", help = "Number of threads for running", type=int)
parser.add_argument("file", nargs='+')
parser.add_argument("-o", help = "output filename.")
args = parser.parse_args()

outputname = args.o
input_files = args.file
n=len(input_files)

input_list =[]
for i in range(n):
	for j in range(i+1,n):
		input_list.append(input_files[i])
		input_list.append(input_files[j])

input_list=zip(input_list[::2],input_list[1::2])
def avg_nucl_identity(gen):
	output_file=[]
	cmd = "dnadiff -p "+str(gen[0]+gen[1])+" "+gen[0]+" "+gen[1]
	os.system(cmd)
	with open(str(gen[0]+gen[1])+".report","r") as f2:
		count=0
		count1=0
		for out in f2.readlines():
			out=out.strip("\n").strip(" ")
			if out[0:11]=="AvgIdentity" and count==0:
				for k in out.split(" "):
					if k!="AvgIdentity" and len(k)>1 and count1==0:
						output_file.append(gen[0])
						output_file.append(gen[1])
						output_file.append(k)
						count1+=1
						
	rm="rm "+str(gen[0]+gen[1])+"*"
	os.system(rm)
	return output_file
	

matrix = [ [ 0 for i in range(n+1) ] for j in range(n+1) ]
l1=len(matrix[0])
for i in range(1,l1):
	matrix[i][i]=100

matlist=[" "]
matlist.extend(input_files)
m=len(matlist)
for i in range(m):
        matrix[i][0]=matlist[i]
        matrix[0][i]=matlist[i]

p = Pool(args.threads) 
semi_final=p.map(avg_nucl_identity, input_list)
final=[]
for sub in semi_final:
	for i in sub:
		final.append(i)			
p.close()
p.join()

for i in range(1,n+1):
	for j in range(1,n+1):
		for k in range(len(final)):
			if (matrix[i][0]==final[k]) and (matrix[0][j]==final[k+1]):
				matrix[i][j]=matrix[j][i]=final[k+2]
#print(matrix)
with open(outputname, 'w') as fh:
	for line in matrix:
		for val in line:
			fh.write(str(val)+'\t')
		fh.write('\n')
	fh.close()

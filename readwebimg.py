#! /usr/bin/env python

import os
import re


def main():
 # Read Index File
 fileIndex = open("webidx")
 fileImage = open('webimg', mode='r+')
 fileContent = fileImage.read()
 currentDir = os.getcwd()
 for i, line in enumerate(fileIndex):
	#fileLine=fileIndex.readlines()
	print line
	print i
	if re.findall('(.*?):',str(line)) == ['path']:
		os.chdir(currentDir)
		path = str(re.findall('path:(.*?)\n',str(line))[0])
		print path
		if not os.path.exists(path):
	    		 	os.makedirs(path)
		os.chdir(path)
	else:
		[(fileName,fileSize,fileStart)] = re.findall(r"(.*?) (\d+) (\d+)",str(line))
		print fileName
		print fileSize
		print fileStart
		fileEnd = int(fileStart) + int(fileSize)
		print fileEnd
	
		
		out = open(str(fileName),"a+")
		outContent = fileContent[int(fileStart):int(fileEnd)]
		out.write(outContent)
		out.close


 fileIndex.close




#def writeFile(data):
#	fo = open("data.txt","a+")
#	for item in data:
#		fo.write(item+'\t')
##	fo.write('\n')
#	fo.close
#	return 1

######################################################################
if __name__ == "__main__": 
    main()  
#EOF

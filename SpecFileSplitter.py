import sys
import os

digits=4

if(len(sys.argv)<2):
	print("usage: python SpecFileSplitter.py [datafile]")
	sys.exit()

if(os.path.exists(sys.argv[1])):
	inputfile=sys.argv[1]
	FH = open(inputfile,"r")
else:
	print("%s does not exist."%(sys.argv[1]))
	sys.exit()

filenum=0
writeflag=0
for line in FH:
	if ('#S' in line):
		filenum+=1
	elif('#L' in line):
		fn_str=str(filenum).zfill(digits)
		FH2 = open("data_%s.txt"%(fn_str),"w")
		writeflag=1
		line2=line.replace('#L ','')
		line3=line2.replace('Two Theta','TwoTheta')
		FH2.write(line3)
	else:
		if('#' in line):
			if(writeflag==1):
				FH2.close()
				writeflag=0
		else:
			if(writeflag==1):
				FH2.write(line)

FH.close()


import sys
import csv
import json
from hashlib import sha1
import time

crawl_date=time.strftime('%Y%m%d')

def JsonToCsv(inputfile,outputfile):
        print "going to convert jsontocsv"
	outfile=open(outputfile,"w+")
	first_write=0
	for line in open(inputfile):
		try:
			json_line=json.loads(line)
			if first_write==0:
				header=json_line.keys()
				#print ','.join(header)
				print >> outfile,','.join(header)
				first_write=1
			print >>outfile,','.join(json_line.values())
				
		except Exception,e:
			print  >>sys.stderr, repr(e)
	outfile.close()

inputfile=sys.argv[1]
outputfile=sys.argv[2]
JsonToCsv(inputfile,outputfile)
#rajesh
#1.what will happen if json file contains object with different keys,so u can't depend upon only key of first line
#if some value is comma separated then we must put those values inside double qoutes.
#i have added flipkart json file that is converted into some csv ,but csv didn't contains all the fields
#if u convert some json to csv then its vice versa should also exist i.e form ur csv file we should able to get exact same json file.
#try urself with flipkart data
#although this is just for getting familiarity with git but if every thing init is fine then in that case we can use those script into our pipeline also

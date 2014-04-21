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

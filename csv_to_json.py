import sys
import csv
import json
from hashlib import sha1
import time

crawl_date=time.strftime('%Y%m%d')

def CsvToJson(inputfile,outputfile):
        print "going to convert csv to json"
        inputfile_result=csv.DictReader(open(inputfile))
        outfile_obj=open(outputfile,'w')
        for row in inputfile_result:
                #url=row['url']
                #urlh=sha1(url).hexdigest()
                #row.update({'urlh':urlh,'crawl_date':crawl_date})
                outfile_obj.write(json.dumps(row)+"\n")
        outfile_obj.close()

if __name__=="__main__":
        inputfile=sys.argv[1]
        outputfile=sys.argv[2]
        CsvToJson(inputfile,outputfile)

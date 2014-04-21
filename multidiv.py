import sys
a=sys.argv[1]
b=sys.argv[2]
c=sys.argv[3]
data=''

#print a,b,c
if b=='m':

	data=float(a)*float(c)
elif b=='d':
	try:
		data=float(a)/float(c)
	except:
		data='Divison by zero is not possibel'
print data

x= int(input())
print 'yes'
count =1
lis = []
while True:
	try:
		z = int(input())	
	
		l = x+count
		lis.append(l)
		if count == 1:
			count =2
		elif count ==2 :
			count =3
		elif count ==3:
			count = 1
		x = l
		if z in lis:
			print 'yes'
		else:
			print 'no'
	except:
		break
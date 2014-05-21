while True:
	try:
		x = int(input())
	except:
		break
	if (x-1)%6 == 0 or (x-3)%6==0 or x%6==0:
		print 'yes'
	else:
		print 'no'
c = int(input())
for j in xrange(c):
	x = raw_input()
	#end = []
	bul = 0
	deo = 0
	cro = 0
	maxi = 0
	z = len(x)
	zur = [0 for i in range(z)]
	for i in range(z):
		if x[i]=='>' and bul>0:
			#end.append(i)
			cro+=1
			bul-=1
			if zur[bul]<zur[bul]+1:
				zur[bul] = zur[bul]+1
		elif x[i]=='>' and bul==0:
			#zor = len(end)*2
			#print zor
			#end = []
			pass
		elif x[i]=='<':
			bul+=1
			deo+=1
	print zur

x,y,z = map(int,raw_input().split())
lol = {}

for i in xrange(z):
  z1,z2 = map(int,raw_input().split())
  if z1 not in lol:
  	lol[z1] = {z2:1}
  else:
  	if z2 not in lol[z1]:
  		lol[z1][z2]=1
  	else:
  		lol[z1][z2]+=1
if y==1:
	for i in xrange(1,x+1):
		print 0
else:
	for i in xrange(1,x+1):
		cost = y-1
		flag = 0
		if i in lol:
			for j in lol[i]:
				if j-1 not in lol[i] and j-1>=1:
					cost+=lol[i][j]
				if j+1<=y:
					if j+1 in lol[i]:
						if lol[i][j]-lol[i][j+1]==1:
							cost-=1
						elif lol[i][j]-lol[i][j+1]<1:
							cost+=lol[i][j+1]-lol[i][j]
							continue
						else:
							print -1
							flag=1
							break
					else:
						if lol[i][j]>1 and j+1<=y:
							print -1
							flag=1
							break
						else:
							cost-=1
			if flag==0:
				print cost
	 	else:
	 		print cost
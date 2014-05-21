from itertools import combinations

q = int(input())
for m in xrange(q):
	x,y = map(int,raw_input().split())
	baloo = {}
	res = []
	count =0
	summ = 0
	for o in xrange(x):
		t,p = map(int,raw_input().split())
		if t in baloo:
			baloo[t].append(p)
		else:
			baloo[t] = [p]
	for o in baloo:
			ach = len(baloo[o])
			res.append(float((2**(ach-1))*sum(baloo[o]))/float((2**ach)-1))
	print res
	if y==0:
		for i in xrange(1,x+1):
			for a in combinations(res,i):
				summ += sum(a)
				count+=1
		print("%.9f" %(float(summ)/float(count+1)))
	else:
		for i in xrange(y,x+1):
			for a in combinations(res,i):
				summ += sum(a)
				count+=1
		print("%.9f" %(float(summ)/float(count)))
def getsec(s):
	l = s.split(':')
	return int(l[0])*3600+int(l[1])*60

x = int(input())
l = []
for i in xrange(x):
	z = raw_input().split('-')
	x1 = getsec(z[0])
	l.append(x1)
	x2 = getsec(z[1])
	l.append(x2)
l.sort()
flag = 0
for i in range(len(l)-1):
	if l[i]>l[i+1] and l[i]!=l[i+1]:
		flag = 1
		print 'Will need a moderator!'
		break
if flag==0:
	print 'Who needs a moderator?'
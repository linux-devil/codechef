i,j = map(int,raw_input().split())
p = map(int, raw_input().split())

for i in range(j):
	l = max(p)
	p = [(l-x) for x in p]
print ' '.join([str(i) for i in p])
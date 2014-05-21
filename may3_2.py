c = int(input())
for j in xrange(c):
  x = raw_input()
  z = len(x)
  s = []
  maxx = 0
  c = [-1 for i in xrange(z)]
  d = [-1 for i in xrange(z)]
  for i in xrange(z):
    if x[i] == '<':
      s.append(i)
    else:
      if s:
        d[i] = s.pop()
        c[i] = d[i]
        q = d[i]-1
        if q >0 and x[q] == '>' and c[q]!=-1:
          c[i] = c[q]
        manu = i-c[i]+1
        if maxx<manu:
          maxx = manu
  print maxx

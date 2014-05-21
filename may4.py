x,y,z = map(int,raw_input().split())
lok = [[i for i in xrange(1,y+1)]for i in xrange(x)]
for i in xrange(z):
  z1,z2 = map(int,raw_input().split())
  lok[z1-1][z2-1]+=1
for j in xrange(x):
  cost =0
  flag=0
  for i in xrange(y-2,-1,-1):
    if lok[j][i+1]>=lok[j][i]:
      cost+=(lok[j][i+1]-lok[j][i])
    else:
      flag = 1
      break
  if flag==0:
    print cost
  else:
    print -1

t=int(raw_input())
for j in xrange(t):
  r,c=map(int,raw_input().strip().split())
  if r>c:
    r,c=c,r
    swapped=True
  else:
    swapped=False
  if r==4 and c==4:
    res=[(1,1),(2,3),(3,1),(4,3),(1,2),(2,4),(3,2),(4,4),
         (1,3),(2,1),(3,3),(4,1),(3,4),(4,2),(1,4),(2,2)]
  elif c<4:
    res="IMPOSSIBLE"
  elif c==4 and r==2:
    res="IMPOSSIBLE"
  else:
    #build up solution by 2 or 3 rows at a time.
    res=[]
    usedrows=0
    for k in xrange(r/2):
      if usedrows==r-3:
        #insert a 3-row pattern
        for trip in xrange(c-2):
          res.append((usedrows+1,trip+1))
          res.append((usedrows+2,trip+3))
          res.append((usedrows+3,trip+1))
        res.append((usedrows+1,c-1))
        res.append((usedrows+2,1))
        res.append((usedrows+3,c-1))
        res.append((usedrows+1,c))
        res.append((usedrows+2,2))
        res.append((usedrows+3,c))
        usedrows+=3
      else:
        #insert a 2-row pattern
        for trip in xrange(c-2):
          res.append((usedrows+1,trip+3))
          res.append((usedrows+2,trip+1))
        res.append((usedrows+1,1))
        res.append((usedrows+2,c-1))
        res.append((usedrows+1,2))
        res.append((usedrows+2,c))
        usedrows+=2
  if res=="IMPOSSIBLE":
    print "Case #"+str(j+1)+": IMPOSSIBLE"
  else:
    print "Case #"+str(j+1)+": POSSIBLE"
    #check result
    #if len(res)!=len(set(res)):
    #  print "ERROR:",len(res)-len(set(res)),"repeats"
    #for k in xrange(1,len(res)):
    #  r1,c1=res[k-1]
    #  r2,c2=res[k]
    #  if r1==r2 or c1==c2 or r1-c1==r2-c2 or r1+c1==r2+c2:
    #    print "ERROR at move",k
    for rr,cc in res:
      if swapped:
        print str(cc)+" "+str(rr)
      else:
        print str(rr)+" "+str(cc)
        

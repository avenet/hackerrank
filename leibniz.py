s=xrange
for i in s(input()):
  r=0
  for j in s(input()):r+=(j%2==0 and 1 or -1)/(2*j+1.0)
  print r  
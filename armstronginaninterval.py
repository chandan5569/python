x=int(input('enter the lower range'))
y=int(input('enter the upper range'))
for i in range(x,y+1):

  w=i
  y=0
  z=0

  if i < 1000:

    while i>0:
      y=i%10
      z=z+y*y*y
      i=i//10
    if w==z :
      print(w)
  else:
    while i>0:
      y=i%10
      z=z+y*y*y*y
      i=i//10
    if w==z:
      print(w)




  


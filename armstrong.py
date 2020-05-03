x=int(input('enter the number you want to check that wheather it is armstrong or not'))
y=0
z=0
w=x
while x>0:

  y=x%10
  z=z+y*y*y
  x=x//10
if z==w:
  print(w,'is a armstrong number')
else:
  print(w,'is not a armstrong number')

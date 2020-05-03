x=int(input('enter the first number'))
y=int(input('enter the second number'))
z=int(input('enter the three number'))

if x>y and x>z:
  print(x,'is the greatest among all')
elif y>x and y>z:
  print(y,'is the greatest among all')
else:
  print(z,'is the greatest among all')
  
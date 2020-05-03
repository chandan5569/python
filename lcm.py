x=int(input('enter the first number'))
y=int(input('enter the second number'))

for i in range(1,x*y+1):

  if i%x==0 and i%y==0:
    break
print('Lcm of',x,'and',y,'is',i)

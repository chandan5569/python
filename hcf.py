x=int(input('enter the first number'))

y=int(input('enter the second number'))
a=x               #storing the temporary value
b=y
while x!=y:       #when the both the values are equal we will get out of the loop and resulting is HCF

  if x>y:
    x=x-y
  else:
    y=y-x
print('Hcf of',a,'and',b,'is ',y)

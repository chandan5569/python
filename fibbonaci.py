x=int(input('enter the number till you want to print the sequence'))
a=0
b=1
for i in range(1,x):
  c=a+b
  a=b
  b=c
  print(c)

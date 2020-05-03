x=int(input('enter a number to check if it is prime or not'))
count=0
for i in range(1,x+1):
  if x%1 == 0 and x%i==0:
    count+=1
if count==2:
  print('prime number')
else:
  print('not a prime number')
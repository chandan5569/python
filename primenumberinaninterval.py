x=int(input('enter the lower range from where you want to find the prime number'))
y=int(input('enter the upper range till where you want to find the prime number'))
for i in range(x,y+1):
  count=0
  for j in range(1,i+1):
    if i%1==0 and i%j==0:
      count+=1
  if count==2:
    print(i)

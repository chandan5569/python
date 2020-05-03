x=int(input('enter the number till you want to find the all the divisible numbers'))
print('Factors of',x,'are as follows:')
for i in range(1,x+1):
  if x%i == 0:
    print(i)

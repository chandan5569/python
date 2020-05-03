x=int(input('enter a number whose factor is to be found'))

print('Factors of',x,'are:')

for i in range(1,x+1):

  if x % i == 0:

    print(i)

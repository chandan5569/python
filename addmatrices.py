x=[
[1,2,3],
[4,5,6],
[7,8,9]
]

y=[
[1,2,3],
[4,5,6],
[7,8,9]
]


z=[
  [0,0,0],
  [0,0,0],
  [0,0,0]
]

for i in range(0,3):

  for j in range(0,3):

    z[i][j]=x[i][j]+y[i][j]


for i in range(0,3):

  for j in range(0,3):

    print(z[i][j])

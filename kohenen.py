def euclid_distance(input,weight):
  d=0
  for i in range(0,len(input)):
    d=d+(input[i]-weight[i])*(input[i]-weight[i])
  return d

import random
x=[[0,0,1,1],[1,0,0,0],[0,1,1,0],[0,0,0,1]]
alpha=0.5
w=[]
n=2
m=4
for i in range(0,n):
 a=[]
 for j in range(0,m):
   a.append(round(random.random(),2))
 w.append(a)
def kohenen_som():
 epoch=10
 for e in range(0,epoch):
  print(e+1)
  for i in range(0, len(x)):
    d=[0,0]
    for j in range (0,len(d)):
        d[j]=euclid_distance(x[i],w[j])
    min=10000
    idx=-1
    for j in range (0,n):
      if(d[j]<min):
        min=d[j]
        idx=j

    for j in range(0,m):
      w[idx][j]=w[idx][j]+alpha*(x[i][j]-w[idx][j])

  print(w)

kohenen_som()
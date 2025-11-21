x=[[0,0,0,1],[1,1,0,0],[0,1,1,0]]
w=[[0,0,1,1],[1,0,0,0]]
cluster=[1,2]
output=[2,1,1]
alpha=0.1

def euclid_distance(input,weight):
  d=0
  for i in range(0,len(input)):
    d=d+(input[i]-weight[i])*(input[i]-weight[i])
  return d

def lvq():
 epoch=3
 for e in range(0,epoch):
  print(e)
  for i in range(0,len(x)):
    d=[0,0]
    for j in range(0,len(d)):
      d[j]=euclid_distance(x[i],w[j])

    min=1000
    idx=-1
    for j in range(0,len(d)):
      if(d[j]<min):
        min=d[j]
        idx=j
    if(cluster[idx]!=output[i]):
      for j in range(0,len(x[i])):
        w[idx][j]=w[idx][j]-alpha*(x[i][j]-w[idx][j])
    else:
      for j in range(0,len(x[i])):
        w[idx][j]=w[idx][j]+alpha*(x[i][j]-w[idx][j])

    print(w)

lvq()
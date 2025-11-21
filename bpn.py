import math
def binary_sigmoidal(yin):
  return 1/(1+math.exp(-yin))

def sigmoidal_derrivative(yin):
  return binary_sigmoidal(yin)*(1-binary_sigmoidal(yin))

x=[1,0,1]
v=[[0.3,0.6,-0.1],[0.5,-0.3,0.4]]
w=[0.4,0.1]
t=1
alpha=0.25

def bpn():

#calculate zin and z (for hidden layer)
 zin=[0,0]
 for i in range(0,len(v)):
   for j in range(0,len(v[i])):
    zin[i]=zin[i]+x[j]*v[i][j]

 z=[0,0]
 for i in range(0,len(v)):
   z[i]=binary_sigmoidal(zin[i])

#calculate yin and y (for output layer)
 yin=-0.2
 for i in range(0,len(z)):
   yin=yin+z[i]*w[i]

 y=binary_sigmoidal(yin)

 #calculate error in output layer
 error_k=(t-y)*sigmoidal_derrivative(yin)

 #calculate change in weights of hidden-output layer
 delta_w=[0,0]
 for i in range(0,len(w)):
   delta_w[i]=error_k*alpha*z[i]
   w[i]=w[i]+delta_w[i]
 b=-0.2
 b=b+error_k*alpha

 #calculate error in hidden layer
 delta_error=[0,0]
 delta_error_in=[0,0]

 for i in range(0, len(w)):
   delta_error_in[i]= error_k*w[i]

 for i in range(0,len(delta_error_in)):
   delta_error[i]=delta_error_in[i]*sigmoidal_derrivative(zin[i])

 #calculate change in weights of inner-hidden layer
 delta_v=[]
 for i in range(0,len(v)):
   tuple_a=[0,0,0]
   for j in range(0,len(v[i])):
     tuple_a[j]=delta_error[i]*alpha*x[j]
   delta_v.append(tuple_a)

 for i in range (0,len(v)):
   for j in range(0,len(v[i])):
     v[i][j]=v[i][j]+delta_v[i][j]


 #print final weights
 print(v)
 print(str(b)+str(w))

epoch=3
for i in range(0,epoch):
  print(i)
  bpn()
  
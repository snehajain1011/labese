import numpy as np
P=np.array([0.1,0.3,0.7,0.4,0.2])
Q=np.array([0.1,0.3,0.3,0.4,0.5,0.2])
T=np.array([0.1,0.7,0.3])

R=np.zeros((len(P),len(Q)))
for i in range(len(P)):
  for j in range(len(Q)):
    R[i][j]=np.minimum(P[i],Q[j])
S=np.zeros((len(Q),len(T)))
for i in range(len(Q)):
  for j in range(len(T)):
    S[i][j]=np.minimum(Q[i],T[j])

M=np.zeros((len(P),len(T)))
for i in range(len(P)):
  for j in range(len(T)):
    M[i][j]=max([min(R[i][k],S[k][j]) for k in range(len(Q))])

M_p=np.zeros((len(P),len(T)))
for i in range(len(P)):
  for j in range(len(T)):
    M_p[i][j]=max([R[i][k]*S[k][j] for k in range(len(Q))])

print(M_p)




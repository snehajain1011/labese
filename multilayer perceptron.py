import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1,0],[1,0],[1,0],
              [0,1],[0,1],[0,1],
              [1,1],[1,1],[1,1]], dtype=float)

Y = np.array([0,0,0, 1,1,1, 2,2,2])
Y_onehot = np.eye(3)[Y]

def sigmoid(x): return 1/(1+np.exp(-x))
def dsigmoid(x): return sigmoid(x)*(1-sigmoid(x))

def relu(x): return np.maximum(0,x)
def drelu(x): return (x>0).astype(float)

def tanh(x): return np.tanh(x)
def dtanh(x): return 1-np.tanh(x)**2

def softmax(x):
    e = np.exp(x - np.max(x, axis=1, keepdims=True))
    return e/np.sum(e, axis=1, keepdims=True)

def train(activation, dactivation, epochs=500, lr=0.1):
    np.random.seed(1)
    W1 = np.random.randn(2,4)
    b1 = np.zeros((1,4))
    W2 = np.random.randn(4,3)
    b2 = np.zeros((1,3))
    losses = []
    for _ in range(epochs):
        z1 = X@W1 + b1
        a1 = activation(z1)
        z2 = a1@W2 + b2
        a2 = softmax(z2)
        loss = -np.mean(np.sum(Y_onehot*np.log(a2+1e-9), axis=1))
        losses.append(loss)
        dz2 = (a2 - Y_onehot)/X.shape[0]
        dW2 = a1.T@dz2
        db2 = np.sum(dz2, axis=0, keepdims=True)
        dz1 = dz2@W2.T * dactivation(z1)
        dW1 = X.T@dz1
        db1 = np.sum(dz1, axis=0, keepdims=True)
        W1 -= lr*dW1
        b1 -= lr*db1
        W2 -= lr*dW2
        b2 -= lr*db2
    return losses

sig_loss = train(sigmoid, dsigmoid)
relu_loss = train(relu, drelu)
tanh_loss = train(tanh, dtanh)

print("Final Losses:")
print("Sigmoid:", sig_loss[-1])
print("ReLU:", relu_loss[-1])
print("Tanh:", tanh_loss[-1])

plt.plot(sig_loss, label="Sigmoid")
plt.plot(relu_loss, label="ReLU")
plt.plot(tanh_loss, label="Tanh")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("MLP Loss Comparison")
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1,0],[1,0],[1,0],
              [0,1],[0,1],[0,1],
              [1,1],[1,1],[1,1]], dtype=float)

Y = np.array([0,0,0, 1,1,1, 2,2,2])
Y_onehot = np.eye(3)[Y]

def sigmoid(x): return 1/(1+np.exp(-x))
def relu(x): return np.maximum(0, x)
def tanh(x): return np.tanh(x)

def softmax(x):
    e = np.exp(x - np.max(x, axis=1, keepdims=True))
    return e / np.sum(e, axis=1, keepdims=True)

def train_single_layer(activation, epochs=300, lr=0.1):
    np.random.seed(0)
    W = np.random.randn(2, 3)
    b = np.zeros((1,3))
    losses = []

    for _ in range(epochs):
        z = X @ W + b
        a = activation(z)

        if activation == softmax:
            a2 = a
        else:
            a2 = softmax(a)

        loss = -np.mean(np.sum(Y_onehot * np.log(a2 + 1e-9), axis=1))
        losses.append(loss)

        dz = (a2 - Y_onehot) / X.shape[0]
        dW = X.T @ dz
        db = np.sum(dz, axis=0, keepdims=True)

        W -= lr * dW
        b -= lr * db

    return losses

sig_loss = train_single_layer(sigmoid)
relu_loss = train_single_layer(relu)
tanh_loss = train_single_layer(tanh)
softmax_loss = train_single_layer(softmax)

print("Final Losses:")
print("Sigmoid:", sig_loss[-1])
print("ReLU:", relu_loss[-1])
print("Tanh:", tanh_loss[-1])
print("Softmax:", softmax_loss[-1])

plt.plot(sig_loss, label="Sigmoid")
plt.plot(relu_loss, label="ReLU")
plt.plot(tanh_loss, label="Tanh")
plt.plot(softmax_loss, label="Softmax")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Single-Layer Perceptron Loss Comparison")
plt.legend()
plt.grid()
plt.show()

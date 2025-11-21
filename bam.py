import numpy as np

def bipolarize(arr):
    a = np.array(arr, dtype=float)
    return np.where(a > 0, 1, -1)

def train_bam(X_patterns, Y_patterns):
    X = bipolarize(X_patterns)
    Y = bipolarize(Y_patterns)
    if X.shape[0] != Y.shape[0]:
        raise ValueError("Pattern count mismatch")
    n_x = X.shape[1]
    n_y = Y.shape[1]
    W = np.zeros((n_x, n_y))
    for i in range(X.shape[0]):
        xi = X[i].reshape(n_x, 1)
        yi = Y[i].reshape(1, n_y)
        W += xi @ yi
    return W

def sign(v):
    return np.where(v >= 0, 1, -1)

def recall_bam(input_x=None, input_y=None, W=None, max_iters=50):
    if W is None:
        raise ValueError("W required")
    n_x, n_y = W.shape
    if input_x is None and input_y is None:
        raise ValueError("Give X or Y")

    if input_x is None:
        x = bipolarize(np.zeros(n_x))
    else:
        x = bipolarize(input_x).reshape(n_x)

    if input_y is None:
        y = bipolarize(np.zeros(n_y))
    else:
        y = bipolarize(input_y).reshape(n_y)

    if input_x is None:
        x = sign(W @ y)
    if input_y is None:
        y = sign(W.T @ x)

    for _ in range(max_iters):
        x_prev = x.copy()
        y_prev = y.copy()
        x = sign(W @ y)
        y = sign(W.T @ x)
        if np.array_equal(x, x_prev) and np.array_equal(y, y_prev):
            return x, y, True
    return x, y, False

if __name__ == "__main__":
    Xp = [
        [1, -1, 1, -1],
        [1, 1, -1, -1],
        [-1, 1, 1, -1]
    ]

    Yp = [
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, 1]
    ]

    W = train_bam(Xp, Yp)
    print("W:\n", W)

    noisy_x = [1, -1, -1, -1]
    print(recall_bam(input_x=noisy_x, W=W))

    noisy_y = [1, -1, -1]
    print(recall_bam(input_y=noisy_y, W=W))

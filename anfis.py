import numpy as np

# --------- 1. Gaussian Membership Function ----------
def gauss(x, c, s):
    return np.exp(-((x - c)**2) / (2 * s**2))

# --------- 2. ANFIS Inference Function ----------
def anfis_predict(x, y):
    
    # ---- Layer 1: Fuzzification (change centers as required) ----
    A1 = gauss(x, c1, s1)   # Input X small
    A2 = gauss(x, c2, s2)   # Input X medium
    A3 = gauss(x, c3, s3)   # Input X large

    B1 = gauss(y, d1, t1)   # Input Y small
    B2 = gauss(y, d2, t2)   # Input Y medium
    B3 = gauss(y, d3, t3)   # Input Y large

    # ---- Layer 2: Rule firing strengths ----
    w1 = A1 * B1            # Rule 1: small-small
    w2 = A2 * B2            # Rule 2: medium-medium
    w3 = A3 * B3            # Rule 3: large-large

    # ---- Layer 3: Normalize ----
    Wsum = w1 + w2 + w3 + 1e-6
    w1n = w1 / Wsum
    w2n = w2 / Wsum
    w3n = w3 / Wsum

    # ---- Layer 4: Sugeno Outputs (change p,q,r for each rule) ----
    f1 = p1*x + q1*y + r1
    f2 = p2*x + q2*y + r2
    f3 = p3*x + q3*y + r3

    # ---- Layer 5: Final Output ----
    output = w1n*f1 + w2n*f2 + w3n*f3
    return output

# --------- 3. Set Membership Parameters (change for your problem) ----------
# Centers & spreads for input X
c1, s1 = 20, 10
c2, s2 = 50, 10
c3, s3 = 80, 10

# Centers & spreads for input Y
d1, t1 = 20, 10
d2, t2 = 50, 10
d3, t3 = 80, 10

# --------- 4. Sugeno Consequent Parameters (change for your rules) ----------
p1, q1, r1 = 0.05, 0.05, 10    # Rule 1
p2, q2, r2 = 0.07, 0.07, 15    # Rule 2
p3, q3, r3 = 0.10, 0.10, 20    # Rule 3

# --------- 5. User Input ---------
x = float(input("Enter Input X: "))
y = float(input("Enter Input Y: "))

print("\nANFIS Output:", anfis_predict(x, y))

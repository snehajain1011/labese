import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
A = np.array([0, 0.2, 0.7, 0.8, 0.9, 1])
B = np.array([0, 0.1, 0.3, 0.2, 0.4, 0.5])

A_union_B = np.maximum(A, B)
A_intersect_B = np.minimum(A, B)

A_complement = 1 - A
B_complement = 1 - B

Abar_union_B = np.maximum(A_complement, B)
Abar_intersect_Bbar = np.minimum(A_complement, B_complement)

alg_sum = (A + B) - (A * B)
alg_prod = A * B

bounded_sum = np.minimum(1, A + B)
bounded_diff = np.maximum(0, A - B)

def fuzzy_set(values, x_labels):
    return "{ " + " ".join([f"{values[i]:.2f}/{x_labels[i]}" for i in range(len(values))]) + " }"

print("A ∪ B =", fuzzy_set(A_union_B, x))
print("A ∩ B =", fuzzy_set(A_intersect_B, x))
print("A̅ =", fuzzy_set(A_complement, x))
print("B̅ =", fuzzy_set(B_complement, x))
print("A̅ ∪ B =", fuzzy_set(Abar_union_B, x))
print("A̅ ∩ B̅ =", fuzzy_set(Abar_intersect_Bbar, x))
print("Algebraic Sum (A + B - A*B) =", fuzzy_set(alg_sum, x))
print("Algebraic Product (A*B) =", fuzzy_set(alg_prod, x))
print("Bounded Sum (min[1, A+B]) =", fuzzy_set(bounded_sum, x))
print("Bounded Difference (max[0, A-B]) =", fuzzy_set(bounded_diff, x))


import numpy as np

A_vals = np.array([0.3, 0.7, 1.0])
B_vals = np.array([0.4, 0.9])
C_vals = np.array([0.2, 0.8])

xA = ['x1', 'x2', 'x3']
yB = ['y1', 'y2']
zC = ['z1', 'z2']

# Relations
R = np.minimum.outer(A_vals, B_vals)  # A × B
S = np.minimum.outer(B_vals, C_vals)  # B × C

print("Relation R (A × B):\n", R)
print("Relation S (B × C):\n", S)

# Max–Min Composition
T_minmax = np.zeros((len(A_vals), len(C_vals)))
for i in range(len(A_vals)):
    for k in range(len(C_vals)):
        T_minmax[i, k] = np.max(np.minimum(R[i, :], S[:, k]))

# Max–Product Composition
T_maxprod = np.zeros((len(A_vals), len(C_vals)))
for i in range(len(A_vals)):
    for k in range(len(C_vals)):
        T_maxprod[i, k] = np.max(R[i, :] * S[:, k])

print("\nMax–Min Composition:\n", T_minmax)
print("\nMax–Product Composition:\n", T_maxprod)


import numpy as np
import matplotlib.pyplot as plt

def trimf(x, a, b, c):
    y = []
    for xi in x:
        if xi <= a or xi >= c:
            y.append(0.0)
        elif a < xi < b:
            y.append((xi - a) / (b - a))
        elif b <= xi < c:
            y.append((c - xi) / (c - b))
        else:
            y.append(0.0)
    return np.array(y)

distance = np.linspace(0, 2000, 2001)
speed = np.linspace(0, 25, 251)
brake = np.linspace(0, 100, 1001)

distance_vnear = trimf(distance, 0, 0, 500)
distance_near  = trimf(distance, 250, 750, 1250)
distance_far   = trimf(distance, 1000, 1500, 2000)
distance_vfar  = trimf(distance, 1500, 2000, 2000)

speed_slow   = trimf(speed, 0, 0, 8)
speed_medium = trimf(speed, 5, 10, 15)
speed_fast   = trimf(speed, 10, 17, 22)
speed_vfast  = trimf(speed, 18, 25, 25)

brake_low    = trimf(brake, 0, 0, 25)
brake_medium = trimf(brake, 20, 40, 60)
brake_high   = trimf(brake, 50, 70, 85)
brake_vhigh  = trimf(brake, 80, 100, 100)

dist_val = 600
speed_val = 18

mu_dvnear = np.interp(dist_val, distance, distance_vnear)
mu_dnear  = np.interp(dist_val, distance, distance_near)
mu_dfar   = np.interp(dist_val, distance, distance_far)
mu_dvfar  = np.interp(dist_val, distance, distance_vfar)

mu_sslow   = np.interp(speed_val, speed, speed_slow)
mu_smed    = np.interp(speed_val, speed, speed_medium)
mu_sfast   = np.interp(speed_val, speed, speed_fast)
mu_svfast  = np.interp(speed_val, speed, speed_vfast)

rule1 = min(mu_dvfar, mu_sslow)
rule2 = min(mu_dvfar, mu_sfast)
rule3 = min(mu_dfar, mu_sfast)
rule4 = min(mu_dnear, mu_sfast)
rule5 = min(mu_dnear, mu_smed)
rule6 = min(mu_dvnear, mu_sslow)
rule7 = min(mu_dvnear, mu_sfast)
rule8 = min(mu_dfar, mu_sslow)
rule9 = min(mu_dvfar, mu_svfast)

active_low    = np.fmin(rule1, brake_low)
active_medium = np.fmin(max(rule2, rule8), brake_medium)
active_high   = np.fmin(max(rule3, rule5, rule9), brake_high)
active_vhigh  = np.fmin(max(rule4, rule6, rule7), brake_vhigh)

aggregated = np.fmax(active_low,
              np.fmax(active_medium,
              np.fmax(active_high, active_vhigh)))

brake_power = np.sum(aggregated * brake) / np.sum(aggregated)

print(f"Distance: {dist_val} m")
print(f"Speed: {speed_val} km/h")
print(f"Calculated Brake Power: {brake_power:.2f}%")

plt.figure(figsize=(10,5))
plt.plot(brake, aggregated, 'r', linewidth=2, label='Aggregated Output')
plt.title("Aggregated Brake Power (Defuzzification)")
plt.xlabel("Brake Power (%)")
plt.ylabel("Membership")
plt.legend()
plt.grid(True)
plt.show()

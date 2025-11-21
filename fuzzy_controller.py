import numpy as np

# =========================================================
# 1. Membership Functions
# =========================================================

def triangular(x, a, b, c):
    """Triangular Membership Function"""
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a) if b != a else 1
    elif b < x < c:
        return (c - x) / (c - b) if c != b else 1


# =========================================================
# 2. FUZZIFICATION FUNCTIONS
#    (Modify these for ANY fuzzy controller problem)
# =========================================================

def fuzzify_dirt(d):
    return {
        'small': triangular(d, 0, 0, 50),
        'medium': triangular(d, 0, 50, 100),
        'large': triangular(d, 50, 100, 100)
    }

def fuzzify_grease(g):
    return {
        'small': triangular(g, 0, 0, 50),
        'medium': triangular(g, 0, 50, 100),
        'large': triangular(g, 50, 100, 100)
    }


# =========================================================
# 3. INFERENCE (RULE BASE)
#    (Modify rules according to the given question)
# =========================================================

def inference(ds, gs):

    # FULL washing machine 3x3 matrix

    very_small = min(ds['small'], gs['small'])

    small = max(
        min(ds['small'], gs['medium']),
        min(ds['medium'], gs['small'])
    )

    medium = max(
        min(ds['small'], gs['large']),
        min(ds['medium'], gs['medium']),
        min(ds['large'], gs['small'])
    )

    large = max(
        min(ds['medium'], gs['large']),
        min(ds['large'], gs['medium'])
    )

    very_large = min(ds['large'], gs['large'])

    return {
        'very_small': very_small,
        'small': small,
        'medium': medium,
        'large': large,
        'very_large': very_large
    }


# =========================================================
# 4. DEFUZZIFICATION METHODS
#    Choose ANY one (depending on your problem)
# =========================================================

# ---- 4A. Weighted Average (simple, most common)
def defuzz_weighted_average(output, crisp_values):
    num = sum(output[k] * crisp_values[k] for k in output)
    den = sum(output.values())
    return num / den if den != 0 else 0


# ---- 4B. Mean of Maximum (MoM)
def defuzz_mom(output, crisp_values):
    max_mu = max(output.values())
    candidates = [crisp_values[k] for k, v in output.items() if v == max_mu]
    return sum(candidates) / len(candidates) if candidates else 0


# ---- 4C. Smallest of Maximum (SoM)
def defuzz_som(output, crisp_values):
    max_mu = max(output.values())
    candidates = [crisp_values[k] for k, v in output.items() if v == max_mu]
    return min(candidates) if candidates else 0


# ---- 4D. Largest of Maximum (LoM)
def defuzz_lom(output, crisp_values):
    max_mu = max(output.values())
    candidates = [crisp_values[k] for k, v in output.items() if v == max_mu]
    return max(candidates) if candidates else 0


# ---- 4E. Centroid Defuzzification (Continuous Method)
def output_mf(category, z):
    if category == "very_small":
        return triangular(z, 0, 0, 10)
    elif category == "small":
        return triangular(z, 10, 15, 20)
    elif category == "medium":
        return triangular(z, 20, 25, 30)
    elif category == "large":
        return triangular(z, 30, 35, 40)
    elif category == "very_large":
        return triangular(z, 40, 50, 50)

def defuzz_centroid(output):
    z = np.linspace(0, 50, 501)
    mu = np.zeros_like(z)

    for i in range(len(z)):
        mu[i] = max(
            output_mf("very_small", z[i]) * output['very_small'],
            output_mf("small", z[i]) * output['small'],
            output_mf("medium", z[i]) * output['medium'],
            output_mf("large", z[i]) * output['large'],
            output_mf("very_large", z[i]) * output['very_large']
        )

    numerator = np.sum(z * mu)
    denominator = np.sum(mu)
    return numerator / denominator if denominator != 0 else 0


# =========================================================
# 5. MAIN CONTROLLER
# =========================================================

def fuzzy_wash_time(dirt, grease, method="weighted"):
    ds = fuzzify_dirt(dirt)
    gs = fuzzify_grease(grease)
    output = inference(ds, gs)

    crisp = {
        'very_small': 10,
        'small': 20,
        'medium': 30,
        'large': 40,
        'very_large': 50
    }

    if method == "weighted":
        return defuzz_weighted_average(output, crisp)
    if method == "mom":
        return defuzz_mom(output, crisp)
    if method == "som":
        return defuzz_som(output, crisp)
    if method == "lom":
        return defuzz_lom(output, crisp)
    if method == "centroid":
        return defuzz_centroid(output)

    return None


# =========================================================
# 6. USER INPUT
# =========================================================

dirt = float(input("Enter dirt (0–100): "))
grease = float(input("Enter grease (0–100): "))

wash_time = fuzzy_wash_time(dirt, grease, method="centroid")
print("\nRecommended Wash Time =", wash_time)

import numpy as np
def detect_drift(train, production):
    return np.abs(np.mean(train) - np.mean(production))
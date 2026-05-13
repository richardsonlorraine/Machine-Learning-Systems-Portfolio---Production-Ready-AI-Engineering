import numpy as np
def federated_averaging(local_weights):
    return np.mean(local_weights, axis=0)
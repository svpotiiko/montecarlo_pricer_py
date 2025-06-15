import numpy as np

# callable classes -> functions that will be plugged into the pricing engine
class EuropeanCallPayoff:
    def __init__(self, strike):
        self.strike = strike

    def __call__(self, paths):
        S_T = paths[:, -1]
        return np.maximum(S_T - self.strike, 0)

class EuropeanPutPayoff:
    def __init__(self, strike):
        self.strike = strike

    def __call__(self, paths):
        S_T = paths[:, -1]
        return np.maximum(self.strike - S_T, 0)

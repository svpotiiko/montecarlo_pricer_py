import numpy as np

# support for knock-in/knock-out options
class DownAndOutCallPayoff:
    def __init__(self, strike, barrier):
        self.strike = strike
        self.barrier = barrier

    def __call__(self, paths):
        barrier_breached = np.any(paths <= self.barrier, axis=1)
        S_T = paths[:, -1]
        payoff = np.maximum(S_T - self.strike, 0)
        payoff[barrier_breached] = 0  # Knocked out
        return payoff

class UpAndInCallPayoff:
    def __init__(self, strike, barrier):
        self.strike = strike
        self.barrier = barrier

    def __call__(self, paths):
        barrier_touched = np.any(paths >= self.barrier, axis=1)
        S_T = paths[:, -1]
        payoff = np.maximum(S_T - self.strike, 0)
        payoff[~barrier_touched] = 0  # Never activated
        return payoff

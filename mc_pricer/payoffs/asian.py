import numpy as np

# supports asian options (payoff depends on average pricing over time)
class AsianArithmeticCallPayoff:
    def __init__(self, strike):
        self.strike = strike

    def __call__(self, paths):
        avg_price = np.mean(paths[:, 1:], axis=1)  # Exclude S0 if needed
        return np.maximum(avg_price - self.strike, 0)

class AsianArithmeticPutPayoff:
    def __init__(self, strike):
        self.strike = strike

    def __call__(self, paths):
        avg_price = np.mean(paths[:, 1:], axis=1)
        return np.maximum(self.strike - avg_price, 0)

class AsianGeometricCallPayoff:
    def __init__(self, strike):
        self.strike = strike

    def __call__(self, paths):
        log_avg = np.mean(np.log(paths[:, 1:]), axis=1)
        geom_mean = np.exp(log_avg)
        return np.maximum(geom_mean - self.strike, 0)

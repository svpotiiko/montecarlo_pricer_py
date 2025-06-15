from mc_pricer.simulators.geometric_bm import GeometricBrownianMotionSimulator
from mc_pricer.utils.plots import plot_paths
import numpy as np

# main simulator
class GeometricBrownianMotionSimulator:
    def __init__(self, S0, mu, sigma, T, n_steps, n_paths, seed=42):
        self.S0 = S0
        self.mu = mu
        self.sigma = sigma
        self.T = T
        self.n_steps = n_steps
        self.n_paths = n_paths
        self.seed = seed

    def generate_paths(self):
        np.random.seed(self.seed)
        dt = self.T / self.n_steps
        paths = np.zeros((self.n_paths, self.n_steps + 1))
        paths[:, 0] = self.S0

        for t in range(1, self.n_steps + 1):
            z = np.random.standard_normal(self.n_paths)
            paths[:, t] = paths[:, t - 1] * np.exp(
                (self.mu - 0.5 * self.sigma ** 2) * dt + self.sigma * np.sqrt(dt) * z
            )

        return paths

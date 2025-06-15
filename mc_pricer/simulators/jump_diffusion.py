
from mc_pricer.utils.plots import plot_paths
import numpy as np

# jump diffusion introiduces sudden, discontinuous price changes and makes simulation engines more realistic
class JumpDiffusionSimulator:
    def __init__(self, S0, mu, sigma, T, n_steps, n_paths,
                 lambda_jump, mu_jump, sigma_jump, seed=42):
        self.S0 = S0
        self.mu = mu
        self.sigma = sigma
        self.T = T
        self.n_steps = n_steps
        self.n_paths = n_paths
        self.lambda_jump = lambda_jump  # average number of jumps per year
        self.mu_jump = mu_jump          # mean of log jump size
        self.sigma_jump = sigma_jump    # std of log jump size
        self.seed = seed

    def generate_paths(self):
        np.random.seed(self.seed)
        dt = self.T / self.n_steps
        paths = np.zeros((self.n_paths, self.n_steps + 1))
        paths[:, 0] = self.S0

        for t in range(1, self.n_steps + 1):
            z = np.random.standard_normal(self.n_paths)
            # Poisson-distributed number of jumps in dt
            n_jumps = np.random.poisson(self.lambda_jump * dt, self.n_paths)
            # Jump sizes drawn from lognormal
            jump_sizes = np.random.lognormal(self.mu_jump, self.sigma_jump, self.n_paths)

            jump_term = n_jumps * (jump_sizes - 1)  # E[J - 1]
            diffusion_term = (self.mu - 0.5 * self.sigma**2) * dt + self.sigma * np.sqrt(dt) * z

            paths[:, t] = paths[:, t - 1] * np.exp(diffusion_term + jump_term)

        return paths

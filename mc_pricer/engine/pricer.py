import numpy as np
from mc_pricer.utils.math_tools import discount_factor
from mc_pricer.utils.stats import confidence_interval

class MonteCarloPricer:
    def __init__(self, simulator, payoff, r, T, n_paths=10000, conf_level=0.95):
        """
        Parameters:
        - simulator: an instance of a simulator with .generate_paths() method
        - payoff: a callable payoff object (e.g., EuropeanCallPayoff)
        - r: risk-free interest rate
        - T: time to maturity (in years)
        - n_paths: number of Monte Carlo paths
        - conf_level: confidence level for interval estimation
        """
        self.simulator = simulator
        self.payoff = payoff
        self.r = r
        self.T = T
        self.n_paths = n_paths
        self.conf_level = conf_level

    def price(self):
        # 1. Generate simulated asset paths
        paths = self.simulator.generate_paths()

        # 2. Compute payoffs at maturity
        payoffs = self.payoff(paths)

        # 3. Discount to present value
        discounted = discount_factor(self.r, self.T) * payoffs

        # 4. Monte Carlo estimation
        mean_price = np.mean(discounted)
        ci_low, ci_high = confidence_interval(discounted, confidence=self.conf_level)

        return {
            "price": mean_price,
            "confidence_interval": (ci_low, ci_high),
            "std_error": np.std(discounted, ddof=1) / np.sqrt(self.n_paths)
        }

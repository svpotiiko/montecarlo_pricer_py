import numpy as np
from mc_pricer import (
    GeometricBrownianMotionSimulator, 
    JumpDiffusionSimulator,
    EuropeanCallPayoff, 
    EuropeanPutPayoff,
    AsianArithmeticCallPayoff,
    MonteCarloPricer
)

def main():
    # Market parameters
    S0 = 100        # Initial stock price
    K = 105         # Strike price
    r = 0.05        # Risk-free rate
    T = 1.0         # Time to maturity (1 year)
    sigma = 0.2     # Volatility
    mu = r          # Risk-neutral drift
    
    # Simulation parameters
    n_paths = 50000
    n_steps = 252   # Daily steps for 1 year
    
    print("=== Monte Carlo Option Pricing Results ===\n")
    
    # 1. European Call Option with GBM
    print("1. European Call Option (GBM)")
    simulator = GeometricBrownianMotionSimulator(S0, mu, sigma, T, n_steps, n_paths)
    payoff = EuropeanCallPayoff(K)
    pricer = MonteCarloPricer(simulator, payoff, r, T, n_paths)
    
    result = pricer.price()
    print(f"   Price: ${result['price']:.4f}")
    print(f"   95% CI: [${result['confidence_interval'][0]:.4f}, ${result['confidence_interval'][1]:.4f}]")
    print(f"   Std Error: ${result['std_error']:.4f}\n")
    
    # 2. European Put Option
    print("2. European Put Option (GBM)")
    put_payoff = EuropeanPutPayoff(K)
    put_pricer = MonteCarloPricer(simulator, put_payoff, r, T, n_paths)
    
    put_result = put_pricer.price()
    print(f"   Price: ${put_result['price']:.4f}")
    print(f"   95% CI: [${put_result['confidence_interval'][0]:.4f}, ${put_result['confidence_interval'][1]:.4f}]\n")
    
    # 3. Asian Arithmetic Call Option
    print("3. Asian Arithmetic Call Option")
    asian_payoff = AsianArithmeticCallPayoff(K)
    asian_pricer = MonteCarloPricer(simulator, asian_payoff, r, T, n_paths)
    
    asian_result = asian_pricer.price()
    print(f"   Price: ${asian_result['price']:.4f}")
    print(f"   95% CI: [${asian_result['confidence_interval'][0]:.4f}, ${asian_result['confidence_interval'][1]:.4f}]\n")
    
    # 4. Jump Diffusion Model
    print("4. European Call with Jump Diffusion")
    jump_sim = JumpDiffusionSimulator(
        S0=S0, mu=mu, sigma=sigma, T=T, n_steps=n_steps, n_paths=n_paths,
        lambda_jump=0.1, mu_jump=-0.05, sigma_jump=0.1
    )
    jump_pricer = MonteCarloPricer(jump_sim, payoff, r, T, n_paths)
    
    jump_result = jump_pricer.price()
    print(f"   Price: ${jump_result['price']:.4f}")
    print(f"   95% CI: [${jump_result['confidence_interval'][0]:.4f}, ${jump_result['confidence_interval'][1]:.4f}]\n")

if __name__ == "__main__":
    main()
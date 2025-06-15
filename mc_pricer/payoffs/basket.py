import numpy as np

# supports basket options (on avergae of multiple assets)
class BasketCallPayoff:
    def __init__(self, strike, weights=None):
        self.strike = strike
        self.weights = weights  # Optional: shape = (n_assets,)

    def __call__(self, asset_paths_list):
        # asset_paths_list: list of np.arrays [paths_asset1, paths_asset2, ...]
        final_prices = np.array([paths[:, -1] for paths in asset_paths_list])  # shape: (n_assets, n_paths)
        basket_price = (self.weights @ final_prices) if self.weights is not None else np.mean(final_prices, axis=0)
        return np.maximum(basket_price - self.strike, 0)

class BasketPutPayoff:
    def __init__(self, strike, weights=None):
        self.strike = strike
        self.weights = weights

    def __call__(self, asset_paths_list):
        final_prices = np.array([paths[:, -1] for paths in asset_paths_list])
        basket_price = (self.weights @ final_prices) if self.weights is not None else np.mean(final_prices, axis=0)
        return np.maximum(self.strike - basket_price, 0)

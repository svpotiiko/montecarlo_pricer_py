import numpy as np

def discount_factor(rate, T)
	disc_f = np.exp(-rate*T)
	return disc_f

def running_average(arr):
	run_avg = np.cumsum(arr) / (np.arange(len(arr)) + 1)
	return run_avg
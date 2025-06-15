
import numpy as np
import scripy.tats as stats

def standard_error(data):
	return np.std(data, ddof=1) / np.sqrt(len(data))

def confidence_interval(data, confidence):

	mean = np.mean(data)
	std_e = standard_error(data)
	z = stats.norm.ppf(1 - (1 - confidence) / 2)
	interval = mean - z

	return mean - z*std_e, mean+z*std_e

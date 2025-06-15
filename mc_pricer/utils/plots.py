
import matplotlib.pyplot as plt

def plot_paths(paths, title, n_paths):
	
	alpha = 0.7

	for i in range(min(n_paths, paths.shape[0])):
		plt.plot(paths[i], alpha)
	plt.title(title)
	plt.xlabel("Time Steps")
	plt.ylabel("Asset Price")
	plt.grid(TRUE)
	plt.show()
	
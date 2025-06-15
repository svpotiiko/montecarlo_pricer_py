
import matplotlib.pyplot as plt

def plot_paths(paths, title, n_paths_to_plot=50):
    alpha = 0.7
    for i in range(min(n_paths_to_plot, paths.shape[0])):
        plt.plot(paths[i], alpha=alpha)
    plt.title(title)
    plt.xlabel("Time Steps")
    plt.ylabel("Asset Price")
    plt.grid(True)
    plt.show()
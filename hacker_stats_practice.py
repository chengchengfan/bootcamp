import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def draw_bs_reps(data, func, size=1):
    """
    Function to generate bootstrap replicates.
    """
    replicate = np.empty(size)
    n = len(data)


    for i in range(size):
        bs_sample = np.random.choice(data, replace=True, size=len(data))
        replicate = func(bs_sample)

    return replicate


def ecdf(data):
    """
    Compute x, y values for an empirical distribution function.
    """
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# loading in data
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

x_1975, y_1975 = ecdf(bd_1975)
# plt.plot(x_1975, y_1975, marker='.', linestyle='none', color='blue')
for _ in range(100):
    bs_sample = np.random.choice(bd_1975, len(bd_1975))
    x_1975, y_1975 = ecdf(bd_1975)
    plt.plot(x_1975, y_1975, marker='.', linestyle='none', color='blue', alpha=0.02)
# plt.show()

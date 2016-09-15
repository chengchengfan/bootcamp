import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

# Setting matplotlip and seaborn parameters
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.labelsize' : 18}
sns.set(rc=rc)

x = np.random.random(size=100000)

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

x_ecdf, y_ecdf = ecdf(x)


x = np.random.random(size=20)
heads = x <= 0.5


np.random.randint(0, 96, size=20) # gives repeats, use choice
np.random.choice(np.arange(96), size=20, replace=False)

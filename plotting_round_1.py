import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set matplotlip rc parms
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.labelsize' : 18}
sns.set(rc=rc)

# Load the food data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Make the bin boundaries
low_min = np.min(xa_low)
low_max = np.max(xa_low)
high_min = np.min(xa_high)
high_max = np.max(xa_high)
global_min = np.min([low_min, high_min])
global_max = np.max([low_max, high_max])

bins = np.arange(global_min-50, global_max+50, 50)
#
# # plot the data as a histogram
# _ = plt.hist((xa_low, xa_high), bins=bins)
# plt.xlabel('Cross-sectional area (µm$^2$)')
# plt.ylabel('count')
# plt.show()
# plt.close()

# plot the data as two overlaid histogram
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('frequency')
plt.legend(('low concentration', 'high concentration'), loc='upper right')
# plt.show()

# Save the figure, figures could also be saved as .pdf
plt.savefig('egg_area_histograms.svg', bbox_inches='tight')

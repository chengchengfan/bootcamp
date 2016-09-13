# Lesson 23, practice 1, 2,
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
# import bootcamp_utils

# set matplotlip rc parms
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.labelsize' : 18}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

# Slicing out iptg and gfp
sem = data_txt[:,2]
iptg = data_txt[:,0]
gfp = data_txt[:,1]

# Plot iptg vs gfp
plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.title('IPTG Titration - semilog X w/ ErrorBars')
plt.ylim(-0.02, 1.02)
plt.xlim(8e-4, 15)
plt.xscale('log')
plt.show()

# # # Plot iptg vs gfp
# plt.semilogx(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - semilog X')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()


# # Plot iptg vs gfp
# plt.semilogy(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - semilog Y')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()

# # Plot iptg vs gfp
# plt.loglog(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration - log-log')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()

# Practice exercise 3

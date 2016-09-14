# Exercise 3

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

# Setting matplotlip and seaborn parameters
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.labelsize' : 18}
sns.set(rc=rc)

# Data import
data_wt = np.loadtxt('data/wt_lac.csv', comments='#', skiprows=3, delimiter=',')
data_qa = np.loadtxt('data/q18a_lac.csv', comments='#', skiprows=3, delimiter=',')
data_qm = np.loadtxt('data/q18m_lac.csv', comments='#', skiprows=3, delimiter=',')

wt_conc = data_wt[:,0]
wt_fold = data_wt[:,1]
qa_conc = data_qa[:,0]
qa_fold = data_qa[:,1]
qm_conc = data_qm[:,0]
qm_fold = data_qm[:,1]

# Plotting the functions
# x = np.linspace(1e-6, 100)
plt.plot(wt_conc, wt_fold, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(qa_conc, qa_fold, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(qm_conc, qm_fold, marker='.', linestyle='none', markersize=20, alpha=0.5)
# data_wt = scipy.stats.norm.data_wt(x, loc=np.mean(data_wt), scale=np.std(data_wt))
# data_qa = scipy.stats.norm.data_qa(x, loc=np.mean(data_qa), scale=np.std(data_qa))
# data_qm = scipy.stats.norm.data_qm(x, loc=np.mean(data_qm), scale=np.std(data_qm))
# plt.plot(x, data_wt, color='gray')
# plt.plot(x, data_qa, color='gray')
# plt.plot(x, data_qm, color='gray')
# plt.title('IPTG vs. Fold Change')
# plt.xlabel('[IPTG](mM)')
# plt.ylabel('Fold Change')
# plt.xscale('log')
# plt.legend(('WT', 'Q18A','Q18M'), loc='lower right')
# plt.show()

# Function to call the fold change
def conc_to_fold(c):
    """
    Calculating the fold changes for wt.
    """

    Kda = 0.017
    KdI = 0.002
    Kswitch = 5.8
    RK_wt = 141.5
    RK_qa = 16.56
    RK_qm = 1328
    # c = np.array([data_wt[:,0], data_qa[:,0], data_qm[:,0]])

    # WT fold change
    fold_change_wt = (1 + RK_wt * ((1 + wt_conc / Kda)**2)/
                     ((1 + wt_conc / Kda)**2 + Kswitch * ((1 + wt_conc / KdI) **2))) **-1

    # QA fold change
    fold_change_qa = (1 + RK_qa * ((1 + qa_conc / Kda)**2)/
                 ((1 + qa_conc / Kda)**2 + Kswitch * ((1 + qa_conc / KdI) **2))) **-1

    # QM fold change
    fold_change_qm = (1 + RK_qm * ((1 + qm_conc / Kda)**2)/
                 ((1 + qm_conc / Kda)**2 + Kswitch * ((1 + qm_conc / KdI) **2))) **-1

    # return fold_change_wt, fold_change_qa, fold_change_qm


# Making a smooth curve for theoretical fold change
Kda = 0.017
KdI = 0.002
Kswitch = 5.8
RK_wt = 141.5
RK_qa = 16.56
RK_qm = 1328
# c = np.array([data_wt[:,0], data_qa[:,0], data_qm[:,0]])

# WT fold change
fold_change_wt = (1 + RK_wt * ((1 + wt_conc / Kda)**2)/
                 ((1 + wt_conc / Kda)**2 + Kswitch * ((1 + wt_conc / KdI) **2))) **-1

# QA fold change
fold_change_qa = (1 + RK_qa * ((1 + qa_conc / Kda)**2)/
             ((1 + qa_conc / Kda)**2 + Kswitch * ((1 + qa_conc / KdI) **2))) **-1

# QM fold change
fold_change_qm = (1 + RK_qm * ((1 + qm_conc / Kda)**2)/
             ((1 + qm_conc / Kda)**2 + Kswitch * ((1 + qm_conc / KdI) **2))) **-1

# x_wt = np.logspace(-5.5, 2.1, 500)
# x_qa = np.logspace(-5.5, 2.1, 500)
# x_qm = np.logspace(-5.5, 2.1, 500)
# cdf_wt= scipy.stats.norm.cdf(x_wt, loc=np.mean(wt_conc), scale=np.std(wt_conc))
# cdf_qa = scipy.stats.norm.cdf(x_qa, loc=np.mean(qa_conc), scale=np.std(qa_conc))
# cdf_qm = scipy.stats.norm.cdf(x_qm, loc=np.mean(qm_conc), scale=np.std(qm_conc))
# plt.plot(wt_conc, fold_change_wt, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.plot(qa_conc, fold_change_qa, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.plot(qm_conc, fold_change_qm, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.plot(x_wt, cdf_wt, color='gray',)
# plt.plot(x_qa, cdf_qa, color='gray')
# plt.plot(x_qm, cdf_qm, color='gray')
# plt.title('IPTG vs. Fold Change')
# plt.xlabel('[IPTG](mM)')
# plt.ylabel('Fold Change')
# plt.xscale('log')
# plt.yscale('log')
plt.legend(('WT', 'Q18A','Q18M', 'T_WT', 'T_Q18A', 'T_Q18M'), loc='upper left')
# plt.show()


# bohr parameters function generation
def fold_change_bohr(bohr):
    """
    Calculating fold change with Bohr function.
    """
    Kda = 0.017
    KdI = 0.002
    Kswitch = 5.8

    fold_change_bohr_wt = (- np.log(bohr) - np.log(((1 + wt_conc / Kda)**2)/
                        ((1 + wt_conc / Kda)**2 + Kswitch * ((1 + wt_conc / KdI) **2))) **-1
    fold_change_bohr_qa = (- np.log(bohr) - np.log(((1 + qa_conc / Kda)**2)/
                        ((1 + qa_conc / Kda)**2 + Kswitch * ((1 + qa_conc / KdI) **2))) **-1
    fold_change_bohr_qm = (- np.log(bohr) - np.log(((1 + qm_conc / Kda)**2)/
                        ((1 + qm_conc / Kda)**2 + Kswitch * ((1 + qm_conc / KdI) **2))) **-1

    return fold_change_bohr_wt, fold_change_bohr_qa, fold_change_bohr_qm



# generate valuse and run function
Kda = 0.017
KdI = 0.002
Kswitch = 5.8


#return fold_change_bohr_wt, fold_change_bohr_qa, fold_change_bohr_qm
# bohr = np.linspace(-6, 6)
bohr_wt = np.logspace(-6, 6, 500)
bohr_qa = np.logspace(-6, 6, 500)
bohr_qm = np.logspace(-6, 6, 500)
fold_change_bohr_wt = (- np.log(bohr_wt) - np.log(((1 + wt_conc / Kda)**2)/
                     ((1 + wt_conc / Kda) **2 + Kswitch * ((1 + wt_conc / KdI) **2)))**-1
#
fold_change_bohr_qa = (- np.log(bohr_qa) - np.log(((1 + qa_conc / Kda)**2)/
                     ((1 + qa_conc / Kda) **2 + Kswitch * ((1 + qa_conc / KdI) **2)))**-1
#
fold_change_bohr_qm = (- np.log(bohr_qm) - np.log(((1 + qm_conc / Kda)**2)/
                     ((1 + qm_conc / Kda) **2 + Kswitch * ((1 + qm_conc / KdI) **2)))**-1
#
# return fold_change_bohr_wt, fold_change_bohr_qa, fold_change_bohr_qm


cdf_bwt= scipy.stats.norm.cdf(x, loc=np.mean(wt_conc), scale=np.std(wt_conc))
cdf_bqa = scipy.stats.norm.cdf(x, loc=np.mean(qa_conc), scale=np.std(qa_conc))
cdf_bqm = scipy.stats.norm.cdf(x, loc=np.mean(qm_conc), scale=np.std(qm_conc))
plt.plot(bohr_wt, fold_change_bohr_wt, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(bohr_qa, fold_change_bohr_qa, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(bohr_qm, fold_change_bohr_qm, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(x, cdf_bwt, color='gray',)
plt.plot(x, cdf_bqa, color='gray')
plt.plot(x, cdf_bqm, color='gray')
plt.show()
# plt.title('IPTG vs. Fold Change')
# plt.xlabel('[IPTG](mM)')
# plt.ylabel('Fold Change')
# plt.xscale('log')
# plt.yscale('log')

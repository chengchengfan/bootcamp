import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()

# 4.1a loading data
df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

# 4.1b
df_1973 = df_1973.drop('yearband', 1)
df_1973['year'] = 1973
df_1973 = df_1973.rename(columns={'beak length': 'beak length (mm)',
                                  'beak depth': 'beak depth (mm)'})
# print(df_1973)

df_1975['year'] = 1975
df_1975 = df_1975.rename(columns={'Beak length, mm': 'beak length (mm)',
                                  'Beak depth, mm': 'beak depth (mm)'})
# print(df_1975)

df_1987['year'] = 1987
df_1987 = df_1987.rename(columns={'Beak length, mm': 'beak length (mm)',
                                  'Beak depth, mm': 'beak depth (mm)'})
# print(df_1987)

df_1991['year'] = 1991
df_1991 = df_1991.rename(columns={'blength': 'beak length (mm)',
                                  'bdepth': 'beak depth (mm)'})
# print(df_1991)

df_2012['year'] = 2012
df_2012 = df_2012.rename(columns={'blength': 'beak length (mm)',
                                  'bdepth': 'beak depth (mm)'})
# print(df_2012)


# Data concatenations
# df_all = pd.concat((df_1973, df_1975, df_1987, df_1991, df_2012), axis=0, ignore_index=True)
# df_all.to_csv('grant_all.csv')

# 4.1c

df_1973_dd = df_1973.drop_duplicates(subset='band')
df_1975_dd = df_1975.drop_duplicates(subset='band')
df_1987_dd = df_1987.drop_duplicates(subset='band')
df_1991_dd = df_1991.drop_duplicates(subset='band')
df_2012_dd = df_2012.drop_duplicates(subset='band')

# Data concatenations
df_all_dd = pd.concat((df_1973_dd, df_1975_dd, df_1987_dd, df_1991_dd, df_2012_dd),
                        axis=0, ignore_index=True)
# df_all_dd.to_csv('grant_all_dd.csv')



# 4.1d
def ecdf(data):
    """
    Compute x, y values for an empirical distribution function.
    """
    return np.sort(data), np.arange(1, len(data)+1) / len(data)


# beak depth
x_1987_bdf, y_1987_bdf = ecdf(df_1987_dd.loc[df_1987_dd['species'] == 'fortis', ['beak depth (mm)']])
x_1987_bds, y_1987_bds = ecdf(df_1987_dd.loc[df_1987_dd['species'] == 'scandens',['beak depth (mm)']])

plt.plot(x_1987_bdf, y_1987_bdf, marker='.', linestyle='none', markersize=7, alpha=0.5, color='blue')
plt.plot(x_1987_bds, y_1987_bds, marker='.', linestyle='none', markersize=7, alpha=0.5, color='green')

plt.xlabel('Beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
plt.show()

#beak length
x_1987_blf, y_1987_blf = ecdf(df_1987_dd.loc[df_1987_dd['species'] == 'fortis', ['beak length (mm)']])
x_1987_bls, y_1987_bls = ecdf(df_1987_dd.loc[df_1987_dd['species'] == 'scandens',['beak length (mm)']])

plt.plot(x_1987_blf, y_1987_blf, marker='.', linestyle='none', markersize=8, alpha=0.5, color='red')
plt.plot(x_1987_bls, y_1987_bls, marker='.', linestyle='none', markersize=8, alpha=0.5, color='orange')

plt.xlabel('Beak length (mm)')
plt.ylabel('ECDF')
plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
plt.show()

# 4.1e
x_1987_bdf = df_1987_dd.loc[df_1987_dd['species'] == 'fortis',['beak depth (mm)']]
y_1987_blf = df_1987_dd.loc[df_1987_dd['species'] == 'fortis',['beak length (mm)']]
plt.plot(x_1987_bdf, y_1987_blf, marker='.', linestyle='none', markersize=8, alpha=0.5, color='blue')

x_1987_bds = df_1987_dd.loc[df_1987_dd['species'] == 'scandens',['beak depth (mm)']]
y_1987_bls = df_1987_dd.loc[df_1987_dd['species'] == 'scandens',['beak length (mm)']]
plt.plot(x_1987_bds, y_1987_bls, marker='.', linestyle='none', markersize=8, alpha=0.5, color='red')

plt.xlabel('Beak depth (mm)')
plt.ylabel('Beak length (mm)')
plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
plt.show()

# 4.1f
# 1973
x_1973_bdf = df_1973_dd.loc[df_1973_dd['species'] == 'fortis',['beak depth (mm)']]
y_1973_blf = df_1973_dd.loc[df_1973_dd['species'] == 'fortis',['beak length (mm)']]
plt.plot(x_1973_bdf, y_1973_blf, marker='.', linestyle='none', markersize=8, alpha=0.5, color='blue')

x_1973_bds = df_1973_dd.loc[df_1973_dd['species'] == 'scandens',['beak depth (mm)']]
y_1973_bls = df_1973_dd.loc[df_1973_dd['species'] == 'scandens',['beak length (mm)']]
plt.plot(x_1973_bds, y_1973_bls, marker='.', linestyle='none', markersize=8, alpha=0.5, color='red')

plt.xlabel('Beak depth (mm)')
plt.ylabel('Beak length (mm)')
plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
plt.show()

# 1975
x_1975_bdf = df_1975_dd.loc[df_1975_dd['species'] == 'fortis',['beak depth (mm)']]
y_1975_blf = df_1975_dd.loc[df_1975_dd['species'] == 'fortis',['beak length (mm)']]
plt.plot(x_1975_bdf, y_1975_blf, marker='.', linestyle='none', markersize=8, alpha=0.5, color='blue')

x_1975_bds = df_1975_dd.loc[df_1975_dd['species'] == 'scandens',['beak depth (mm)']]
y_1975_bls = df_1975_dd.loc[df_1975_dd['species'] == 'scandens',['beak length (mm)']]
plt.plot(x_1975_bds, y_1975_bls, marker='.', linestyle='none', markersize=8, alpha=0.5, color='red')

plt.xlabel('Beak depth (mm)')
plt.ylabel('Beak length (mm)')
plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
plt.show()

# 1991
x_1991_bdf = df_1991_dd.loc[df_1991_dd['species'] == 'fortis',['beak depth (mm)']]
y_1991_blf = df_1991_dd.loc[df_1991_dd['species'] == 'fortis',['beak length (mm)']]
plt.plot(x_1991_bdf, y_1991_blf, marker='.', linestyle='none', markersize=8, alpha=0.5, color='blue')

x_1991_bds = df_1991_dd.loc[df_1991_dd['species'] == 'scandens',['beak depth (mm)']]
y_1991_bls = df_1991_dd.loc[df_1991_dd['species'] == 'scandens',['beak length (mm)']]
plt.plot(x_1991_bds, y_1991_bls, marker='.', linestyle='none', markersize=8, alpha=0.5, color='red')

plt.xlabel('Beak depth (mm)')
plt.ylabel('Beak length (mm)')
plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
plt.show()

# 2012
x_2012_bdf = df_2012_dd.loc[df_2012_dd['species'] == 'fortis',['beak depth (mm)']]
y_2012_blf = df_2012_dd.loc[df_2012_dd['species'] == 'fortis',['beak length (mm)']]
plt.plot(x_2012_bdf, y_2012_blf, marker='.', linestyle='none', markersize=8, alpha=0.5, color='blue')

x_2012_bds = df_2012_dd.loc[df_2012_dd['species'] == 'scandens',['beak depth (mm)']]
y_2012_bls = df_2012_dd.loc[df_2012_dd['species'] == 'scandens',['beak length (mm)']]
plt.plot(x_2012_bds, y_2012_bls, marker='.', linestyle='none', markersize=8, alpha=0.5, color='red')

plt.xlabel('Beak depth (mm)')
plt.ylabel('Beak length (mm)')
plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
plt.show()

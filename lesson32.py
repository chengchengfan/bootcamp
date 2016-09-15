#Lesson32 practices
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()

# Practice 1

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

#a
df_2000 = df.loc[df['adhesive strength (Pa)'] <= -2000, ['impact time (ms)']]

#b
df_II = df.loc[df['ID']=='II', ['impact force (mN)', 'adhesive force (mN)']]

#c
df_III = df.loc[df['ID']=='III', ['impact force (mN)', 'adhesive force (mN)']]

df_IV = df.loc[df['ID']=='IV', ['impact force (mN)', 'adhesive force (mN)']]

df_III_IV = pd.concat((df_III, df_IV), axis=0)
    # could also be written with an "or" sign
df_34 = df.loc[(df['ID'] == 'III') | (df['ID']== 'IV'), ['impact force (mN)', 'adhesive force (mN)']]


# Practice 2
# 1
df_I = df.loc[df['ID']=='I', ['impact force (mN)', 'adhesive force (mN)']]
I_mean = np.mean(df_I.loc[df['ID']=='I', ['impact force (mN)'])

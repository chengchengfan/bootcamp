import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()

# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Rename impact force column
df = df.rename(columns={'impact force (mN)': 'impf'})

sns.swarmplot(data=df, x='ID', y='impf', hue='date')

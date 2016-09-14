df_tidy = pd.melt(df, var_name='fold density', value_name='cross-sectional area (sq.microm)').dropna()

df_tidy.loc[df_tidy[('fold density')] =='low', :]

df_tidy.loc[(df_tidy['food density']=='low') & (df_tidy['cross-sectional area (sq. micron)'] > 2100), :]

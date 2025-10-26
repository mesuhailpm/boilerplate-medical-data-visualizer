import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3
#Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7 Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: sns.catplot().


    # 8
    #Get the figure for the output and store it in the fig variable.

    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
    #Draw the Heat Map in the draw_heat_map function.

def draw_heat_map():
    # 11
    # Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
#diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
#height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
#height is more than the 97.5th percentile
#weight is less than the 2.5th percentile
#weight is more than the 97.5th percentile

    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12 Calculate the correlation matrix and store it in the corr variable.

    corr = df_heat.corr()

    # 13 Generate a mask for the upper triangle and store it in the mask variable.

    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14 Set up the matplotlib figure.

    fig, ax = plt.subplots(figsize=(12, 10))

    # 15 Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, vmax=.3, vmin=-.1, square=True, cbar_kws={"shrink": .5}, ax=ax)



    # 16
    fig.savefig('heatmap.png')
    return fig

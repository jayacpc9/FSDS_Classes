import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import warnings

warnings.filterwarnings('ignore', category=FutureWarning)

sns_df = sns.load_dataset("tips")


# tips = sns.load_dataset("tips")
# sns.set_theme(style="darkgrid")
# print(tips)

def get_df_coloumns():
    return sns_df.columns.tolist()


print(get_df_coloumns())



def hist_plot(ax,xvals):
    sns.histplot(data=sns_df, x=xvals, bins=20, kde=True, color='blue', ax=ax)
    ax.set_title(f"Histogram {xvals}")


def scatter_plot(ax, xvals, yvals,hue_vals):
    sns.scatterplot(data=sns_df, x=xvals, y=yvals, hue=hue_vals, size="size", palette="deep", ax=ax)
    ax.set_title(f"Scatter plot of {xvals} vs {yvals} and {hue_vals} ")

def box_plot(ax, xvals, yvals,hue_vals):
    sns.boxplot(data=sns_df,  x=xvals, y=yvals, hue=hue_vals, palette='Set2', ax=ax)
    ax.set_title(f"Boxplot of {xvals} by {yvals} and {hue_vals} Status")

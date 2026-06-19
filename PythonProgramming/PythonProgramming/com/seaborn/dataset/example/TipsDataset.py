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


# def scatter_plot(ax):
#     sns.scatterplot(data=sns_df, x="total_bill", y="tip", hue="time", size="size", palette="deep", ax=ax)
#     ax.set_title("Scatter plot of total bill vs tip")


def scatter_plot(ax, xvals, yvals,hue_vals):
    sns.scatterplot(data=sns_df, x=xvals, y=yvals, hue=hue_vals, size="size", palette="deep", ax=ax)
    ax.set_title("Scatter plot of total bill vs tip")

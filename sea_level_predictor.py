import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1. Import data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Line of best fit (1880–latest year)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create years up to 2050
    years_extended = np.arange(df["Year"].min(), 2051)
    sea_level_predicted = res.slope * years_extended + res.intercept

    plt.plot(years_extended, sea_level_predicted, 'r')

    # 4. Line of best fit (2000–latest year)
    df_recent = df[df["Year"] >= 2000]

    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])

    years_recent_extended = np.arange(2000, 2051)
    sea_level_recent_predicted = (
        res_recent.slope * years_recent_extended + res_recent.intercept
    )

    plt.plot(years_recent_extended, sea_level_recent_predicted, 'g')

    # 5. Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.savefig("sea_level_plot.png")
    return plt.gca()
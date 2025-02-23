import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data", color="blue")

    # Line of best fit for full dataset (1880-2050)
    slope1, intercept1, _, _, _ = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = list(range(1880, 2051))
    plt.plot(years_extended, [slope1 * year + intercept1 for year in years_extended], 
             label="Best Fit Line (1880-2050)", color="red")

    # Line of best fit for data from 2000 onwards (2000-2050)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = stats.linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = list(range(2000, 2051))
    plt.plot(years_recent, [slope2 * year + intercept2 for year in years_recent], 
             label="Best Fit Line (2000-2050)", color="green")

    # Labels, title, and legend
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save and show plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()

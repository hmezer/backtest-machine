

# Function that takes pandas dataframe columns and plots the given columns for a small window to peek (or preview) the data
# each column will be plotted in different plots in a figure board
import pandas as pd
import matplotlib.pyplot as plt

def plot_preview(df: pd.DataFrame, columns: list, window: int = 100):
    plt.figure(figsize=(6, 12)) # set figure size
    for col in columns:
        plt.subplot(len(columns), 1, columns.index(col) + 1)
        df[col].head(window).plot()
        plt.title(f"Preview of {col} (first {window} rows)")
        plt.xlabel("Index")
        plt.ylabel("Values")
        plt.legend()
        plt.grid()
    plt.tight_layout()
    plt.show()
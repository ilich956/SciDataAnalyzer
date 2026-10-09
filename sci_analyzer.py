import pandas as pd
import matplotlib.pyplot as plt

class SciDataAnalyzer:
    def __init__(self, data_dict):
        """Initialize with a dictionary of scientific data."""
        self.df = pd.DataFrame(data_dict)

    def calculate_statistics(self, column_name):
        """Calculates basic scientific statistics for a given column."""
        if column_name not in self.df.columns:
            raise ValueError(f"Column '{column_name}' not found in dataset.")
        
        stats = {
            "mean": self.df[column_name].mean(),
            "median": self.df[column_name].median(),
            "std_dev": self.df[column_name].std()
        }
        return stats

    def generate_plot(self, x_col, y_col, output_filename="plot.png"):
        """Generates a scatter plot for visual scientific analysis."""
        plt.figure(figsize=(8, 5))
        plt.scatter(self.df[x_col], self.df[y_col], color='blue', alpha=0.7)
        plt.title(f"Scientific Analysis: {x_col} vs {y_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True)
        plt.savefig(output_filename)
        plt.close()
        return output_filename
# scripts/task2.py
import pandas as pd
import numpy as np

def analyze_data():
    try:
        # Load data from CSV
        iris_df = pd.read_csv('../data/iris.csv')
        
        # Basic statistics
        print("\nBasic statistics:")
        print(iris_df.describe())
        
        # Group by species
        print("\nMean by species:")
        print(iris_df.groupby('species').mean())
        
        # Correlation
        print("\nCorrelation matrix:")
        print(iris_df.corr())
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_data()
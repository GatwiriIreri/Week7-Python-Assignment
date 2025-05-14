# scripts/task3.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data():
    try:
        # Load data
        iris_df = pd.read_csv('../data/iris.csv')
        
        # Set style
        sns.set_style("whitegrid")
        plt.figure(figsize=(15, 10))
        
        # 1. Line chart
        plt.subplot(2, 2, 1)
        plt.plot(iris_df.index, iris_df['sepal length (cm)'], label='Sepal Length')
        plt.plot(iris_df.index, iris_df['petal length (cm)'], label='Petal Length')
        plt.title('Trend of Lengths')
        plt.xlabel('Sample Index')
        plt.ylabel('Length (cm)')
        plt.legend()
        
        # 2. Bar chart
        plt.subplot(2, 2, 2)
        sns.barplot(x='species', y='petal length (cm)', data=iris_df, estimator=np.mean)
        plt.title('Average Petal Length by Species')
        
        # 3. Histogram
        plt.subplot(2, 2, 3)
        sns.histplot(iris_df['sepal width (cm)'], bins=15, kde=True)
        plt.title('Sepal Width Distribution')
        
        # 4. Scatter plot
        plt.subplot(2, 2, 4)
        sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)
        plt.title('Sepal vs Petal Length')
        
        plt.tight_layout()
        plt.savefig('../output/visualizations.png')  # Save the figure
        plt.show()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    visualize_data()
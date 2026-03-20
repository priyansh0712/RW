import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

    def __init__(self):
        self.data = None

    def __del__(self):
        print("🧹 Cleaning up resources...")

    # -------------------------------
    # Load Dataset
    # -------------------------------
    def load_data(self, path):
        try:
            self.data = pd.read_csv(path)
            print("✅ Dataset loaded successfully!")
        except Exception as e:
            print("❌ Error loading dataset:", e)

    # -------------------------------
    # Explore Data
    # -------------------------------
    def explore_data(self):
        if self.data is None:
            print("⚠️ Load dataset first")
            return

        print("\n1. First 5 rows:\n", self.data.head())
        print("\n2. Last 5 rows:\n", self.data.tail())
        print("\n3. Columns:\n", self.data.columns)
        print("\n4. Data Types:\n", self.data.dtypes)
        print("\n5. Info:\n")
        print(self.data.info())

    # -------------------------------
    # Clean Data
    # -------------------------------
    def clean_data(self):
        self.data.drop_duplicates(inplace=True)
        self.data.fillna(0, inplace=True)
        print("✅ Data cleaned")

    # -------------------------------
    # Mathematical Operations
    # -------------------------------
    def mathematical_operations(self):
        if 'Sales' in self.data.columns and 'Profit' in self.data.columns:
            self.data['Profit_Percent'] = (self.data['Profit'] / self.data['Sales']) * 100
            print("✅ Profit percentage added")
        else:
            print("⚠️ Required columns not found")

    # -------------------------------
    # Combine Data
    # -------------------------------
    def combine_data(self, other_df):
        self.data = pd.concat([self.data, other_df])
        print("✅ Data combined")

    # -------------------------------
    # Split Data
    # -------------------------------
    def split_data(self):
        if 'Region' in self.data.columns:
            groups = dict(tuple(self.data.groupby('Region')))
            print("✅ Data split by region")
            return groups
        else:
            print("⚠️ Region column missing")

    # -------------------------------
    # Search, Sort, Filter
    # -------------------------------
    def search_sort_filter(self):
        print("\n1. Search Product")
        print("2. Sort by Sales")
        print("3. Filter by Region")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            print(self.data[self.data['Product'] == name])

        elif choice == '2':
            print(self.data.sort_values(by='Sales', ascending=False))

        elif choice == '3':
            region = input("Enter region: ")
            print(self.data[self.data['Region'] == region])

    # -------------------------------
    # Aggregate Functions
    # -------------------------------
    def aggregate_functions(self):
        print("\nTotal Sales:", self.data['Sales'].sum())
        print("Average Sales:", self.data['Sales'].mean())
        print("Count:", self.data['Sales'].count())

    # -------------------------------
    # Statistical Analysis
    # -------------------------------
    def statistical_analysis(self):
        print(self.data.describe())
        print("\nStandard Deviation:\n", self.data.std(numeric_only=True))
        print("\nVariance:\n", self.data.var(numeric_only=True))

    # -------------------------------
    # Pivot Table
    # -------------------------------
    def create_pivot_table(self):
        pivot = pd.pivot_table(self.data, values='Sales',
                               index='Region', columns='Product',
                               aggfunc='sum')
        print("\nPivot Table:\n", pivot)

    # -------------------------------
    # NumPy Operations
    # -------------------------------
    def numpy_operations(self):
        arr = self.data['Sales'].to_numpy()
        print("Array:", arr)
        print("First 5:", arr[:5])
        print("Mean:", np.mean(arr))

    # -------------------------------
    # Visualization
    # -------------------------------
    def visualize_data(self):

        # Line Plot
        plt.figure()
        plt.plot(self.data['Sales'])
        plt.title("Sales Trend")
        plt.show()

        # Bar Plot
        plt.figure()
        self.data.groupby('Region')['Sales'].sum().plot(kind='bar')
        plt.title("Sales by Region")
        plt.show()

        # Histogram
        plt.figure()
        plt.hist(self.data['Sales'])
        plt.title("Sales Distribution")
        plt.show()

        # Scatter Plot
        if 'Profit' in self.data.columns:
            plt.figure()
            plt.scatter(self.data['Sales'], self.data['Profit'])
            plt.title("Sales vs Profit")
            plt.show()

        # Seaborn Heatmap
        plt.figure()
        sns.heatmap(self.data.corr(numeric_only=True), annot=True)
        plt.title("Correlation Heatmap")
        plt.show()

    # -------------------------------
    # Save Visualization
    # -------------------------------
    def save_visualization(self):
        plt.figure()
        self.data.groupby('Region')['Sales'].sum().plot(kind='bar')
        plt.savefig("sales_chart.png")
        print("✅ Visualization saved as sales_chart.png")


# ================================
# MENU SYSTEM
# ================================
def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========== Data Analysis & Visualization ==========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            path = input("Enter CSV file path: ")
            analyzer.load_data(path)

        elif choice == '2':
            analyzer.explore_data()

        elif choice == '3':
            analyzer.mathematical_operations()
            analyzer.search_sort_filter()
            analyzer.aggregate_functions()
            analyzer.create_pivot_table()
            analyzer.numpy_operations()

        elif choice == '4':
            analyzer.clean_data()

        elif choice == '5':
            analyzer.statistical_analysis()

        elif choice == '6':
            analyzer.visualize_data()

        elif choice == '7':
            analyzer.save_visualization()

        elif choice == '8':
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()

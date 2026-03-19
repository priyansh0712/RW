import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


class FitnessTracker:
    def __init__(self, file_name="fitness_activities.csv"):
        self.file_name = file_name
        try:
            self.df = pd.read_csv(self.file_name)
        except:
            self.df = pd.DataFrame(columns=["Date", "Activity Type", "Duration", "Calories Burned"])

    def save_data(self):
        self.df.to_csv(self.file_name, index=False)

    def log_activity(self, activity_type, duration, calories):
        if duration <= 0 or calories <= 0:
            print("Invalid input! Duration and calories must be positive.")
            return

        new_data = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Activity Type": activity_type,
            "Duration": duration,
            "Calories Burned": calories
        }

        self.df = pd.concat([self.df, pd.DataFrame([new_data])], ignore_index=True)
        self.save_data()
        print("Activity logged successfully.")

    def calculate_metrics(self):
        if self.df.empty:
            print("No data available.")
            return

        total_calories = self.df["Calories Burned"].sum()
        avg_duration = np.mean(self.df["Duration"])
        activity_freq = self.df["Activity Type"].value_counts()

        print("\n--- Metrics ---")
        print("Total Calories Burned:", total_calories)
        print("Average Duration:", avg_duration)
        print("\nActivity Frequency:\n", activity_freq)

    def filter_activities(self, activity_type=None, start_date=None, end_date=None):
        df_filtered = self.df.copy()

        if activity_type:
            df_filtered = df_filtered[df_filtered["Activity Type"] == activity_type]

        if start_date and end_date:
            df_filtered["Date"] = pd.to_datetime(df_filtered["Date"])
            df_filtered = df_filtered[
                (df_filtered["Date"] >= start_date) &
                (df_filtered["Date"] <= end_date)
            ]

        return df_filtered

    def generate_report(self):
        if self.df.empty:
            print("No data to generate report.")
            return

        print("\n--- Report ---")
        print(self.df.describe())

    def add_extra_metrics(self):
        if self.df.empty:
            return

        self.df["Calories per Minute"] = self.df["Calories Burned"] / self.df["Duration"]

    def visualize_data(self):
        if self.df.empty:
            print("No data to visualize.")
            return

        self.add_extra_metrics()

        plt.figure()
        self.df.groupby("Activity Type")["Duration"].sum().plot(kind="bar")
        plt.title("Time Spent per Activity")
        plt.xlabel("Activity Type")
        plt.ylabel("Total Duration")
        plt.show()

        plt.figure()
        df_temp = self.df.copy()
        df_temp["Date"] = pd.to_datetime(df_temp["Date"])
        df_temp.groupby("Date")["Calories Burned"].sum().plot()
        plt.title("Calories Burned Over Time")
        plt.xlabel("Date")
        plt.ylabel("Calories")
        plt.show()

        plt.figure()
        self.df["Activity Type"].value_counts().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Activity Distribution")
        plt.ylabel("")
        plt.show()

        plt.figure()
        corr = self.df[["Duration", "Calories Burned"]].corr()
        sns.heatmap(corr, annot=True)
        plt.title("Correlation Heatmap")
        plt.show()


def main():
    tracker = FitnessTracker()

    while True:
        print("\n1. Log Activity")
        print("2. View Metrics")
        print("3. Filter Activities")
        print("4. Generate Report")
        print("5. Visualize Data")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            activity = input("Enter activity type: ")
            try:
                duration = float(input("Enter duration (minutes): "))
                calories = float(input("Enter calories burned: "))
                tracker.log_activity(activity, duration, calories)
            except:
                print("Invalid input!")

        elif choice == "2":
            tracker.calculate_metrics()

        elif choice == "3":
            activity = input("Enter activity type (or press Enter to skip): ")
            start = input("Start date (YYYY-MM-DD) or press Enter: ")
            end = input("End date (YYYY-MM-DD) or press Enter: ")

            start_date = pd.to_datetime(start) if start else None
            end_date = pd.to_datetime(end) if end else None

            result = tracker.filter_activities(activity or None, start_date, end_date)
            print(result)

        elif choice == "4":
            tracker.generate_report()

        elif choice == "5":
            tracker.visualize_data()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
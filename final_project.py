import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("cowid-covid-data.csv")

df['date'] = pd.to_datetime(df['date'])


df = df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]


df = df.dropna(subset=['location'])

countries = ['India', 'United States', 'Brazil']
df = df[df['location'].isin(countries)]

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='total_cases', hue='location')
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='new_cases', hue='location')
plt.title("Daily New Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['death_rate'] = df['total_deaths'] / df['total_cases']

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='death_rate', hue='location')
plt.title("Death Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Death Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

latest_df = df.sort_values('date').groupby('location').tail(1)

plt.figure(figsize=(8,5))
sns.barplot(data=latest_df, x='location', y='total_cases')
plt.title("Latest Total Cases by Country")
plt.show()

fig = px.line(df, x='date', y='total_cases', color='location',
              title="Interactive COVID-19 Total Cases")
fig.show()

df.to_csv("cleaned_covid_data.csv", index=False)

print("✅ Analysis Completed Successfully!")

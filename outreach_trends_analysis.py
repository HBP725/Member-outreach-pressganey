
import pandas as pd
import matplotlib.pyplot as plt

# Load data
press_ganey = pd.read_csv('press_ganey_mock.csv')
outreach_logs = pd.read_csv('outreach_logs.csv')

# Convert dates
press_ganey['survey_date'] = pd.to_datetime(press_ganey['survey_date'])
outreach_logs['outreach_date'] = pd.to_datetime(outreach_logs['outreach_date'])

# Merge datasets
merged = pd.merge(press_ganey, outreach_logs, on='member_id', how='left')
merged['survey_month'] = merged['survey_date'].dt.to_period("M").astype(str)

# Calculate average rating per month
monthly_ratings = merged.groupby('survey_month')['rating'].mean().reset_index()

# Plot
plt.figure(figsize=(10, 5))
plt.plot(monthly_ratings['survey_month'], monthly_ratings['rating'], marker='o')
plt.title("Average Press Ganey Rating Over Time")
plt.xlabel("Survey Month")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Traffic_Dataset.csv')
df['date_time'] = pd.to_datetime(df['date_time'])

# Plot traffic volume over time
plt.figure(figsize=(12, 6))
plt.plot(df['date_time'], df['traffic_volume'], color='blue', alpha=0.5)
plt.title('Traffic Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Traffic Volume')
plt.tight_layout()
plt.show()



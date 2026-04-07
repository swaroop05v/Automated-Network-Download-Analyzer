# analysis.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("log.csv", names=["timestamp", "size", "time", "speed"])

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["speed_mb"] = df["speed"] 

print("\n===== STATISTICS =====")
print("Average Speed:", df["speed_mb"].mean(), "MB/s")
print("Max Speed:", df["speed_mb"].max(), "MB/s")
print("Min Speed:", df["speed_mb"].min(), "MB/s")

hourly = df.groupby("hour")["speed_mb"].mean()
busiest_hour = hourly.idxmin()

print("Busiest Hour (slowest):", busiest_hour)

# Plot graph
plt.plot(df["timestamp"], df["speed_mb"], marker='o')
plt.xlabel("Time")
plt.ylabel("Speed (MB/s)")
plt.title("Download Speed Over Time")
plt.xticks(rotation=45)
plt.tight_layout()

# Save graph (important for submission)
plt.savefig("speed_graph.png")

plt.show()
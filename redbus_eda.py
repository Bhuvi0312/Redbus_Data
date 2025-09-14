# Redbus Data EDA

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
bus = pd.read_csv("bus_data10.csv")
route = pd.read_csv("route_data10.csv")

# Merge bus + route info
df = pd.merge(bus, route, left_on="bus_no", right_on="route_no", how="left")

print("=== Dataset Overview ===")
print(df.shape)
print(df.info())
print(df.describe())

# 1. Missing values

print("\n=== Missing Values ===")
print(df.isnull().sum())


# 2. Distribution of Price

plt.figure(figsize=(8,5))
sns.histplot(df["price"], bins=50, kde=True)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

# 3. Star Ratings

plt.figure(figsize=(6,4))
sns.countplot(x="star_rating", data=df, palette="viridis")
plt.title("Star Rating Distribution")
plt.show()


# 4. Bus Types
plt.figure(figsize=(10,5))
sns.countplot(y="bus_type", data=df, order=df["bus_type"].value_counts().index, palette="Set2")
plt.title("Bus Type Distribution")
plt.show()

# 5. Seat Availability by Bus Type

plt.figure(figsize=(8,5))
sns.barplot(x="bus_type", y="seat_availability", data=df, estimator=sum, ci=None, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Total Seat Availability by Bus Type")
plt.show()

# 6. Average Price by State

plt.figure(figsize=(10,5))
avg_price_state = df.groupby("state_name")["price"].mean().sort_values(ascending=False)
sns.barplot(x=avg_price_state.index, y=avg_price_state.values, palette="mako")
plt.xticks(rotation=90)
plt.title("Average Price by State")
plt.ylabel("Avg Price")
plt.show()

# 7. Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[["price", "star_rating", "seat_availability"]].corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()

# 8. Top 10 Routes by Seat Availability

top_routes = df.groupby("route_name")["seat_availability"].sum().nlargest(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_routes.values, y=top_routes.index, palette="crest")
plt.title("Top 10 Routes by Seat Availability")
plt.xlabel("Seats Available")
plt.ylabel("Route")
plt.show()
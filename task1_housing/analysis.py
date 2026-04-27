# print("Hello, World!")

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Load the dataset
data = pd.read_csv('housing.csv')
data.rename(columns={'ocean_proximity': 'Ocean_proximity'}, inplace=True)

print("=" * 33)
print("\t Housing Dataset")
print("=" * 33)


# 1.
print("1. How many geographical units?")
unit = len(data)
print(f"Answer: Geographical units = {unit:,}")


# 2.
print("\n2. What is the mean house value among all “Ocean_proximity” categories?")
mean_house_value = data['median_house_value'].mean()
print(f"Answer: Mean house value = {mean_house_value:.2f}")

# 3.
print("\n3. What is the mean house value in each “Ocean_proximity” category?")
mean_by_cat = data.groupby("Ocean_proximity")['median_house_value'].mean().sort_values(ascending=False)
# print(f"Answer: Mean house value = {mean_house_value:.2f}")
print(mean_by_cat.apply(lambda x: f"  ${x:,.2f}").to_string())

# 4.
print("\n4. What can you tell about the differences between the mean and median values?")
diff_stat = data.groupby("Ocean_proximity")['median_house_value'].agg(['mean', 'median'])
diff_stat['difference'] = diff_stat['mean'] - diff_stat['median']
diff_stat.columns = ['Mean', 'Median', 'Difference']
print(diff_stat.map(lambda x: f"${x:,.0f}").to_string())


# 5. and 6.
histogram = ["households", "median_income", "housing_median_age", "median_house_value"]

titles = ["Households", "Median Income", "Housing Median Age", "Median House Value (USD)"]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("5. Histograms of Key Variables", fontsize=15, fontweight="bold")

for ax, col, title in zip(axes.flat, histogram, titles):
    ax.hist(data[col].dropna(), bins=50, color="#1E6AE4", edgecolor="white", linewidth=0.4)
    ax.set_title(title, fontsize=12)
    ax.set_xlabel(title)
    ax.set_ylabel("Frequency")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
    
plt.tight_layout()
plt.savefig("housing_histogram.png", dpi=150, bbox_inches="tight")
plt.close()
print("\n5,6. Histograms saved to housing_histogram.png")

#7
print("\n7. Where is the Most,least expensive and largest,smallest by category?")
# No house size, so total_rooms / households = rooms per household
data["average_rooms"] = data["total_rooms"] / data["households"]
 
house_price = data.groupby("Ocean_proximity")["median_house_value"].mean()
house_size  = data.groupby("Ocean_proximity")["average_rooms"].mean()
 
print(f"\n  Most expensive:  {house_price.idxmax()} (${house_price.max():,.0f})")
print(f"  Least expensive: {house_price.idxmin()} (${house_price.min():,.0f})")
print(f"\n  Largest houses:  {house_size.idxmax()} ({house_size.max():.2f} rooms per household)")
print(f"  Smallest houses: {house_size.idxmin()} ({house_size.min():.2f} rooms per household)")


#8
print("\n8. Quality of houses per category")
data["bedroom_category"] = data["total_bedrooms"] / data["total_rooms"]

house_quality = data.groupby("Ocean_proximity").agg(
    average_house_age = ("housing_median_age", "mean"),
    average_room_household = ("average_rooms", "mean"),
    average_bedroom = ("bedroom_category", "mean")
).round(2)
print(house_quality.to_string())


#9
print("\n9. Demographics per category")

demography = data.groupby("Ocean_proximity").agg(
    mean_population   = ("population",    "mean"),
    mean_households   = ("households",    "mean"),
    mean_income       = ("median_income", "mean"),
    people_per_hh     = ("population",    lambda x: (x / data.loc[x.index, "households"]).mean()),
).round(2)
print(demography.to_string())


#10.
print("\n10. Additional observations")

# Observation 1: Income vs House Value scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(data["median_income"], data["median_house_value"], 
            alpha=0.1, color="#4C72B0")
plt.xlabel("Median Income (scaled)")
plt.ylabel("Median House Value (USD)")
plt.title("10. Income vs House Value")
plt.tight_layout()
plt.savefig("income_vs_value.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nObservation 1: Income vs House Value scatter plot")
print("  Saved at income_vs_value.png")

print(f"\nObservation 2: Missing values per column:")
# print(data.isnull().sum()[data.isnull().sum() > 0])
print("  For Example in total_bedrooms")
print("  Line 292")
print("  Line 343")
print("  Line 540...")

print(f"\nObservation 3: Capped columns:")
print(f"  housing_median_age max:  {data['housing_median_age'].max()}")
print(f"  median_house_value max:  ${data['median_house_value'].max():,.0f}\n")

print("=" * 19)
print(" Analysis complete")
print("=" * 19)
import pandas as pd

# Create Tesla dataset (2008–2030 realistic + forecasted)
years = list(range(2008, 2031))

# Approximate revenue in billions (historical + projections)
revenue = [
    0.015, 0.024, 0.117, 0.204, 0.413, 2.01, 3.2, 4.05, 7.0, 11.8, 21.4, 24.6,
    31.5, 53.8, 81.5, 81.4, 96.8, 100.2, 115.0, 132.0, 150.0, 170.0, 190.0
]

# Approximate car deliveries (in thousands)
deliveries = [
    0.8, 1.2, 2.0, 2.6, 3.1, 22.5, 31.6, 50.1, 76.2, 103.1, 245.2, 367.5,
    499.6, 936.2, 1313.8, 1340.0, 1500.0, 1700.0, 1900.0, 2100.0, 2300.0, 2500.0, 2700.0
]

# Approximate net income in billions (Tesla was negative until ~2019)
net_income = [
    -0.08, -0.12, -0.15, -0.25, -0.39, -0.74, -0.89, -0.89, -0.67, -2.24,
    -0.98, -0.87, 0.72, 3.47, 5.52, 12.6, 10.3, 12.5, 14.0, 16.0, 18.0, 20.0, 22.0
]

# Regional market share (percentages)
regions = {
    "North America": [60, 58, 55, 52, 50, 48, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 36, 36, 36, 36, 36, 36],
    "Europe": [25, 26, 28, 30, 31, 32, 33, 34, 34, 34, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36],
    "Asia": [15, 16, 17, 18, 19, 20, 21, 21, 22, 23, 23, 24, 25, 26, 26, 27, 28, 28, 28, 28, 28, 28, 28]
}

# Build dataframe
data = {
    "Year": years,
    "Revenue_Billion_USD": revenue,
    "Deliveries_Thousands": deliveries,
    "Net_Income_Billion_USD": net_income,
    "NA_Share_%": regions["North America"],
    "EU_Share_%": regions["Europe"],
    "Asia_Share_%": regions["Asia"]
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv("Tesla_Futuristic_Dashboard.csv", index=False)

print("✅ Tesla_Futuristic_Dashboard.csv file created successfully!")

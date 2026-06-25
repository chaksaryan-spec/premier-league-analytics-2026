import pandas as pd

fixtures = pd.read_csv("data/fixtures.csv")

print("Premier League 2026/27 Fixtures")
print("-------------------------------")

print(fixtures.head())

print()

print("Number of fixtures:", len(fixtures))
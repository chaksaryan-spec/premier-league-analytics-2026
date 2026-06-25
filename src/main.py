import pandas as pd

# Football-Data.co.uk Premier League 2025/26
url = "https://www.football-data.co.uk/mmz4281/2526/E0.csv"

fixtures = pd.read_csv(url)

print("First 10 matches")
print(fixtures.head(10))

print()

print("Columns available")
print(fixtures.columns)

print()

print("Total matches:", len(fixtures))
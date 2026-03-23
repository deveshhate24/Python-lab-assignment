import pandas as pd

data = {
    "state": ["Maharashtra", "Gujarat", "Rajasthan", "Karnataka", "Punjab"],
    "area": [307713, 196024, 342239, 191791, 50362],
    "population": [112374333, 60439692, 68548437, 61095297, 27743338]
}

df = pd.DataFrame(data)

print("\nState Information:\n")
print(df)

largest_area = df.loc[df["area"].idxmax()]
print("\nState with Largest Area:", largest_area["state"])

largest_population = df.loc[df["population"].idxmax()]
print("State with Largest Population:", largest_population["state"])

df["density"] = df["population"] / df["area"]

highest_density = df.loc[df["density"].idxmax()]
print("State with Highest Population Density:", highest_density["state"])
import pandas as pd

df = pd.read_csv("books.csv")

print("\nComplete Book Report:\n")
print(df)

author_name = input("\nEnter author name: ")
print("\nBooks by Author:\n")
print(df[df["author"] == author_name])

publisher_name = input("\nEnter publishing house: ")
print("\nBooks by Publisher:\n")
print(df[df["publisher"] == publisher_name])

cheapest = df.loc[df["price"].idxmin()]
costliest = df.loc[df["price"].idxmax()]

print("\nCheapest Book:", cheapest["title"])
print("Costliest Book:", costliest["title"])

print("\nBooks Sorted by Year:\n")
print(df.sort_values(by="year"))
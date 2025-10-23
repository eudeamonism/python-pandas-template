import pandas as pd

# --- Step 1: Define your nested data ---
data = [
    {
        "id": 1,
        "name": "Bret",
        "address": {
            "city": "Houston",
            "counties": ["Harris", "Fort Bend"],
            "geo": {"lat": 29.7, "lng": -95.3}
        }
    },
    {
        "id": 2,
        "name": "Antonette",
        "address": {
            "city": "Austin",
            "counties": ["Travis", "Williamson"],
            "geo": {"lat": 30.3, "lng": -97.7}
        }
    }
]

# --- Step 2: Normalize (flatten) the nested JSON ---
df = pd.json_normalize(data)

# --- Step 3: Examine the resulting structure ---
print("Columns created after normalization:\n", df.columns.tolist(), "\n")
print(df)

# --- Step 4: Expand (explode) the 'address.counties' list to multiple rows ---
df = df.explode("address.counties").reset_index(drop=True)

# --- Step 5: Rename for readability ---
df = df.rename(
    columns={
        "address.city": "city",
        "address.counties": "county",
        "address.geo.lat": "lat",
        "address.geo.lng": "lng"
    }
)

# --- Step 6: Display the final clean table ---
print("\nFlattened and exploded DataFrame:\n")
print(df)

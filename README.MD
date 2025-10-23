# API to Excel Automation (JSONPlaceholder Demo)

## Overview

This projects demonstrates a simple Python automation pipeline that:

- Fetches JSON data from a public API.
- Flattens nested data into tabular form using Pandas
- Exports clean, readable results into Excel using OpenPyXL

### Housekeeping

For setting up the Python environment, see
[Setup](setup_guide)

## Main Steps

### Make API Request

Uses `requests.get()` to fetch data from

```python
https://jsonplaceholder.typicode.com/users
```

Includes `r.raise_for_status()` for error handling.

This ensures only successful (200) responses are processed.

create a new variable that jsonifies data, such as `x = r.json()`

### Flatten JSON

Flattens one level down, revealing keys as headers

```python
import pandas as pd

...
pd.json_normalize(json_data)
```

## Rename Columns

Nested columns are dot notated, like `address.city`

Select columns you want you want only

```python

df = df[["id", "name", "username", "address.city", "company.name"]]
```

Notice the two dot notated columns.

next either chain method or just

```python
df = df.rename(columns={
    "address.city": "city",
    "company.name": "company
    })
```

## Ensure Output Folder Exists

```python
os.makedirs("output", exist_ok=True)
```

## Write to Excel

```python
from openpyxl.utils.dataframe import dataframe_to_rows

wb = px.Workbook()
ws = wb.active
ws.title = "Users"

for row in dataframe_to_rows(df, index=False, header=True):
    ws.append(row)

wb.save("output/users_openpyxl.xlsx")
```

💡 Why dataframe_to_rows()?

Pandas is column-oriented; OpenPyXL writes by rows.

`dataframe_to_rows()` bridges this difference — it converts your column-based DataFrame into a sequence of rows that Excel can append.

Each iteration passes one row list ([id, name, username, city, ...]) into the worksheet.

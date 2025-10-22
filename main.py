import os
import requests
import pandas as pd
import openpyxl as px
from openpyxl.utils.dataframe import dataframe_to_rows

api_url = "https://jsonplaceholder.typicode.com/"

def get_user_information():
    r = requests.get(api_url + "users")
    r.raise_for_status()
    users_json = r.json()

    # 1) Flatten nested dicts
    df = pd.json_normalize(users_json)

    # 2) Keep only scalar, readable columns
    df = df[[
        "id", "name", "username", "email",
        "address.city", "phone", "website", "company.name"
    ]].rename(columns={
        "address.city": "city",
        "company.name": "company"
    })

    # 3) Ensure output dir exists
    os.makedirs("output", exist_ok=True)

    # 4) Write via openpyxl
    wb = px.Workbook()
    ws = wb.active
    ws.title = "Users"

    for row in dataframe_to_rows(df, index=False, header=True):
        ws.append(row)

    wb.save("output/users_openpyxl.xlsx")
    print("✅ Wrote output/users_openpyxl.xlsx")

    # Diagnostics
    print("\nColumns:", df.columns.tolist())
    print("\nUsernames:", df["username"].tolist())

get_user_information()

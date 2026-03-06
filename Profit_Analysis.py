import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Sales": [1200, 150, 300]
}

df = pd.DataFrame(data)

print("Sales Data")
print(df)

total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)
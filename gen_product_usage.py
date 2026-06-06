import pandas as pd
import numpy as np

np.random.seed(42)

# Load customers
customers = pd.read_csv("customers.csv")

# Monthly dates
dates = pd.date_range(
    start="2023-01-01",
    end="2025-12-01",
    freq="MS"
)

usage_records = []

for _, customer in customers.iterrows():

    customer_id = customer["customer_id"]
    plan = customer["plan"]

    for date in dates:

        # Usage depends on plan
        if plan == "Basic":
            logins = np.random.randint(20, 100)
            sessions = np.random.randint(50, 300)
            feature_usage_score = np.random.randint(30, 70)

        elif plan == "Pro":
            logins = np.random.randint(100, 300)
            sessions = np.random.randint(300, 800)
            feature_usage_score = np.random.randint(60, 90)

        else:  # Enterprise
            logins = np.random.randint(300, 1000)
            sessions = np.random.randint(1000, 5000)
            feature_usage_score = np.random.randint(80, 100)

        support_tickets = np.random.poisson(2)

        usage_records.append([
            date,
            customer_id,
            logins,
            sessions,
            feature_usage_score,
            support_tickets
        ])

product_usage = pd.DataFrame(
    usage_records,
    columns=[
        "date",
        "customer_id",
        "logins",
        "sessions",
        "feature_usage_score",
        "support_tickets"
    ]
)

product_usage.to_csv(
    "product_usage.csv",
    index=False
)

print(product_usage.head())
print(f"Rows: {len(product_usage):,}")
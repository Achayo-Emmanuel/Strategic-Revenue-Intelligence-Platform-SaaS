import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Load customers
customers = pd.read_csv("customers.csv")

# Monthly dates
dates = pd.date_range(
    start="2023-01-01",
    end="2025-12-01",
    freq="MS"
)

revenue_records = []

for _, customer in customers.iterrows():

    customer_id = customer["customer_id"]
    plan = customer["plan"]
    status = customer["account_status"]

    # Base MRR by plan
    if plan == "Basic":
        base_mrr = np.random.randint(200, 1000)
    elif plan == "Pro":
        base_mrr = np.random.randint(1000, 5000)
    else:
        base_mrr = np.random.randint(5000, 25000)

    current_mrr = base_mrr

    # Random churn month if customer churned
    churn_month = None
    if status == "Churned":
        churn_month = np.random.choice(dates)

    for date in dates:

        # Stop revenue after churn
        if churn_month is not None and date >= churn_month:
            revenue_records.append([
                date,
                customer_id,
                0,
                0,
                0,
                1
            ])
            continue

        # Expansion revenue (upsell)
        expansion_revenue = 0
        if np.random.rand() < 0.05:
            expansion_revenue = round(current_mrr * np.random.uniform(0.05, 0.20), 2)

        # Contraction revenue (downgrade)
        contraction_revenue = 0
        if np.random.rand() < 0.03:
            contraction_revenue = round(current_mrr * np.random.uniform(0.05, 0.15), 2)

        current_mrr = current_mrr + expansion_revenue - contraction_revenue

        revenue_records.append([
            date,
            customer_id,
            round(current_mrr, 2),
            expansion_revenue,
            contraction_revenue,
            0
        ])

revenue = pd.DataFrame(
    revenue_records,
    columns=[
        "date",
        "customer_id",
        "mrr",
        "expansion_revenue",
        "contraction_revenue",
        "churn_flag"
    ]
)

revenue.to_csv("revenue.csv", index=False)

print(revenue.head())
print(f"Rows: {len(revenue):,}")
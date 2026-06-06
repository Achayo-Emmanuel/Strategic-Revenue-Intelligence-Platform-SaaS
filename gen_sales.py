import pandas as pd
import numpy as np

np.random.seed(42)

n_opportunities = 10000

sales_reps = [
    f"Sales Rep {i}"
    for i in range(1, 51)
]

industries = [
    "Healthcare",
    "Financial Services",
    "Retail",
    "Technology",
    "Manufacturing"
]

stages = [
    "Prospecting",
    "Qualified",
    "Proposal",
    "Negotiation",
    "Closed Won",
    "Closed Lost"
]

created_dates = pd.to_datetime(
    np.random.choice(
        pd.date_range("2023-01-01", "2025-12-31"),
        n_opportunities
    )
)

sales = pd.DataFrame({
    "opportunity_id": [
        f"OPP{i:05d}"
        for i in range(1, n_opportunities + 1)
    ],
    "sales_rep": np.random.choice(sales_reps, n_opportunities),
    "industry": np.random.choice(industries, n_opportunities),
    "deal_size": np.random.randint(
        5000,
        150000,
        n_opportunities
    ),
    "stage": np.random.choice(
        stages,
        n_opportunities,
        p=[0.20, 0.20, 0.20, 0.15, 0.15, 0.10]
    ),
    "created_date": created_dates
})

sales["close_date"] = (
    sales["created_date"] +
    pd.to_timedelta(
        np.random.randint(15, 120, n_opportunities),
        unit="D"
    )
)

sales.to_csv(
    "sales_pipeline.csv",
    index=False
)

print(sales.head())
print(f"Rows: {len(sales):,}")
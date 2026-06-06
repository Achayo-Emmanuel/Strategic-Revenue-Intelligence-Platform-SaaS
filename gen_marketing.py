import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(
    start="2023-01-01",
    end="2025-12-01",
    freq="MS"
)

channels = [
    "Google Ads",
    "LinkedIn",
    "Email",
    "Webinar",
    "Referral"
]

marketing_records = []

for date in dates:
    for channel in channels:

        spend = np.random.randint(5000, 50000)

        leads = int(
            spend * np.random.uniform(0.05, 0.20)
        )

        conversions = int(
            leads * np.random.uniform(0.05, 0.25)
        )

        marketing_records.append([
            date,
            channel,
            spend,
            leads,
            conversions
        ])

marketing = pd.DataFrame(
    marketing_records,
    columns=[
        "date",
        "channel",
        "spend",
        "leads",
        "conversions"
    ]
)

marketing.to_csv(
    "marketing.csv",
    index=False
)

print(marketing.head())
print(f"Rows: {len(marketing):,}")
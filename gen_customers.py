import pandas as pd
import numpy as np

np.random.seed(42)

n_customers = 1000

industries = [
    'Healthcare',
    'Financial Services',
    'Retail',
    'Technology',
    'Manufacturing'
]

regions = [
    'North America',
    'Europe',
    'Asia Pacific'
]

plans = [
    'Basic',
    'Pro',
    'Enterprise'
]

customers = pd.DataFrame({
    'customer_id': [f'CUST{i:04d}' for i in range(1, n_customers + 1)],
    'industry': np.random.choice(industries, n_customers),
    'region': np.random.choice(regions, n_customers),
    'plan': np.random.choice(
        plans,
        n_customers,
        p=[0.5, 0.35, 0.15]
    ),
    'signup_date': pd.to_datetime(
        np.random.choice(
            pd.date_range('2023-01-01', '2025-12-31'),
            n_customers
        )
    )
})

customers['company_name'] = (
    customers['industry'].str.replace(' ', '') +
    '_' +
    customers.index.astype(str)
)

customers['employees'] = np.random.randint(10, 5000, n_customers)

customers['account_status'] = np.random.choice(
    ['Active', 'Churned'],
    n_customers,
    p=[0.9, 0.1]
)

customers.to_csv('customers.csv', index=False)

print(customers.head())
print(f"Rows: {len(customers)}")

print(customers.info())
print(customers['plan'].value_counts())
print(customers['industry'].value_counts())
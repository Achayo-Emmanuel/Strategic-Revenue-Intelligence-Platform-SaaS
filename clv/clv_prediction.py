import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor

df = pd.read_csv("clv_features.csv")

df = pd.get_dummies(
    df,
    columns=["INDUSTRY","REGION","PLAN"],
    drop_first=True
)

X = df.drop(
    columns=["CUSTOMER_ID","LIFETIME_REVENUE"]
)

y = df["LIFETIME_REVENUE"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("R²:", round(r2_score(y_test, predictions),3))

df["predicted_clv"] = model.predict(X)

output = df[
    ["CUSTOMER_ID","predicted_clv"]
]

output.to_csv(
    "predicted_clv.csv",
    index=False
)






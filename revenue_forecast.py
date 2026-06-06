
import pandas as pd
from prophet import Prophet

df = pd.read_csv("monthly_revenue.csv")

df.columns = ["ds", "y"]

model = Prophet()

model.fit(df)

future = model.make_future_dataframe(
    periods=6,
    freq="MS"
)

forecast = model.predict(future)

print(
    forecast[
        ["ds", "yhat", "yhat_lower", "yhat_upper"]
    ].tail(6)
)

forecast.to_csv(
    "revenue_forecast_output.csv",
    index=False
)
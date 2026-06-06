
import pandas as pd
from prophet import Prophet

df = pd.read_csv(
    r"C:\Users\mario\Desktop\EN channel\business_solution\AI-Powered-SaaS-Revenue-Intelligence\forecast\monthly_revenue.csv"
)
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


import matplotlib.pyplot as plt

fig1 = model.plot(forecast)
plt.show()



forecast_output = forecast[
    ["ds", "yhat", "yhat_lower", "yhat_upper"]
].tail(6)

forecast_output.columns = [
    "FORECAST_MONTH",
    "PREDICTED_REVENUE",
    "LOWER_BOUND",
    "UPPER_BOUND"
]

forecast_output.to_csv(
    "forecast_revenue.csv",
    index=False
)
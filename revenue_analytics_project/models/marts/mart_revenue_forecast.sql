WITH actuals AS (

    SELECT
        DATE_TRUNC('MONTH', DATE) AS revenue_month,
        SUM(MRR) AS actual_revenue
    FROM {{ ref('stg_revenue') }}
    GROUP BY 1

)

SELECT
    f.FORECAST_MONTH,
    a.actual_revenue,
    f.PREDICTED_REVENUE,
    f.LOWER_BOUND,
    f.UPPER_BOUND,

    ROUND(
        (f.PREDICTED_REVENUE - a.actual_revenue)
        / NULLIF(a.actual_revenue, 0) * 100,
        2
    ) AS forecast_variance_pct

FROM {{ ref('stg_forecast_revenue') }} f

LEFT JOIN actuals a
    ON f.FORECAST_MONTH = a.revenue_month
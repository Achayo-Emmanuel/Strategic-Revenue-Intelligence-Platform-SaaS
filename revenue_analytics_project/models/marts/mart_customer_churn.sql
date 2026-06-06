SELECT
    c.customer_id,
    c.industry,
    c.region,
    c.plan,
    c.avg_mrr,
    p.churn_probability,

    CASE
        WHEN p.churn_probability >= 0.70 THEN 'High Risk'
        WHEN p.churn_probability >= 0.40 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS risk_level,

    ROUND(c.avg_mrr * p.churn_probability, 2) AS revenue_at_risk

FROM {{ ref('mart_churn_features') }} c

LEFT JOIN {{ ref('stg_predicted_churn') }} p
    ON c.customer_id = p.customer_id
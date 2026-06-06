SELECT

    c.customer_id,

    c.industry,

    c.region,

    c.plan,

    p.predicted_clv,

    ch.churn_probability,

    ch.risk_level,

    ch.revenue_at_risk

FROM {{ ref('mart_churn_features') }} c

LEFT JOIN {{ ref('stg_predicted_clv') }} p
    ON c.customer_id = p.customer_id

LEFT JOIN {{ ref('mart_customer_churn') }} ch
    ON c.customer_id = ch.customer_id
WITH customer_usage AS (

    SELECT
        customer_id,
        AVG(logins) AS avg_logins,
        AVG(sessions) AS avg_sessions
    FROM {{ ref('stg_usage') }}
    GROUP BY customer_id

),

customer_revenue AS (

    SELECT
        customer_id,
        AVG(mrr) AS avg_mrr,
        MAX(churn_flag) AS churn_flag
    FROM {{ ref('stg_revenue') }}
    GROUP BY customer_id

)

SELECT

    c.customer_id,
    c.company_name,
    c.industry,
    c.region,
    c.plan,

    u.avg_logins,
    u.avg_sessions,

    r.avg_mrr,
    r.churn_flag,

    CASE

        WHEN u.avg_logins < 10
             OR u.avg_sessions < 20
        THEN 'High Risk'

        WHEN u.avg_logins < 25
             OR u.avg_sessions < 50
        THEN 'Medium Risk'

        ELSE 'Low Risk'

    END AS customer_risk

FROM {{ ref('stg_customers') }} c

LEFT JOIN customer_usage u
    ON c.customer_id = u.customer_id

LEFT JOIN customer_revenue r
    ON c.customer_id = r.customer_id


-- what this tables answers
-- Which customers are likely to churn?
-- Which segments need retention efforts?
-- Which industries are healthiest?
-- Which customers generate high revenue but have low engagement?
-- High Risk
-- Medium Risk
-- Low Risk
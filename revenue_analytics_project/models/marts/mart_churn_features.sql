WITH usage_metrics AS (

    SELECT

        customer_id,

        AVG(logins) AS avg_logins,

        AVG(sessions) AS avg_sessions,

        AVG(feature_usage_score) AS avg_feature_usage_score,

        AVG(support_tickets) AS avg_support_tickets

    FROM {{ ref('stg_usage') }}

    GROUP BY customer_id

),

revenue_metrics AS (

    SELECT

        customer_id,

        AVG(mrr) AS avg_mrr,

        MAX(churn_flag) AS churn_flag

    FROM {{ ref('stg_revenue') }}

    GROUP BY customer_id

)

SELECT

    c.customer_id,

    c.industry,

    c.region,

    c.plan,

    u.avg_logins,

    u.avg_sessions,

    u.avg_feature_usage_score,

    u.avg_support_tickets,

    r.avg_mrr,

    r.churn_flag

FROM {{ ref('stg_customers') }} c

LEFT JOIN usage_metrics u
    ON c.customer_id = u.customer_id

LEFT JOIN revenue_metrics r
    ON c.customer_id = r.customer_id
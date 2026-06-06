WITH revenue_metrics AS (

    SELECT
        CUSTOMER_ID,
        SUM(MRR) AS lifetime_revenue,
        AVG(MRR) AS avg_mrr,
        MAX(MRR) AS max_mrr,
        COUNT(DISTINCT DATE) AS active_months
    FROM {{ ref('stg_revenue') }}
    GROUP BY CUSTOMER_ID

),

usage_metrics AS (

    SELECT
        CUSTOMER_ID,
        AVG(LOGINS) AS avg_logins,
        AVG(SESSIONS) AS avg_sessions,
        AVG(FEATURE_USAGE_SCORE) AS avg_feature_usage_score,
        AVG(SUPPORT_TICKETS) AS avg_support_tickets
    FROM {{ ref('stg_usage') }}
    GROUP BY CUSTOMER_ID

)

SELECT
    c.CUSTOMER_ID,
    c.INDUSTRY,
    c.REGION,
    c.PLAN,

    r.lifetime_revenue,
    r.avg_mrr,
    r.max_mrr,
    r.active_months,

    u.avg_logins,
    u.avg_sessions,
    u.avg_feature_usage_score,
    u.avg_support_tickets

FROM {{ ref('stg_customers') }} c

LEFT JOIN revenue_metrics r
    ON c.CUSTOMER_ID = r.CUSTOMER_ID

LEFT JOIN usage_metrics u
    ON c.CUSTOMER_ID = u.CUSTOMER_ID
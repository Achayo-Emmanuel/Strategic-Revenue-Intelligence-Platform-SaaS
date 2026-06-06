WITH monthly_revenue AS (

    SELECT

        DATE_TRUNC('MONTH', DATE) AS revenue_month,

        SUM(MRR) AS monthly_revenue

    FROM {{ ref('stg_revenue') }}

    GROUP BY 1

)

SELECT

    revenue_month,

    monthly_revenue,

    LAG(monthly_revenue)
        OVER (ORDER BY revenue_month)
        AS prior_month_revenue,

    ROUND(
        (
            monthly_revenue
            -
            LAG(monthly_revenue)
            OVER (ORDER BY revenue_month)
        )
        /
        NULLIF(
            LAG(monthly_revenue)
            OVER (ORDER BY revenue_month),
            0
        ) * 100,
        2
    ) AS revenue_growth_pct

FROM monthly_revenue

-- Answers: Are we going to hit revenue targets this quarter?
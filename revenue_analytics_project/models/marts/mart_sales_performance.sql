WITH sales_metrics AS (

    SELECT

        SALES_REP,
        INDUSTRY,

        COUNT(DISTINCT OPPORTUNITY_ID) AS total_opportunities,

        SUM(DEAL_SIZE) AS pipeline_value,

        AVG(DEAL_SIZE) AS avg_deal_size,

        SUM(
            CASE
                WHEN STAGE = 'Closed Won'
                THEN DEAL_SIZE
                ELSE 0
            END
        ) AS revenue_generated,

        COUNT(
            CASE
                WHEN STAGE = 'Closed Won'
                THEN 1
            END
        ) AS won_deals

    FROM {{ ref('stg_sales') }}

    GROUP BY
        SALES_REP,
        INDUSTRY

)

SELECT

    SALES_REP,
    INDUSTRY,
    TOTAL_OPPORTUNITIES,
    PIPELINE_VALUE,
    AVG_DEAL_SIZE,
    REVENUE_GENERATED,
    WON_DEALS,

    ROUND(
        WON_DEALS
        /
        NULLIF(TOTAL_OPPORTUNITIES,0)
        * 100,
        2
    ) AS WIN_RATE_PCT

FROM sales_metrics


-- This table answers >
-- Which sales reps drive the most revenue?
-- Who has the highest win rate?
-- Who manages the largest pipeline?
-- What is the average deal size?
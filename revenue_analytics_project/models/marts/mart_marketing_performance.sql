SELECT

    channel,

    SUM(spend) AS total_spend,

    SUM(leads) AS total_leads,

    SUM(conversions) AS total_conversions,

    ROUND(
        SUM(conversions) * 100.0
        / NULLIF(SUM(leads),0),
        2
    ) AS conversion_rate_pct,

    ROUND(
        SUM(spend)
        / NULLIF(SUM(leads),0),
        2
    ) AS cost_per_lead,

    ROUND(
        SUM(spend)
        / NULLIF(SUM(conversions),0),
        2
    ) AS cac

FROM {{ ref('stg_marketing') }}

GROUP BY channel


-- This tables answers:
-- Which channels generate the most leads?
-- Which channels convert best?
-- What is CAC?
-- What is the highest ROI channel?
-- Where should we invest more budget?
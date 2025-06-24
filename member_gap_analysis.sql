
-- member_gap_analysis.sql

-- This query identifies members with a care gap and combines it with their most recent Press Ganey rating
-- and the latest outreach interaction.

SELECT 
    m.member_id,
    m.member_name,
    m.dob,
    m.last_visit_date,
    m.gap_in_care,
    pg.survey_date,
    pg.rating,
    pg.comments,
    o.outreach_date,
    o.outreach_type,
    o.response
FROM 
    member_data m
LEFT JOIN 
    press_ganey_data pg ON m.member_id = pg.member_id
LEFT JOIN 
    outreach_logs o ON m.member_id = o.member_id
WHERE 
    m.gap_in_care = 'Yes'
ORDER BY 
    m.member_id, o.outreach_date DESC, pg.survey_date DESC;

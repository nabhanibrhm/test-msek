-- ================================
-- Average resolution by product
-- ================================
\copy (SELECT product, COUNT(*) AS total_complaints, ROUND(AVG((date_sent_to_company - date_received)),2) AS avg_resolution_days FROM crm_events WHERE date_sent_to_company IS NOT NULL AND date_received IS NOT NULL GROUP BY product ORDER BY avg_resolution_days DESC) TO '/data/avg_by_product.csv' CSV HEADER;

-- ================================
-- Average resolution by server
-- ================================
\copy (SELECT l.server, COUNT(DISTINCT e.complaint_id) AS complaints_handled, ROUND(AVG((e.date_sent_to_company - e.date_received)),2) AS avg_resolution_days FROM crm_events e JOIN crm_call_logs l ON e.complaint_id = l.complaint_id WHERE e.date_sent_to_company IS NOT NULL GROUP BY l.server ORDER BY avg_resolution_days DESC) TO '/data/avg_by_server.csv' CSV HEADER;

-- ================================
-- Monthly trend of resolution time
-- ================================
\copy (SELECT DATE_TRUNC('month', date_received)::date AS month, ROUND(AVG(date_sent_to_company - date_received),2) AS avg_resolution_days FROM crm_events WHERE date_sent_to_company IS NOT NULL AND date_received IS NOT NULL GROUP BY month ORDER BY month) TO '/data/avg_by_month.csv' CSV HEADER;
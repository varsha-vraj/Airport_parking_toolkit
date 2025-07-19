

SELECT
  event_id,
  vehicle_id,
  zone_id,
  entry_time,
  exit_time,
  paid_amount
FROM parking_events
ORDER BY entry_time DESC;


SELECT *
FROM parking_events
WHERE exit_time <= entry_time OR paid_amount < 0;


SELECT
  pz.zone_name,
  SUM(pe.paid_amount) AS total_revenue,
  COUNT(*) AS total_visits
FROM parking_events pe
JOIN parking_zones pz ON pe.zone_id = pz.zone_id
GROUP BY pz.zone_name
ORDER BY total_revenue DESC;


SELECT
  vehicle_id,
  COUNT(*) AS visit_count
FROM parking_events
GROUP BY vehicle_id
ORDER BY visit_count DESC
LIMIT 5;


-- Null vehicle_id or zone_id
SELECT *
FROM parking_events
WHERE vehicle_id IS NULL OR zone_id IS NULL;


SELECT
  pz.is_valet,
  COUNT(*) AS total_visits,
  SUM(pe.paid_amount) AS total_revenue
FROM parking_events pe
JOIN parking_zones pz ON pe.zone_id = pz.zone_id
GROUP BY pz.is_valet;


WITH zone_revenue AS (
  SELECT
    zone_id,
    SUM(paid_amount) AS revenue
  FROM parking_events
  GROUP BY zone_id
)
SELECT *,
       RANK() OVER (ORDER BY revenue DESC) AS revenue_rank
FROM zone_revenue;


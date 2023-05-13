SELECT tbb.group_id as id_group, min(overdue) as min, max(overdue) as max, avg(overdue) as avg FROM (
SELECT group_id, assisgnment_id, count(*) as overdue FROM (
SELECT a.assisgnment_id, date, due_date, group_id FROM 'assignments_grades' ag, 'assignments' a
WHERE a.assisgnment_id = ag.assisgnment_id) as tb
WHERE tb.date <= tb.due_date
GROUP BY tb.assisgnment_id) as tbb
GROUP BY group_id

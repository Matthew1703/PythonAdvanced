SELECT round(min(srr), 4) AS avgg, name FROM (
SELECT AVG(sr) AS srr, t.full_name AS name FROM
    (SELECT AVG(grade) AS sr, assisgnment_id FROM 'assignments_grades' GROUP BY assisgnment_id) AS tb,
    'assignments' a, 'teachers' t
WHERE a.assisgnment_id = tb.assisgnment_id AND t.teacher_id = a.teacher_id
GROUP BY a.teacher_id)


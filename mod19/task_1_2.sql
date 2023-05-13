SELECT avgg, s.full_name FROM
    (SELECT AVG(grade) as avgg, student_id FROM 'assignments_grades' GROUP BY student_id) AS tb,
    'students' s
WHERE s.student_id = tb.student_id
ORDER BY avgg DESC
LIMIT 10

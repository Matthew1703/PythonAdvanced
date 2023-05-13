SELECT full_name FROM students WHERE group_id in (SELECT group_id FROM
(SELECT max(srr), teacher_id as tid FROM
(SELECT AVG(sr) as srr, teacher_id FROM
(SELECT AVG(grade) AS sr, assisgnment_id FROM 'assignments_grades' GROUP BY assisgnment_id) as tb,
'assignments' a
WHERE a.assisgnment_id = tb.assisgnment_id
GROUP BY teacher_id)) as tbb, 'students_groups' sg
WHERE sg.teacher_id = tbb.tid)
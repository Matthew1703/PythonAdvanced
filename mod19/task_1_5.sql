SELECT tb1.group_id, stud_count, tb1.avg, not_submitted, missed_deadline FROM
(SELECT AVG(grade) as avg, group_id FROM assignments_grades ag, assignments a WHERE a.assisgnment_id = ag.assisgnment_id
GROUP BY a.group_id) tb1, (SELECT COUNT(student_id) as stud_count, group_id FROM students s GROUP BY group_id) as tb2,
(SELECT tbb.group_id, (cn - cnt) as not_submitted  FROM (SELECT COUNT(*) as cnt, group_id FROM (SELECT distinct student_id as sid FROM assignments_grades ag, assignments a
WHERE a.assisgnment_id = ag.assisgnment_id) tb, students s
WHERE tb.sid = s.student_id
GROUP BY group_id) tb, (SELECT count(student_id) as cn, group_id FROM  students s GROUP BY group_id) tbb
WHERE tb.group_id = tbb.group_id) as tb3, (SELECT tbb.group_id as id_group, sum(overdue) as missed_deadline FROM (
SELECT group_id, assisgnment_id, count(*) as overdue FROM (
SELECT a.assisgnment_id, date, due_date, group_id FROM 'assignments_grades' ag, 'assignments' a
WHERE a.assisgnment_id = ag.assisgnment_id) as tb
WHERE tb.date <= tb.due_date
GROUP BY tb.assisgnment_id) as tbb
GROUP BY group_id) as tb4
WHERE tb1.group_id = tb2.group_id and tb3.group_id = tb2.group_id and tb4.id_group = tb3.group_id
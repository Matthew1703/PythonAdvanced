SELECT ROUND(AVG(sr), 4) AS avg FROM (SELECT a.assisgnment_id, AVG(grade) as sr, assignment_text FROM assignments a, assignments_grades ag
WHERE a.assisgnment_id = ag.assisgnment_id and exists(SELECT assignment_text FROM assignments_grades WHERE assignment_text like '%прочитать%' or assignment_text like '%выучить%')
GROUP BY a.assisgnment_id)
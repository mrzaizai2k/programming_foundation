SELECT AVG(e.salary) AS avg_salary
FROM employees e
JOIN positions p ON e.id = p.employee_id
WHERE p.position_name = 'Software' AND e.age <=30
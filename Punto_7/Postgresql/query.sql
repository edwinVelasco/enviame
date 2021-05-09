

SELECT e.id, (e.first_name || ' ' || e.last_name) AS name, e.salary, c.name, co.name, co.anual_adjustment adjustment
FROM employees AS e
INNER JOIN countries AS c 
	ON e.country_id = c.id
INNER JOIN continents AS co
	ON c.continent_id = co.id
ORDER BY e.salary;


-- Consulta de actualizacion en PosgreSQL
UPDATE employees as e
SET 
	salary = salary + co.anual_adjustment
FROM countries c, continents co
WHERE e.country_id = c.id AND c.continent_id = co.id AND e.salary <= 5000;
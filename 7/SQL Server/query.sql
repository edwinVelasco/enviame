
--
-- Query
--

-- Consulta de actualizacion en SQL Server
UPDATE e
SET 
	salary = salary + co.anual_adjustment
FROM employees e
	INNER JOIN countries c 
		ON e.country_id = c.id
	INNER JOIN continents co 
		ON c.continent_id = co.id
WHERE salary <= 5000;


SELECT e.id, e.first_name + ' '+ e.last_name AS name , e.salary, c.name, co.name, co.anual_adjustment AS adjustment
FROM employees e
INNER JOIN countries c 
	ON e.country_id = c.id
INNER JOIN continents co
	ON c.continent_id = co.id
ORDER BY e.salary;





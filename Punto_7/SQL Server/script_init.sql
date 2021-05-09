--
-- Create model Continents
--
CREATE TABLE continents (id int IDENTITY(1,1) PRIMARY KEY, name varchar(25) NOT NULL, anual_adjustment integer NOT NULL);
--
-- Create model Contries
--
CREATE TABLE countries (id int IDENTITY(1,1) PRIMARY KEY, name varchar(25) NOT NULL, continent_id integer NOT NULL);
--
-- Create model Employee
--
CREATE TABLE employees (id int  IDENTITY(1,1) PRIMARY KEY, first_name varchar(25) NOT NULL, last_name varchar(25) NOT NULL, salary integer NOT NULL, country_id integer NOT NULL);
--
-- Create data Continents
-- 
INSERT INTO continents (name, anual_adjustment) VALUES ('América', 4);
INSERT INTO continents (name, anual_adjustment) VALUES ('Europa', 5); 
INSERT INTO continents (name, anual_adjustment) VALUES ('Asia', 6); 
INSERT INTO continents (name, anual_adjustment) VALUES ('Oceanía', 6); 
INSERT INTO continents (name, anual_adjustment) VALUES ('Africa', 5);
--
-- Create data Contries
-- 
INSERT INTO countries (continent_id, name) VALUES (1, 'Chile'); 
INSERT INTO countries (continent_id, name) VALUES (1, 'Argentina'); 
INSERT INTO countries (continent_id, name) VALUES (1, 'Canadá'); 
INSERT INTO countries (continent_id, name) VALUES (1, 'Colombia'); 
INSERT INTO countries (continent_id, name) VALUES (2, 'Alemania'); 
INSERT INTO countries (continent_id, name) VALUES (2, 'Francia'); 
INSERT INTO countries (continent_id, name) VALUES (2, 'España'); 
INSERT INTO countries (continent_id, name) VALUES (2, 'Grecia'); 
INSERT INTO countries (continent_id, name) VALUES (3, 'India'); 
INSERT INTO countries (continent_id, name) VALUES (3, 'Japón'); 
INSERT INTO countries (continent_id, name) VALUES (3, 'Corea del Sur'); 
INSERT INTO countries (continent_id, name) VALUES (4, 'Australia');
--
-- Create data Employee
-- 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (1, 'Pedro', 'Rojas', 2000); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (2, 'Luciano', 'Alessandri', 2100); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (3, 'John', 'Carter', 3050); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (4, 'Alejandra', 'Benavides', 2150); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (5, 'Moritz', 'Baring', 6000); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (6, 'Thierry', 'Henry', 5900); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (7, 'Sergio', 'Ramos', 6200); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (8, 'Nikoleta', 'Kyriakopulu', 7000); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (9, 'Aamir', 'Khan', 2000); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (10, 'Takumi', 'Fujiwara', 5000); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (11, 'Heung-min', 'Son', 5100); 
INSERT INTO employees (country_id, first_name, last_name, salary) VALUES (12, 'Peter', 'Johnson', 6100);
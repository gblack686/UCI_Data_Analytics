USE sakila;

SELECT first_name,last_name from actor;

SELECT CONCAT(first_name,  ' ', last_name) AS ' Actor Name'
FROM actor;

SELECT actor_id, first_name, last_name 
FROM actor
WHERE first_name = 'JOE';

-- 2b. Find all actors whose last name contain the letters GEN:
SELECT actor_id, first_name, last_name 
FROM actor
WHERE last_name LIKE '%GEN%';

SELECT actor_id, first_name, last_name 
FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

SELECT country_id,  country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

SELECT * FROM actor;
ALTER TABLE actor
ADD COLUMN  description BLOB(50) AFTER first_name;

ALTER TABLE actor
DROP COLUMN description;

SELECT last_name, COUNT(*) AS `Count`
FROM actor
GROUP BY last_name;

SELECT last_name, COUNT(*) AS `Count`
FROM actor
GROUP BY last_name
HAVING Count > 2;
-- ************ code runs *********** --

UPDATE actor 
SET first_name= 'HARPO'
WHERE first_name='GROUCHO' AND last_name='WILLIAMS';

SELECT first_name FROM actor WHERE last_name = 'WILLIAMS';

DESCRIBE sakila.address

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT s.first_name, s.last_name, a.address
FROM staff s LEFT JOIN address a ON s.address_id = a.address_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT first_name, last_name, SUM(amount)
FROM staff s INNER JOIN payment p ON s.staff_id = p.staff_id
WHERE p.payment_date LIKE '2005-08%' GROUP BY p.staff_id ORDER BY last_name ASC;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT title, COUNT(actor_id) FROM film f INNER JOIN film_actor fa
ON f.film_id = fa.film_id GROUP BY title;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT title, COUNT(inventory_id) FROM film f
INNER JOIN inventory i  ON f.film_id = i.film_id
WHERE title = "Hunchback Impossible";

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
SELECT last_name, first_name, SUM(amount)
FROM payment p INNER JOIN customer c ON p.customer_id = c.customer_id
GROUP BY p.customer_id ORDER BY last_name ASC;

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name, last_name
FROM actor
WHERE actor_id
	IN (SELECT actor_id FROM film_actor WHERE film_id 
		IN (SELECT film_id from film where title='ALONE TRIP'));
        
-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
SELECT country, last_name, first_name, email
FROM country c
LEFT JOIN customer cu
ON c.country_id = cu.customer_id
WHERE country = 'Canada';

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies 
SELECT title, category
FROM film_list
WHERE category = 'Family';

-- 7e. Display the most frequently rented movies in descending order.
SELECT i.film_id, f.title, COUNT(r.inventory_id)
FROM inventory i
INNER JOIN rental r
ON i.inventory_id = r.inventory_id
INNER JOIN film_text f 
ON i.film_id = f.film_id
GROUP BY r.inventory_id
ORDER BY COUNT(r.inventory_id) DESC;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT store.store_id, SUM(amount)
FROM store
INNER JOIN staff
ON store.store_id = staff.store_id
INNER JOIN payment p 
ON p.staff_id = staff.staff_id
GROUP BY store.store_id
ORDER BY SUM(amount);

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT s.store_id, city, country
FROM store s
INNER JOIN customer cu
ON s.store_id = cu.store_id
INNER JOIN staff st
ON s.store_id = st.store_id
INNER JOIN address a
ON cu.address_id = a.address_id
INNER JOIN city ci
ON a.city_id = ci.city_id
INNER JOIN country coun
ON ci.country_id = coun.country_id;

-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)



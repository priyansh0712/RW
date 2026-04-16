-- Active: 1774610285273@@127.0.0.1@3306
CREATE TABLE events (
	event_id INT PRIMARY KEY,
	event_name VARCHAR(100) NOT NULL,
	event_date DATE NOT NULL,
	venue_id INT NOT NULL,
	organizer_id INT NOT NULL,
	ticket_price DECIMAL(10,2) NOT NULL,
	total_seats INT NOT NULL,
	available_seats INT NOT NULL,
	FOREIGN KEY (venue_id) REFERENCES venues(venue_id),
	FOREIGN KEY (organizer_id) REFERENCES organizers(organizer_id)
);


CREATE TABLE venues (
	venue_id INT PRIMARY KEY,
	venue_name VARCHAR(100) NOT NULL,
	location VARCHAR(150) NOT NULL,
	capacity INT NOT NULL
);

CREATE TABLE organizers (
	organizer_id INT PRIMARY KEY,
	organizer_name VARCHAR(100) NOT NULL,
	contact_email VARCHAR(100),
	phone_number VARCHAR(20)
);

CREATE TABLE attendees (
	attendee_id INT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100),
	phone_number VARCHAR(20)
);

CREATE TABLE tickets (
	ticket_id INT PRIMARY KEY,
	event_id INT NOT NULL,
	attendee_id INT NOT NULL,
	booking_date DATE NOT NULL,
	status VARCHAR(20) NOT NULL,
	FOREIGN KEY (event_id) REFERENCES events(event_id),
	FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id)
);

CREATE TABLE payments (
	payment_id INT PRIMARY KEY,
	ticket_id INT NOT NULL,
	amount_paid DECIMAL(10,2) NOT NULL,
	payment_status VARCHAR(20) NOT NULL,
	payment_date DATE NOT NULL,
	FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id)
);

-- 1. CRUD OPERATIONS

INSERT INTO events (event_id, event_name, event_date, venue_id, organizer_id, ticket_price, total_seats, available_seats)
VALUES (1, 'Tech Summit', '2026-12-10', 1, 1, 2500.00, 500, 500);

UPDATE events
SET ticket_price = 2750.00, available_seats = 450
WHERE event_id = 1;

DELETE FROM tickets
WHERE ticket_id = 1;

SELECT e.*
FROM events e
JOIN venues v ON e.venue_id = v.venue_id
WHERE v.location = 'Mumbai';

INSERT INTO venues (venue_id, venue_name, location, capacity)
VALUES (1, 'Expo Center', 'Mumbai', 2000);

UPDATE venues
SET capacity = 2500
WHERE venue_id = 1;

DELETE FROM venues
WHERE venue_id = 99;

SELECT *
FROM venues
WHERE location = 'Mumbai';

INSERT INTO organizers (organizer_id, organizer_name, contact_email, phone_number)
VALUES (1, 'EventPro', 'info@eventpro.com', '9876543210');

UPDATE organizers
SET phone_number = '9000000000'
WHERE organizer_id = 1;

DELETE FROM organizers
WHERE organizer_id = 99;

SELECT *
FROM organizers
WHERE organizer_name LIKE '%Event%';

INSERT INTO attendees (attendee_id, name, email, phone_number)
VALUES (1, 'Aman Shah', 'aman.shah@email.com', '9123456780');

UPDATE attendees
SET email = 'aman.new@email.com'
WHERE attendee_id = 1;

DELETE FROM attendees
WHERE attendee_id = 99;

SELECT *
FROM attendees
WHERE name LIKE '%Aman%';

INSERT INTO tickets (ticket_id, event_id, attendee_id, booking_date, status)
VALUES (1, 1, 1, CURDATE(), 'Confirmed');

UPDATE tickets
SET status = 'Cancelled'
WHERE ticket_id = 1;

DELETE FROM tickets
WHERE ticket_id = 1;

SELECT *
FROM tickets
WHERE status = 'Confirmed';

-- 2. WHERE, HAVING, LIMIT

SELECT e.event_id, e.event_name, e.event_date, v.venue_name, v.location
FROM events e
JOIN venues v ON e.venue_id = v.venue_id
WHERE e.event_date > CURDATE()
	AND v.location = 'Mumbai'
ORDER BY e.event_date;

SELECT e.event_id, e.event_name, SUM(p.amount_paid) AS total_revenue
FROM events e
JOIN tickets t ON e.event_id = t.event_id
JOIN payments p ON t.ticket_id = p.ticket_id
WHERE p.payment_status = 'Success'
GROUP BY e.event_id, e.event_name
ORDER BY total_revenue DESC
LIMIT 5;

SELECT DISTINCT a.attendee_id, a.name, a.email, a.phone_number
FROM attendees a
JOIN tickets t ON a.attendee_id = t.attendee_id
WHERE t.booking_date >= CURDATE() - INTERVAL 7 DAY;

-- 3. AND, OR, NOT

SELECT e.*
FROM events e
WHERE MONTH(e.event_date) = 12
	AND e.available_seats > (e.total_seats / 2);

SELECT DISTINCT a.attendee_id, a.name, a.email
FROM attendees a
LEFT JOIN tickets t ON a.attendee_id = t.attendee_id
LEFT JOIN payments p ON t.ticket_id = p.ticket_id
WHERE t.ticket_id IS NOT NULL
	 OR p.payment_status = 'Pending';

SELECT e.*
FROM events e
WHERE NOT (e.available_seats = 0);

-- 4. ORDER BY, GROUP BY

SELECT *
FROM events
ORDER BY event_date ASC;

SELECT e.event_id, e.event_name, COUNT(t.attendee_id) AS attendee_count
FROM events e
LEFT JOIN tickets t ON e.event_id = t.event_id
GROUP BY e.event_id, e.event_name;

SELECT e.event_id, e.event_name, COALESCE(SUM(p.amount_paid), 0) AS total_revenue
FROM events e
LEFT JOIN tickets t ON e.event_id = t.event_id
LEFT JOIN payments p ON t.ticket_id = p.ticket_id AND p.payment_status = 'Success'
GROUP BY e.event_id, e.event_name;

-- 5. AGGREGATE FUNCTIONS

SELECT COALESCE(SUM(amount_paid), 0) AS total_revenue
FROM payments
WHERE payment_status = 'Success';

SELECT e.event_id, e.event_name, COUNT(t.attendee_id) AS attendee_count
FROM events e
LEFT JOIN tickets t ON e.event_id = t.event_id
GROUP BY e.event_id, e.event_name
ORDER BY attendee_count DESC
LIMIT 1;

SELECT AVG(ticket_price) AS average_ticket_price
FROM events;


-- 7. JOIN QUERIES

SELECT e.event_id, e.event_name, e.event_date, v.venue_name, v.location
FROM events e
INNER JOIN venues v ON e.venue_id = v.venue_id;

SELECT a.attendee_id, a.name, t.ticket_id, p.payment_status
FROM attendees a
LEFT JOIN tickets t ON a.attendee_id = t.attendee_id
LEFT JOIN payments p ON t.ticket_id = p.ticket_id
WHERE t.ticket_id IS NOT NULL
	AND (p.payment_id IS NULL OR p.payment_status <> 'Success');

SELECT e.event_id, e.event_name, t.ticket_id, t.attendee_id
FROM tickets t
RIGHT JOIN events e ON t.event_id = e.event_id
WHERE t.ticket_id IS NULL;

SELECT a.attendee_id, a.name, t.ticket_id
FROM attendees a
LEFT JOIN tickets t ON a.attendee_id = t.attendee_id
WHERE t.ticket_id IS NULL
UNION
SELECT a.attendee_id, a.name, t.ticket_id
FROM tickets t
RIGHT JOIN attendees a ON t.attendee_id = a.attendee_id
WHERE t.ticket_id IS NULL;

-- 8. SUBQUERIES

SELECT e.event_id, e.event_name, event_revenue
FROM (
	SELECT e.event_id, e.event_name, SUM(p.amount_paid) AS event_revenue
	FROM events e
	JOIN tickets t ON e.event_id = t.event_id
	JOIN payments p ON t.ticket_id = p.ticket_id
	WHERE p.payment_status = 'Success'
	GROUP BY e.event_id, e.event_name
) AS revenue_data
JOIN events e ON e.event_id = revenue_data.event_id
WHERE revenue_data.event_revenue > (
	SELECT AVG(event_revenue)
	FROM (
		SELECT SUM(p.amount_paid) AS event_revenue
		FROM events e
		JOIN tickets t ON e.event_id = t.event_id
		JOIN payments p ON t.ticket_id = p.ticket_id
		WHERE p.payment_status = 'Success'
		GROUP BY e.event_id
	) AS average_revenue_data
);

SELECT a.attendee_id, a.name, COUNT(DISTINCT t.event_id) AS event_count
FROM attendees a
JOIN tickets t ON a.attendee_id = t.attendee_id
GROUP BY a.attendee_id, a.name
HAVING COUNT(DISTINCT t.event_id) > 1;

SELECT o.organizer_id, o.organizer_name, COUNT(e.event_id) AS total_events
FROM organizers o
JOIN events e ON o.organizer_id = e.organizer_id
GROUP BY o.organizer_id, o.organizer_name
HAVING COUNT(e.event_id) > 3;

-- 9. DATE & TIME FUNCTIONS

SELECT event_id, event_name, MONTH(event_date) AS event_month
FROM events;

SELECT event_id, event_name, DATEDIFF(event_date, CURDATE()) AS days_remaining
FROM events
WHERE event_date >= CURDATE();

SELECT payment_id, ticket_id, DATE_FORMAT(CONCAT(payment_date, ' 00:00:00'), '%Y-%m-%d %H:%i:%s') AS formatted_payment_date
FROM payments;

-- 10. STRING MANIPULATION FUNCTIONS

SELECT organizer_id, UPPER(organizer_name) AS organizer_name_upper
FROM organizers;

SELECT attendee_id, TRIM(name) AS trimmed_name
FROM attendees;

SELECT attendee_id, name, COALESCE(email, 'Not Provided') AS email_display
FROM attendees;

-- 11. WINDOW FUNCTIONS

SELECT event_id, event_name, total_revenue, RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
FROM (
	SELECT e.event_id, e.event_name, SUM(p.amount_paid) AS total_revenue
	FROM events e
	LEFT JOIN tickets t ON e.event_id = t.event_id
	LEFT JOIN payments p ON t.ticket_id = p.ticket_id
	WHERE p.payment_status = 'Success'
	GROUP BY e.event_id, e.event_name
) ranked_events;

SELECT e.event_id, e.event_name, e.event_date, SUM(p.amount_paid) AS event_revenue,
	   SUM(SUM(p.amount_paid)) OVER (ORDER BY e.event_date, e.event_id) AS cumulative_ticket_sales
FROM events e
LEFT JOIN tickets t ON e.event_id = t.event_id
LEFT JOIN payments p ON t.ticket_id = p.ticket_id AND p.payment_status = 'Success'
GROUP BY e.event_id, e.event_name, e.event_date;

SELECT event_id, event_name, event_date, attendee_count,
	   SUM(attendee_count) OVER (ORDER BY event_date, event_id) AS running_total_attendees
FROM (
	SELECT e.event_id, e.event_name, e.event_date, COUNT(t.attendee_id) AS attendee_count
	FROM events e
	LEFT JOIN tickets t ON e.event_id = t.event_id
	GROUP BY e.event_id, e.event_name, e.event_date
) AS event_attendance;

-- 12. CASE EXPRESSIONS

SELECT event_id, event_name, available_seats, total_seats,
	   CASE
		   WHEN available_seats < (total_seats * 0.2) THEN 'High Demand'
		   WHEN available_seats BETWEEN (total_seats * 0.2) AND (total_seats * 0.5) THEN 'Moderate Demand'
		   ELSE 'Low Demand'
	   END AS demand_category
FROM events;

SELECT payment_id, ticket_id, payment_status,
	   CASE
		   WHEN payment_status = 'Success' THEN 'Successful'
		   WHEN payment_status = 'Failed' THEN 'Failed'
		   ELSE 'Pending'
	   END AS payment_status_label
FROM payments;
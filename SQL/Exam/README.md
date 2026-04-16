# Event Management SQL Exam

This folder contains a complete SQL practice script for an Event Management System.
It is designed for exam preparation and demonstrates core to advanced SQL concepts.

## File Structure

- `event_managment.sql`: Main SQL script with schema creation and assignment queries.

## Project Objective

The project models how events are organized, tickets are booked, and payments are tracked.
It helps practice:

- Schema design with table relationships
- Data retrieval using filters and joins
- Analytical queries with aggregate and window functions
- Business logic with CASE expressions

## Database Schema

### 1. venues
- `venue_id` (Primary Key)
- `venue_name`
- `location`
- `capacity`

### 2. organizers
- `organizer_id` (Primary Key)
- `organizer_name`
- `contact_email`
- `phone_number`

### 3. events
- `event_id` (Primary Key)
- `event_name`
- `event_date`
- `venue_id` (Foreign Key -> venues.venue_id)
- `organizer_id` (Foreign Key -> organizers.organizer_id)
- `ticket_price`
- `total_seats`
- `available_seats`

### 4. attendees
- `attendee_id` (Primary Key)
- `name`
- `email`
- `phone_number`

### 5. tickets
- `ticket_id` (Primary Key)
- `event_id` (Foreign Key -> events.event_id)
- `attendee_id` (Foreign Key -> attendees.attendee_id)
- `booking_date`
- `status`

### 6. payments
- `payment_id` (Primary Key)
- `ticket_id` (Foreign Key -> tickets.ticket_id)
- `amount_paid`
- `payment_status`
- `payment_date`

## Relationship Summary

- One venue can host many events.
- One organizer can manage many events.
- One event can have many ticket bookings.
- One attendee can book many tickets.
- One ticket can have one or more payment records depending on business rules.

## Query Coverage In Script

The SQL script includes practical examples for:

- CRUD operations (Insert, Update, Delete, Search)
- WHERE, HAVING, LIMIT
- AND, OR, NOT operators
- ORDER BY and GROUP BY
- Aggregate functions: SUM, AVG, COUNT
- JOIN types: INNER JOIN, LEFT JOIN, RIGHT JOIN
- FULL OUTER JOIN style output using UNION
- Subqueries for filtered analytics
- Date and time functions (MONTH, DATEDIFF, DATE_FORMAT)
- String functions (UPPER, TRIM, COALESCE)
- Window functions (RANK, cumulative sums, running totals)
- CASE expressions for business classifications

## How To Run

1. Open MySQL Workbench (or any MySQL-compatible SQL editor).
2. Open `event_managment.sql`.
3. Execute CREATE TABLE statements.
4. Insert test/sample data in all tables.
5. Run query sections one by one to verify outputs.

## Suggested Execution Order

Use this order to avoid foreign key issues:

1. venues
2. organizers
3. events
4. attendees
5. tickets
6. payments

## Example Learning Outcomes

After completing this script, you should be able to:

- Write multi-table joins confidently
- Build grouped analytics reports
- Use nested queries for decision-making logic
- Apply window functions for ranking and running metrics
- Convert business conditions into CASE-based outputs

## Notes

- The script uses MySQL-style syntax and functions.
- Query results depend on available sample data.
- FULL OUTER JOIN is emulated through UNION because MySQL does not support FULL OUTER JOIN directly.
- File name uses `event_managment.sql` spelling as present in this folder.

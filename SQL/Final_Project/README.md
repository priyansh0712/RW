# 📚 Student Management Database System

## 🚀 Overview

This project is a **relational database system** designed to manage student data, courses, instructors, departments, and enrollments using SQL.

It demonstrates:

* Table creation with relationships
* Data insertion
* Core SQL operations (CRUD)
* Advanced queries (JOINs, aggregation, subqueries, window functions)

---

## 🗂️ Database Structure

### 1. Students

Stores student information.

* StudentID (PK)
* FirstName
* LastName
* Email
* BirthDate
* EnrollmentDate

### 2. Departments

Stores department details.

* DepartmentID (PK)
* DepartmentName

### 3. Courses

Stores course details.

* CourseID (PK)
* CourseName
* DepartmentID (FK)
* Credits

### 4. Instructors

Stores instructor information.

* InstructorID (PK)
* FirstName
* LastName
* Email
* DepartmentID (FK)
* Salary

### 5. Enrollments

Links students and courses.

* EnrollmentID (PK)
* StudentID (FK)
* CourseID (FK)
* EnrollmentDate

---

## 🔗 Relationships

* One Department → Many Courses
* One Department → Many Instructors
* One Student → Many Enrollments
* One Course → Many Enrollments

---

## 🧪 Features & Queries

This project includes the following SQL operations:

### 🔹 Basic Operations

* Create tables
* Insert sample data
* Retrieve records

### 🔹 Filtering & Conditions

* Students enrolled after a specific year
* Courses by department

### 🔹 Aggregations

* Count students per course
* Average credits
* Maximum instructor salary

### 🔹 JOIN Operations

* INNER JOIN → Students with enrolled courses
* LEFT JOIN → All students with/without courses

### 🔹 Advanced Queries

* Subqueries
* Window functions (running total)
* CASE statements (Senior/Junior classification)
* Date extraction
* String concatenation

---

## ⚙️ How to Run

1. Open MySQL / SQL environment
2. Copy the full SQL script
3. Execute step-by-step:

   * Create tables
   * Insert data
   * Run queries

---

## ⚠️ Limitations (Don’t Ignore This)

* Sample dataset is **very small**
* Some queries may return **empty results**
* No indexing → not optimized
* Not production-ready schema

---

## 🔥 Improvements You Should Actually Do

If you want this to be useful beyond assignments:

* Add **indexes** on foreign keys
* Use **ON DELETE CASCADE**
* Normalize schema further
* Add more realistic data
* Add constraints (UNIQUE, NOT NULL)
* Implement stored procedures

---

## 🧠 Learning Outcome

After completing this project, you should understand:

* Relational database design
* SQL joins and aggregations
* Real-world query patterns
* Basic performance considerations

---

## 📌 Final Note

Right now, this is **academic-level SQL**.
If your goal is real development or interviews, you need:

* Complex joins
* Query optimization
* Large datasets
* Real-world scenarios

If you want next-level upgrade, ask for:
👉 "Advanced SQL version"
👉 "Interview-level SQL questions"
👉 "DB optimization + indexing"


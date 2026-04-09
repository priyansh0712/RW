-- 1. CREATE TABLES

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    BirthDate DATE,
    EnrollmentDate DATE
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    DepartmentID INT,
    Credits INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    DepartmentID INT,
    Salary DECIMAL(10,2),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);


-- 2. INSERT DATA

INSERT INTO Students VALUES
(1, 'John', 'Doe', 'john.doe@email.com', '2000-01-15', '2022-08-01'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '1999-05-25', '2021-08-01');

INSERT INTO Departments VALUES
(1, 'Computer Science'),
(2, 'Mathematics');

INSERT INTO Courses VALUES
(101, 'Introduction to SQL', 1, 3),
(102, 'Data Structures', 2, 4);

INSERT INTO Instructors VALUES
(1, 'Alice', 'Johnson', 'alice.johnson@univ.com', 1, 70000),
(2, 'Bob', 'Lee', 'bob.lee@univ.com', 2, 65000);

INSERT INTO Enrollments VALUES
(1, 1, 101, '2022-08-01'),
(2, 2, 102, '2021-08-01');


-- 3. QUERIES

-- 2
SELECT * FROM Students
WHERE YEAR(EnrollmentDate) > 2022;

-- 3
SELECT * FROM Courses
WHERE DepartmentID = 2
LIMIT 5;

-- 4
SELECT CourseID, COUNT(StudentID) AS total_students
FROM Enrollments
GROUP BY CourseID
HAVING COUNT(StudentID) > 5;

-- 5
SELECT s.*
FROM Students s
JOIN Enrollments e1 ON s.StudentID = e1.StudentID
JOIN Enrollments e2 ON s.StudentID = e2.StudentID
WHERE e1.CourseID = 101 AND e2.CourseID = 102;

-- 6
SELECT DISTINCT s.*
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE e.CourseID IN (101,102);

-- 7
SELECT AVG(Credits) AS avg_credits FROM Courses;

-- 8
SELECT MAX(Salary) FROM Instructors
WHERE DepartmentID = 1;

-- 9
SELECT d.DepartmentName, COUNT(e.StudentID) AS total_students
FROM Departments d
JOIN Courses c ON d.DepartmentID = c.DepartmentID
JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY d.DepartmentName;

-- 10 INNER JOIN
SELECT s.FirstName, c.CourseName
FROM Students s
INNER JOIN Enrollments e ON s.StudentID = e.StudentID
INNER JOIN Courses c ON e.CourseID = c.CourseID;

-- 11 LEFT JOIN
SELECT s.FirstName, c.CourseName
FROM Students s
LEFT JOIN Enrollments e ON s.StudentID = e.StudentID
LEFT JOIN Courses c ON e.CourseID = c.CourseID;

-- 12 SUBQUERY
SELECT *
FROM Students
WHERE StudentID IN (
    SELECT StudentID
    FROM Enrollments
    GROUP BY CourseID, StudentID
    HAVING COUNT(*) > 10
);

-- 13
SELECT StudentID, YEAR(EnrollmentDate) AS Year
FROM Students;

-- 14
SELECT CONCAT(FirstName, ' ', LastName) AS FullName
FROM Instructors;

-- 15
SELECT CourseID,
COUNT(StudentID) OVER (ORDER BY CourseID) AS running_total
FROM Enrollments;

-- 16
SELECT StudentID,
CASE
    WHEN TIMESTAMPDIFF(YEAR, EnrollmentDate, CURDATE()) > 4 THEN 'Senior'
    ELSE 'Junior'
END AS Status
FROM Students;
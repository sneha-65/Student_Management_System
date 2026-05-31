CREATE VIEW vw_StudentCourses AS

SELECT

    s.StudentID,
    s.StudentName,
    c.CourseName,
    e.EnrollmentDate

FROM Enrollments e

JOIN Students s
ON e.StudentID = s.StudentID

JOIN Courses c
ON e.CourseID = c.CourseID;

CREATE VIEW vw_StudentSummary AS

SELECT

StudentID,

StudentName,

Department

FROM Students;
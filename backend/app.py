from flask import Flask,jsonify,request
from flask_cors import CORS

from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():

    return jsonify({

        "message":"Student Management API Running"

    })
@app.route("/students")
def students():

    conn = get_connection()

    cur = conn.cursor(dictionary=True)

    cur.execute("""

    SELECT *
    FROM Students

    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(data)
@app.route("/addStudent",methods=["POST"])
def add_student():

    data = request.json

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    INSERT INTO Students(

        StudentName,
        Email,
        Phone,
        Department

    )

    VALUES(%s,%s,%s,%s)

    """,

    (

        data["name"],
        data["email"],
        data["phone"],
        data["department"]

    ))

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({

        "message":"Student Added"

    })

@app.route("/deleteStudent/<int:id>",
methods=["DELETE"])
def delete_student(id):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    DELETE FROM Students

    WHERE StudentID=%s

    """,(id,))

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({

        "message":"Student Deleted"

    })

@app.route("/updateStudent/<int:id>",
methods=["PUT"])
def update_student(id):

    data = request.json

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    UPDATE Students

    SET

    StudentName=%s,
    Email=%s,
    Phone=%s,
    Department=%s

    WHERE StudentID=%s

    """,

    (

        data["name"],
        data["email"],
        data["phone"],
        data["department"],
        id

    ))

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({

        "message":"Student Updated"

    })

@app.route("/courses")
def courses():

    conn = get_connection()

    cur = conn.cursor(dictionary=True)

    cur.execute("""

    SELECT *
    FROM Courses

    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(data)

@app.route("/addCourse",
methods=["POST"])
def add_course():

    data = request.json

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    INSERT INTO Courses(

        CourseName,
        Credits

    )

    VALUES(%s,%s)

    """,

    (

        data["courseName"],
        data["credits"]

    ))

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({

        "message":"Course Added"

    })

@app.route("/enrollStudent",
methods=["POST"])
def enroll_student():

    data = request.json

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

    INSERT INTO Enrollments(

        StudentID,
        CourseID

    )

    VALUES(%s,%s)

    """,

    (

        data["studentID"],
        data["courseID"]

    ))

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({

        "message":"Student Enrolled"

    })

@app.route("/studentCourses")
def student_courses():

    conn = get_connection()

    cur = conn.cursor(dictionary=True)

    cur.execute("""

    SELECT *
    FROM vw_StudentCourses

    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(data)
@app.route("/dashboard")
def dashboard():

    conn = get_connection()

    cur = conn.cursor(dictionary=True)

    # Total Students
    cur.execute(
        "SELECT COUNT(*) total FROM Students"
    )
    students = cur.fetchone()["total"]

    # Total Courses
    cur.execute(
        "SELECT COUNT(*) total FROM Courses"
    )
    courses = cur.fetchone()["total"]

    # Total Enrollments
    cur.execute(
        "SELECT COUNT(*) total FROM Enrollments"
    )
    enrollments = cur.fetchone()["total"]

    # Departments
    cur.execute(
        """
        SELECT COUNT(
            DISTINCT Department
        ) total
        FROM Students
        """
    )
    departments = cur.fetchone()["total"]

    conn.close()

    return jsonify({

        "students":students,
        "courses":courses,
        "enrollments":enrollments,
        "departments":departments

    })
@app.route("/departmentReport")
def department_report():

    conn = get_connection()

    cur = conn.cursor(dictionary=True)

    cur.execute("""

    SELECT

    Department,

    COUNT(*) StudentCount

    FROM Students

    GROUP BY Department

    """)

    data = cur.fetchall()

    conn.close()

    return jsonify(data)
@app.route("/courseReport")
def course_report():

    conn = get_connection()

    cur = conn.cursor(dictionary=True)

    cur.execute("""

    SELECT

    c.CourseName,

    COUNT(
        e.StudentID
    ) EnrolledStudents

    FROM Courses c

    LEFT JOIN Enrollments e

    ON c.CourseID =
       e.CourseID

    GROUP BY c.CourseID

    """)

    data = cur.fetchall()

    conn.close()

    return jsonify(data)
@app.route("/studentSummary")
def student_summary():

    conn = get_connection()

    cur = conn.cursor(dictionary=True)

    cur.execute("""

    SELECT *
    FROM vw_StudentSummary

    """)

    data = cur.fetchall()

    conn.close()

    return jsonify(data)

if __name__ == "__main__":

    app.run(debug=True)
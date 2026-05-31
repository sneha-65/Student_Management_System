const API =
"http://127.0.0.1:5000";

loadStudents();
loadCourses();
loadEnrollments();
loadDashboard();
loadDepartmentReport();
loadCourseReport();
async function loadCourseReport(){

    const response =
    await fetch(
        `${API}/courseReport`
    );

    const data =
    await response.json();

    let rows = "";

    data.forEach(item=>{

        rows += `

        <tr>

            <td>
                ${item.CourseName}
            </td>

            <td>
                ${item.EnrolledStudents}
            </td>

        </tr>

        `;

    });

    document.getElementById(
        "courseReportTable"
    ).innerHTML = rows;
}
async function loadDepartmentReport(){

    const response =
    await fetch(
        `${API}/departmentReport`
    );

    const data =
    await response.json();

    let rows = "";

    data.forEach(item=>{

        rows += `

        <tr>

            <td>
                ${item.Department}
            </td>

            <td>
                ${item.StudentCount}
            </td>

        </tr>

        `;

    });

    document.getElementById(
        "departmentTable"
    ).innerHTML = rows;
}
async function loadDashboard(){

    const response =
    await fetch(
        `${API}/dashboard`
    );

    const data =
    await response.json();

    document.getElementById(
        "studentCount"
    ).innerText =
    data.students;

    document.getElementById(
        "courseCount"
    ).innerText =
    data.courses;

    document.getElementById(
        "enrollmentCount"
    ).innerText =
    data.enrollments;

    document.getElementById(
        "departmentCount"
    ).innerText =
    data.departments;
}
async function loadStudents(){

    const response =
    await fetch(`${API}/students`);

    const data =
    await response.json();

    document.getElementById(
        "studentCount"
    ).innerText = data.length;

    let rows = "";

    data.forEach(student=>{

        rows += `

        <tr>

            <td>${student.StudentID}</td>

            <td>${student.StudentName}</td>

            <td>${student.Email}</td>

            <td>${student.Phone}</td>

            <td>${student.Department}</td>

            <td>

                <button
                onclick="deleteStudent(
                ${student.StudentID}
                )">

                    Delete

                </button>

            </td>

        </tr>

        `;

    });

    document.getElementById(
        "studentTable"
    ).innerHTML = rows;
}


async function addStudent(){

    const name =
    document.getElementById(
        "name"
    ).value;

    const email =
    document.getElementById(
        "email"
    ).value;

    const phone =
    document.getElementById(
        "phone"
    ).value;

    const department =
    document.getElementById(
        "department"
    ).value;

    await fetch(

        `${API}/addStudent`,

        {

            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({

                name,
                email,
                phone,
                department

            })

        }

    );

    alert("Student Added");

    loadStudents();
}

async function deleteStudent(id){

    await fetch(

        `${API}/deleteStudent/${id}`,

        {

            method:"DELETE"

        }

    );

    loadStudents();
}

function searchStudent(){

    const input =
    document.getElementById(
        "search"
    ).value.toLowerCase();

    const rows =
    document.querySelectorAll(
        "#studentTable tr"
    );

    rows.forEach(row=>{

        const text =
        row.innerText.toLowerCase();

        row.style.display =
        text.includes(input)
        ? ""
        : "none";

    });
}
async function loadCourses(){

    const response =
    await fetch(`${API}/courses`);

    const data =
    await response.json();

    document.getElementById(
        "courseCount"
    ).innerText = data.length;

    let rows = "";

    data.forEach(course=>{

        rows += `

        <tr>

            <td>${course.CourseID}</td>

            <td>${course.CourseName}</td>

            <td>${course.Credits}</td>

        </tr>

        `;

    });

    document.getElementById(
        "courseTable"
    ).innerHTML = rows;
}
async function addCourse(){

    const courseName =
    document.getElementById(
        "courseName"
    ).value;

    const credits =
    document.getElementById(
        "credits"
    ).value;

    await fetch(

        `${API}/addCourse`,

        {

            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({

                courseName,
                credits

            })

        }

    );

    alert("Course Added");

    loadCourses();
}
async function enrollStudent(){

    const studentID =
    document.getElementById(
        "studentID"
    ).value;

    const courseID =
    document.getElementById(
        "courseID"
    ).value;

    await fetch(

        `${API}/enrollStudent`,

        {

            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({

                studentID,
                courseID

            })

        }

    );

    alert(
        "Student Enrolled"
    );

    loadEnrollments();
}

async function loadEnrollments(){

    const response =
    await fetch(
        `${API}/studentCourses`
    );

    const data =
    await response.json();

    let rows = "";

    data.forEach(item=>{

        rows += `

        <tr>

            <td>
                ${item.StudentName}
            </td>

            <td>
                ${item.CourseName}
            </td>

            <td>
                ${item.EnrollmentDate}
            </td>

        </tr>

        `;

    });

    document.getElementById(
        "enrollmentTable"
    ).innerHTML = rows;
}
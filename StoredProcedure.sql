DELIMITER $$

CREATE PROCEDURE AddStudent(

    IN p_name VARCHAR(100),
    IN p_email VARCHAR(100),
    IN p_phone VARCHAR(20),
    IN p_department VARCHAR(100)

)

BEGIN

    INSERT INTO Students(

        StudentName,
        Email,
        Phone,
        Department

    )

    VALUES(

        p_name,
        p_email,
        p_phone,
        p_department

    );

END$$

DELIMITER ;
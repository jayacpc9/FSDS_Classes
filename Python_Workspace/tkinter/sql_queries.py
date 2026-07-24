INSERT_NEW_STUDENT = "INSERT INTO registration (name, course, fee) VALUES (%s, %s, %s)"
SELECT_ALL_STUDENT = "SELECT * FROM registration"
UPDATE_STUDENT_DETAILS = "UPDATE registration SET name=%s, course=%s, fee=%s WHERE id=%s"
DELETE_STUDENT_DETAILS = "DELETE FROM registration WHERE id=%s"

CREATE TABLE IF NOT EXISTS students
                (student_id SERIAL PRIMARY KEY, 
                first_name TEXT NOT NULL, 
                last_name TEXT NOT NULL, 
                year_of_studying INTEGER NOT NULL,
                date_of_birth DATE NOT NULL);

CREATE TABLE IF NOT EXISTS lectures
                (lecture_id SERIAL PRIMARY KEY, 
                teacher_id INTEGER NOT NULL, 
                course TEXT NOT NULL, 
                required BOOL NOT NULL);

CREATE TABLE IF NOT EXISTS courses
                (course_id SERIAL PRIMARY KEY, 
                course_name TEXT NOT NULL,
                teacher_id INTEGER NOT NULL);
              
CREATE TABLE IF NOT EXISTS student_course_connection
                (student_id INTEGER NOT NULL, 
                course_id INTEGER NOT NULL,
                grade INTEGER,
                CONSTRAINT uc_scc UNIQUE (student_id, course_id));                
                
CREATE TABLE IF NOT EXISTS teachers
                    (teacher_id SERIAL PRIMARY KEY, 
                    first_name TEXT NOT NULL, 
                    last_name TEXT NOT NULL, 
                    hiring_date DATE NOT NULL,
                    course_id INTEGER NOT NULL);                
                
CREATE TABLE IF NOT EXISTS course_lecture_connection
                (course_id INTEGER NOT NULL,
                lecture_id INTEGER NOT NULL,
                time_held TIMESTAMP,
                CONSTRAINT uc_clc UNIQUE (course_id, lecture_id));                
                
CREATE TABLE IF NOT EXISTS student_lecture_connection
                (student_id INTEGER NOT NULL, 
                lecture_id INTEGER NOT NULL,
                CONSTRAINT uc_slc UNIQUE (student_id, lecture_id));
                

CREATE TABLE IF NOT EXISTS average_grade_storage
		(id INTEGER NOT NULL,
		grade FLOAT NOT NULL);
               

               
               
               
                
do $$
	begin
		if ((select count(*) from students) <= 0) then
			INSERT INTO students(first_name,last_name,year_of_studying, date_of_birth)
              VALUES('Milos', 'Korac', 2, '1996-02-21'),
              ('Marko', 'Kostic', 3, '1995-03-13'),
              ('Marijana', 'Hajdari', 3, '1994-05-12'),
              ('Ana', 'Nikolić', 1, '1998-02-02');
		end if;

		if ((select count(*) from lectures) <= 0) then
			INSERT INTO lectures(teacher_id,course, required)
              VALUES(3, 'Intro to data bases', False),
              (2, 'Intro to object orientated programming', True),
              (2, 'Python syntax', False),
              (3, 'SELECT and INSERT', True);
		end if;

		if ((select count(*) from courses) <= 0) then
			INSERT INTO courses(course_name, teacher_id)
              VALUES('Data Bases', 1),
              ('Object Programming', 2),
              ('Java', 3),
              ('Visual Programming', 1);
		end if;

	
			if ((select count(*) from student_course_connection) <= 0) then
			INSERT INTO student_course_connection(student_id, course_id, grade)
              VALUES(1, 1, 7),
              (1, 2, 9),
              (1, 3, 6),
              (1, 4, 7),
              (2, 2, 7),
              (2, 4, 6),
              (2, 1, 5),
              (3, 4, 8),
              (4, 2, 7),
              (4, 3, 10);
			end if;
		
			if ((select count(*) from teachers) <= 0) then
			INSERT INTO teachers(first_name,last_name, hiring_date, course_id)
              VALUES('Miodrag', 'Draganovic', '2000-03-03', 2),
              ('Aleksandra', 'Kovacevic', '2010-02-15', 1),
              ('Nemanja', 'Ristic', '2015-03-03', 3),
              ('Milica', 'Nestorovic', '2018-09-10', 4);
   			end if;

             
			if ((select count(*) from course_lecture_connection) <= 0) then
			INSERT INTO course_lecture_connection(course_id, lecture_id, time_held)
              VALUES(1, 1, '2021-09-14 12:30:00'),
              (2, 2, '2021-09-17 15:30:00'),
              (2, 3, '2021-10-1 12:30:00'),
              (1, 4, '2021-10-1 15:00:00');             
			end if;

			if ((select count(*) from student_lecture_connection) <= 0) then
			INSERT INTO student_lecture_connection(student_id, lecture_id)
              VALUES(1, 1),
              (2, 2),
              (2, 3),
              (3, 2),
              (3, 3),
              (4, 1),
              (4, 2),
              (4, 4); 
			end if;         
end $$

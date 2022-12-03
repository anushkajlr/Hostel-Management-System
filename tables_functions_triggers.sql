create table student(room_no int, srn varchar(50), name varchar(50), semester int, phone bigint, address varchar(200), PRIMARY KEY(srn));

create table dependent(dependent_id int,name varchar(50),relation varchar(50),phone bigint, address varchar(100),dob date,PRIMARY KEY(dependent_id));

create table student_dependent(srn varchar(50),dependent_id int ,PRIMARY KEY(srn, dependent_id), FOREIGN KEY(srn) REFERENCES student(srn) ON DELETE CASCADE, FOREIGN KEY(dependent_id) REFERENCES dependent(dependent_id));

create table unit(unit_no int PRIMARY KEY, location varchar(100), capacity int);

alter table student add column unit_no int;

alter table student add constraint FOREIGN KEY (unit_no) references unit(unit_no);

create table staff(staff_id int PRIMARY KEY,unit_no int, name varchar(50), occupation varchar(50), salary int, dob date,doj date, FOREIGN KEY(unit_no) references unit(unit_no));

create table fee(rcpt_id int PRIMARY KEY, srn varchar(50), amount int, year year, FOREIGN KEY(srn) references student(srn) ON DELETE CASCADE);

create table lg(srn varchar(50), start_date date, end_date date, dependent_id int,PRIMARY KEY(srn,dependent_id), FOREIGN KEY (srn) references student(srn) on delete cascade, FOREIGN KEY (dependent_id) references dependent(dependent_id));
alter table lg add column duration int;

DELIMITER $$
CREATE FUNCTION calc_age(dob date)
RETURNS int
DETERMINISTIC
BEGIN
DECLARE result int;
(SELECT DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),dob)), '%Y')+0 as age) into result;
return result;
END;
$$


DELIMITER $$
CREATE TRIGGER guardian_count
BEFORE INSERT
ON student_guardian 
FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(500);
DECLARE result int;
(select count(*) from student_guardian where srn = new.srn) into result;
IF (result > 1)
THEN
SET error_msg = 'Cannot have more than two guardian';
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg;
END IF;
END $$


DELIMITER $$
CREATE TRIGGER date_verify
BEFORE INSERT
ON lg
FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(500);
DECLARE result int;
(select DATEDIFF(new.end_date,new.start_date)) into result;
IF (result < 0)
THEN
SET error_msg = 'Please enter correct date range';
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg;
END IF;
END $$


	



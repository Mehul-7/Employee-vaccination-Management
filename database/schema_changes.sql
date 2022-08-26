CREATE TABLE IF NOT EXISTS user_details
(
id varchar(12) PRIMARY KEY ,
user_name varchar(33) NOT NULL ,
dob date NOT NULL ,
contact varchar(13) NOT NULL ,
gender varchar(6) NOT NULL ,
_password varchar(16)
);

CREATE TABLE IF NOT EXISTS dose_details(
    id varchar (12) NOT NULL ,
    date date NOT NULL,
    dose_type varchar(10) NOT NULL,
    PRIMARY KEY (id, dose_type)
);
-- id -> last 4 digit
-- dose_type -> how many

CREATE TABLE IF NOT EXISTS vaccine_details (
    id int PRIMARY KEY,
    name varchar(10) NOT NULL
);
-- #1 -> Covaxine
-- #2 -> Covishield

CREATE TABLE IF NOT EXISTS role_mapping (
user_id varchar(12) NOT NULL ,
role_id int NOT NULL,
constraint pk_user_role PRIMARY KEY(user_id, role_id),
constraint fk_role FOREIGN KEY (role_id) REFERENCES roles(id),
constraint fk_user FOREIGN KEY (user_id) REFERENCES user_details(id)
);
CREATE TABLE IF NOT EXISTS roles (
    id int(3) PRIMARY KEY,
    name varchar(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS dose_info_mapping (
   user_id varchar(12) ,
   dose_id varchar(12) ,
   vaccine_id int ,
   PRIMARY KEY (user_id),
   constraint fk_user_dose foreign key (user_id) REFERENCES user_details(id),
   constraint fk_dose FOREIGN KEY (dose_id) REFERENCES dose_details(id),
   constraint fk_vaccine FOREIGN KEY (vaccine_id) REFERENCES vaccine_details(id)
);
-- which vaccine to which user and when
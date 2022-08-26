insert into user_details(id, user_name, dob, contact, gender, password)
values("813870812124", "mehul", "2000-05-07", "9919838736", "Male", "temp123");

insert into roles(id, name)
values(1, "admin");

insert into roles(id , name)
values(0 , "regular")

insert into role_mapping(user_id, role_id)
values("813870812124", 1);

insert into vaccine_details(id, name)
values(01, "covaxin");

insert into vaccine_details(id, name)
values(02, "sputnik");

insert into dose_details(id, date, dose_type)
values("1234", "2021-05-10", "1");

insert into dose_info_mapping(user_id, dose_id, vaccine_id)
values("813870812124", "1234", 01)

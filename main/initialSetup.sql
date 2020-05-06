create database corona;
show databases;
use corona;


create table patients ( patient_id int not null, primary key(patient_id), 
						state_patient_number varchar(20), 
						date_announced date,
                        estimated_onset_date date,
                        age_bracket int,
                        gender varchar(10),
                        detected_city varchar(20),
                        detected_district varchar(20),
                        detected_state varchar(20),
                        status_code varchar(20),
                        current_status varchar(20),
                        notes varchar(50),
                        contracted_from varchar(8),
                        nationality varchar(20),
                        type_of_transmission varchar(30),
                        status_change_date date);
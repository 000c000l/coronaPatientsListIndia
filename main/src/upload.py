import mysql.connector

def mysql_load(path):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password"
    )
    cursor=mydb.cursor()
    cursor.execute("use corona;")
    cursor.execute("truncate table patients;")
    cmd=f"""load data local infile '{path}' into table patients fields terminated by ',' lines terminated by '\\n' ignore 1 rows (patient_id,state_patient_number,date_announced,estimated_onset_date,age_bracket,gender,detected_city,detected_district,detected_state,status_code,current_status,notes,contracted_from,nationality,type_of_transmission,status_change_date);"""
    print("run this command on your mysql:")
    cursor.execute(cmd)
    print(cmd)
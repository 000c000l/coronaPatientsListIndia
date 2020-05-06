import mysql.connector
def mysql_query(query):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password"
    )
    cursor=mydb.cursor()
    cursor.execute("use corona;")
    cursor.execute(query)
    list_of_locations=[]
    for i in cursor:
        print(i[0])
        list_of_locations.append(i[0])
    return list_of_locations
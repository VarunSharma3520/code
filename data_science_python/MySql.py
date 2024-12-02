import pymysql
#!database link:https://console.aiven.io/account/a46b5440bb59/project/datasciencelearn/services/mysql-afd228b/overview

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="mysql-afd228b-datasciencelearn.aivencloud.com",
    password="AVNS_pEE5vj0CSCNvCYEX0sx",
    read_timeout=timeout,
    port=11357,
    user="avnadmin",
    write_timeout=timeout,
)

try:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
    cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
    cursor.execute("SELECT * FROM mytest")
    print(cursor.fetchall())
finally:
    connection.close()

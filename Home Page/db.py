import mysql.connector


user_login_db=mysql.connector.connect(host='loaclhost',
                            user='root',
                            password='kalyanalamelu',
                            )
            

cursor = user_login_db.cursor()

cursor.execute("CREATE DATABASE mydatabase")

cursor.execute("SHOW DATABASES")

'''for x in cursor:
  print(x)'''


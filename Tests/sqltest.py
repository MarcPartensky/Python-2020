import pymysql
connection = pymysql.connect(host='127.0.0.1',
                             user='esclave',
                             password='esclave',
                             db='commandes')
c = connection.cursor()   
cursor = c.execute('select * from answers')
names = next(zip(*cursor.description))
print(names)

import MySQLdb

conn = MySQLdb.connect('localhost', 'root', '123Qwe456', 'task')
cursor = conn.cursor()

cursor.execute("SELECT * FROM task.guns")

# Получаем данные.
row = cursor.fetchone()
print(row)

# Разрываем подключение.
conn.close()
import mysql.connector

# Подключение к базе данных
cnx = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='mysql'
)

# Создание курсора
cursor = cnx.cursor()

# Выполнение запроса
cursor.execute("SELECT * FROM user")

# Получение результатов
results = cursor.fetchall()

# Вывод результатов
for row in results:
    print(row)

# Закрытие соединения
cnx.close()
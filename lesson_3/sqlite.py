import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('example.db')

# Создание курсора
cur = conn.cursor()

# Создание таблицы
cur.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Вставка записей
cur.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')")
cur.execute("INSERT INTO users (name, email) VALUES ('Jane Doe', 'jane@example.com')")

# Сохранение изменений
conn.commit()

# Выборка записей
cur.execute('SELECT * FROM users')
rows = cur.fetchall()

# Вывод записей
for row in rows:
    print(row)

# Закрытие соединения
conn.close()
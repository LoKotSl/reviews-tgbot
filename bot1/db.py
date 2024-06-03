import sqlite3
#--
conn = sqlite3.connect('data/mydatabase.db')
cursor = conn.cursor()
#--

# Создаем таблицу для каналов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS channels (

        id INTEGER,
        channel_link TEXT
    )
''')
conn.commit()

# Функция для добавления канала в бд
def add_channel_to_db(id, channel_link):
    cursor.execute('INSERT OR IGNORE INTO channels (id, channel_link) VALUES (?, ?)',
                   (id, channel_link))
    conn.commit()
# Функция для добавления редактирования канала в бд
def edit_channel_in_db(id, channel_edit_link):
    cursor.execute("UPDATE channels SET channel_link = ? WHERE id = ?", (channel_edit_link, id))
    conn.commit()
# Проверка существования айди в бд
def check_id_in_db(id):
    return cursor.execute("SELECT COUNT(*) FROM channels WHERE id = ?", (id,)).fetchone()[0] > 0

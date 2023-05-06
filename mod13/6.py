import sqlite3

def update_work_schedule(cursor: sqlite3.Cursor, schedule: [tuple[int, str]]) -> None:
    cursor.executemany("""INSERT INTO table_friendship_schedule 
    (employee_id, date) VALUES (?, ?)""", schedule)


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM 'table_friendship_schedule'""")
        update_work_schedule(cursor)

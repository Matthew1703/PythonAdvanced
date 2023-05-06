import sqlite3

def register(username: str, password: str) -> None:
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
            INSERT INTO `table_users` (username, password)
            VALUES ('{username}, {password}')  
            """
        )
        conn.commit()
def hack() -> None:
    # username: str = "i_like --  DELETE FROM 'table_users'"
    # username: str = "i_like"
    # username: str = "DELETE table_users"
    username: str = "i_like', 1000) -- DELETE FROM 'table_users'"
    # username: str = "i_like', 1000) -- "
    password: str = "sql_injection"
    register(username, password)

if __name__ == "__main__":
    hack()
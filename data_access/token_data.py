from data_connection import get_db_connection

def add_token(token, username):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO refresh_tokens (token, username) VALUES (?, ?)",
        (token, username)
    )
    conn.commit()
    conn.close()

def remove_token(token):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM refresh_tokens WHERE token = ?",
        (token,)
    )
    conn.commit()
    conn.close()

def is_token_valid(token):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT token FROM refresh_tokens WHERE token = ?",
        (token,)
    ).fetchone()
    conn.close()
    return row is not None

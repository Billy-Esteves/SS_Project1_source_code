from . import utils

def get_user_by_username(cur, username):
    sql, params = utils.prepare_query(
        "SELECT id, username, password, is_disabled, is_admin FROM users WHERE username=%s",
        (username,)
    )
    cur.execute(sql, params)
    return cur.fetchone()

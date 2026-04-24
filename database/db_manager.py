import sqlite3

class Database:
    def __init__(self, db_name="repos.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS saved_repos (
                user_id INTEGER,
                full_name TEXT,
                html_url TEXT,
                UNIQUE(user_id, full_name)
            )
        """)
        self.conn.commit()

    def save_repo(self, user_id, full_name, html_url):
        try:
            self.cursor.execute(
                "INSERT INTO saved_repos VALUES (?, ?, ?)", 
                (user_id, full_name, html_url)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False # Repo already saved

    def get_repos(self, user_id):
        self.cursor.execute(
            "SELECT full_name, html_url FROM saved_repos WHERE user_id = ?", 
            (user_id,)
        )
        return self.cursor.fetchall()
import sqlite3

from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer


class Database:
    def __init__(self, file) -> None:
        self._connection = None
        self.file = file

    def __enter__(self):
        self._connection = sqlite3.connect(self.file)
        return self._connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._connection:
            self._connection.commit()
            self._connection.close()
        return False


class Records():
    fields = [
        "started_at",
        "ended_at",
        "activity",
        "comment",
    ]

    def __init__(self, database) -> None:
        self.database = database
        self.create_table()

    def create_table(self) -> None:
        with self.database as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS records (
                    started_at DATETIME NOT NULL,
                    ended_at DATETIME NOT NULL,
                    activity TEXT,
                    comment TEXT
                )
            """)

    def get(self):
        with self.database as db:
            db.execute("""
                SELECT * FROM records
            """)
            return db.fetchall()


class TimeApp(App):
    def __init__(self) -> None:
        self.database = Database("time.db")
        self.records = Records(self.database)
        App.__init__(self)

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        for column in self.records.fields:
            table.add_column(column)
        rows = self.records.get()
        table.add_rows(rows)


if __name__ == "__main__":
    app = TimeApp()
    app.run()

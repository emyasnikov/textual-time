from peewee import *
from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer

db = SqliteDatabase("time.db")


class Records(Model):
    class Meta:
        database = db

    started_at = DateTimeField()
    ended_at = DateTimeField()
    activity = TextField()
    comment = TextField()


class TimeApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()


if __name__ == "__main__":
    app = TimeApp()
    db.connect()
    db.create_tables([Records])
    app.run()

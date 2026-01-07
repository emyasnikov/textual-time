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

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        query = Records.select().dicts()
        for column in query[0].keys():
            table.add_column(column)
        rows = [d.values() for d in query]
        table.add_rows(rows)


if __name__ == "__main__":
    app = TimeApp()
    db.connect()
    db.create_tables([Records])
    app.run()

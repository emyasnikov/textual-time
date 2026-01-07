from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer


class TimeApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()


if __name__ == "__main__":
    app = TimeApp()
    app.run()

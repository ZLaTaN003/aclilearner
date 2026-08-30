from rich.layout import Layout
from rich.text import Text
from rich.panel import Panel

from acli import console


class LayoutInterface:
    def __init__(self):
        self.main_layout = Layout(name="main_layout")
        self.current_layout = self.main_layout

    def update_main_layout(self, heading: Text, body: Text) -> None:
        content = heading + body
        self.current_layout.update(Panel(content))

    def update_right_layout(self, content: Text) -> None:
        self.right_layout.update(Panel(content))

    def print(self) -> None:
        console.print(self.main_layout)

    def split_layout(self) -> None:
        self.main_layout.split_row(Layout(name="left"), Layout(name="right"))
        self.left_layout = self.main_layout["left"]
        self.right_layout = self.main_layout["right"]
        self.current_layout = self.left_layout

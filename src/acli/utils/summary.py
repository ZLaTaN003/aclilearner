from rich.panel import Text
from pathlib import Path
from importlib.resources import files


class Summary:
    def __init__(self, command: str) -> None:

        self.tldr_path = files("acli").joinpath("tldr_commands")
        self.command = command

    def get_help_text(self) -> str:
        return self.get_tldr_content()

    def __rich__(self) -> Text:
        return Text(self.help_text)

    def get_tldr_content(self):
        glob = self.tldr_path.rglob(f"{self.command}.md")
        file = next(glob, None)

        if not file:
            return "Not Found"
        content = file.read_text()
        return content

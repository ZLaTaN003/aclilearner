from rich.panel import Text
import subprocess


class Summary:

    def __init__(self, command: str) -> None:
        self.command = command
        self.help_text = self.get_help_text()

    def get_help_text(self) -> str:
        return subprocess.run(
            [self.command, "--help"], capture_output=True, encoding="utf-8"
        ).stdout

    def __rich__(self) -> Text:
        return Text(self.help_text)

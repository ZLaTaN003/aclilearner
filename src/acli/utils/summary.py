from rich.panel import Text
import subprocess


class Summary:

    def __init__(self, command: str) -> None:
        self.command = command
        self.help_text = self.get_help_text()

    def get_help_text(self) -> str:
        result = subprocess.run(
            [self.command, "--help"], capture_output=True, encoding="utf-8"
        ).stdout
        if not result:
            result = subprocess.run(
                ["man", self.command], capture_output=True, encoding="utf-8"
            ).stdout
        return result

    def __rich__(self) -> Text:
        return Text(self.help_text)

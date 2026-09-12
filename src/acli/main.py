from argparse import ArgumentParser
from acli.layout import LayoutInterface
from rich.prompt import IntPrompt
from rich.text import Text
from acli.utils.summary import Summary
from acli.utils.download_organizer import DownloadOrganizer
from rich.markdown import Markdown

COMMAND_CATEGORIES = {
    "File and Directory": [
        "ls",
        "cd",
        "pwd",
        "mkdir",
        "rmdir",
        "rm",
        "head",
        "tail",
        "touch",
        "cp",
        "mv",
        "paste",
        "cat",
        "grep",
        "find",
        "df",
        "du",
        "chmod",
        "chown",
    ],
    "Text Processing": ["awk", "grep", "wc", "sort"],
    "Process and System Monitoring": [
        "ps",
        "exec",
        "htop",
        "free",
        "kill",
        "killall",
        "whoami",
        "systemctl",
        "journalctl",
        "strace",
    ],
    "Networking": [
        "ping",
        "ifconfig",
        "nslookup",
        "netstat",
        "wget",
        "curl",
        "ssh",
        "scp",
    ],
    "Other Utils": ["alias", "unalias", "history", "echo", "watch"],
}
category_shortcut_map = {
    "fd": "File and Directory",
    "tp": "Text Processing",
    "pm": "Process and System Monitoring",
    "nt": "Networking",
    "ot": "Other Utils",
    "dorg": "Download Organizer",
}

parser = ArgumentParser(
    prog="acli",
    description="Linux Commands Easy to Find",
    allow_abbrev=False,
)
category_string = ",".join(category for category in category_shortcut_map.values())
parser.add_argument(
    "category",
    choices=category_shortcut_map,
    help=f"Categories are {category_string}",
)

args = parser.parse_args()
if args.category:
    chosen_category = category_shortcut_map[args.category]

layout = LayoutInterface()


def main() -> None:
    while True:
        commands = sorted(COMMAND_CATEGORIES.get(chosen_category))
        if not commands:
            organizer = DownloadOrganizer()
            organizer.run()
            break

        populate_command_options(commands)
        layout.print()

        try:
            chosen_command_index = IntPrompt.ask(
                "Choose the command, Give the index number 0 to exit"
            )

            if chosen_command_index == 0:
                break

            chosen_command = commands[chosen_command_index - 1]
            summary = Summary(chosen_command).get_help_text()

            layout.split_layout()

            layout.update_right_layout(Markdown(summary))

        except ValueError:
            print("The category/command index must be an integer")


def populate_command_options(commands: list[str]) -> None:
    content = ""
    for index, command in enumerate(commands):
        content += f"{index+1} {command} \n"

    body = Text(content)
    heading = Text("Choose the command  \n")
    layout.update_main_layout(heading, body)


if __name__ == "__main__":
    main()

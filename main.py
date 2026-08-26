import subprocess
from argparse import ArgumentParser

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
}

parser = ArgumentParser(
    prog="acli", description="Linux Command Categorised", allow_abbrev=False
)

for category in category_shortcut_map:
    parser.add_argument(
        f"--{category}",
        action="store_const",
        const=category_shortcut_map[category],
        help=f"{category_shortcut_map[category]} commands are selected",
    )


chosen_category = next(
    category
    for short, category in category_shortcut_map.items()
    if getattr(parser.parse_args(), short)
)
print(chosen_category, "this")


def main() -> None:
    while True:
        print("Welcome to acli")
        commands = COMMAND_CATEGORIES[chosen_category]
        display_command_options(commands)

        try:
            chosen_command_index = int(
                input("Choose the command, Give the index number \n")
            )

            print("you chose", chosen_command_index)

        except ValueError:
            print("The category/command index must be an integer")


def display_command_options(commands) -> None:
    for index, command in enumerate(commands):
        print(f"{index+1}   {command}")


if __name__ == "__main__":
    main()

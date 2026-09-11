import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
src_dir = os.path.join(project_dir, "src")
sys.path.append(src_dir)

from acli.utils.summary import Summary


def test_summary_exists():
    command = "ls"
    s = Summary(command).get_help_text()
    print(s)
    assert s is not None
    assert command in s


def test_summary_not_exisits():
    command = "thiscommanddontexist"
    s = Summary(command).get_help_text()
    assert s == "Not Found"

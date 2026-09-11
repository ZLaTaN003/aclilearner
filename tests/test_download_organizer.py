import os, sys
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
src_dir = os.path.join(project_dir, "src")
sys.path.append(src_dir)

from acli.utils.download_organizer import DownloadOrganizer


def test_download_organizer_organizes():
    d = DownloadOrganizer()
    tmp_folder = Path("/tmp/downloadorg_test")
    tmp_folder.mkdir(exist_ok=True)
    img = tmp_folder / "Cat.jpg"
    img.touch()
    d.base_dir = tmp_folder
    d.run()

    assert not img.exists()
    assert (tmp_folder / "Images" / "Cat.jpg").exists()

from pathlib import Path
import shutil

FOLDER_CATEGORY = {
    "pdf": "Documents",
    "pptx": "Documents",
    "docx": "Documents",
    "doc": "Documents",
    "ppt": "Documents",
    "xls": "Documents",
    "xlsx": "Documents",
    "txt": "Documents",
    "csv": "Documents",
    "rtf": "Documents",
    "epub": "Documents",
    "mp4": "Videos",
    "mkv": "Videos",
    "avi": "Videos",
    "mov": "Videos",
    "webm": "Videos",
    "flv": "Videos",
    "mp3": "Audio",
    "wav": "Audio",
    "flac": "Audio",
    "aac": "Audio",
    "m4a": "Audio",
    "ogg": "Audio",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "svg": "Images",
    "webp": "Images",
    "bmp": "Images",
    "ico": "Images",
    "psd": "Images",
    "ai": "Images",
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "tar": "Archives",
    "gz": "Archives",
    "exe": "Applications",
    "msi": "Applications",
    "dmg": "Applications",
    "pkg": "Applications",
    "deb": "Applications",
    "rpm": "Applications",
    "apk": "Applications",
    "py": "Code",
    "js": "Code",
    "html": "Code",
    "css": "Code",
    "json": "Code",
    "cpp": "Code",
    "c": "Code",
    "java": "Code",
    "sh": "Code",
    "obj": "Design",
    "stl": "Design",
    "fbx": "Design",
}

BASE_DIR = Path("/home/adithyakrishna/Downloads")


class DownloadOrganizer:
    def create_category_directories(self):
        folders = set(FOLDER_CATEGORY.values())
        for folder in folders:
            folder_path = BASE_DIR / folder
            folder_path.mkdir(parents=True, exist_ok=True)

        print("Folders are created")

    def run(self):
        self.create_category_directories()
        for f in BASE_DIR.iterdir():
            if f.is_file():
                ext = f.suffix.lstrip(".")
                category = FOLDER_CATEGORY.get(ext)
                if category:
                    destination_location = BASE_DIR / category / f.name
                    shutil.move(f, destination_location)

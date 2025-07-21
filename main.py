""" Utility to organize files in a directory by extension """

import sys
from pathlib import Path

if len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit(1)

# If no argument is given work in the current directory
PATH = Path(sys.argv[1] if len(sys.argv) == 2 else "").resolve()
PATH_POSIX = PATH.as_posix()

if not PATH.is_dir():
    print(f"Invalid path: {PATH_POSIX}")
    sys.exit(1)

if input(f"Working on directory {PATH_POSIX}, continue? [y/n]: ").lower() != "y":
    sys.exit(0)

# Map file extensions with their destination directory
# Add more if needed
ext_dir = {
    ".jpeg": "Images",
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".acc": "Audio",
    ".mp4": "Video",
    ".avi": "Video",
    ".wmv": "Video",
    ".mkv": "Video",
    ".webm": "Video",
    ".exe": "Executable",
    ".msi": "Executable",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".pptx": "Documents", 
    ".docx": "Documents",
    ".rar": "Compressed",
    ".zip": "Compressed",
}

for item in PATH.iterdir():
    # Work only with files
    if not item.is_file():
        continue

    ext = item.suffix
    # Ignore files without a valid extension
    if not ext in ext_dir:
        continue

    new_dir = ext_dir[ext]
    new_path = PATH.joinpath(new_dir)

    new_path.mkdir(exist_ok=True)

    try:
        item.rename(new_path.joinpath(item.name))
        print(f'Moved "{item.name}" to "{new_dir}"')
    except FileExistsError:
        print(f'A file with the name "{item.name}" already exists in "{new_dir}"')

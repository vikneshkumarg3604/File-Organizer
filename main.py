import os
from pathlib import Path
import glob
import shutil
from tkinter import Tk, filedialog

FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Spreadsheets": [".xlsx", ".xls", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css"]
}

root = Tk()
root.withdraw()

path = filedialog.askdirectory(title="Select Folder to Organize")

if not path:
    print("No folder selected. Exiting...")
    exit()

path=Path(path)
if os.path.exists(path):

    for category,extensions in FILE_TYPES.items():
        for ext in extensions:
            files=glob.glob(os.path.join(path,"*"+ext))
            for file in files:
                file=Path(file)
                print(file.name,"->",category)
                dest=path / category
                dest.mkdir(parents=True,exist_ok=True)
                target=dest/file.name

                if target.exists():
                    print("File already exists:", file.name)
                    
                else:

                    shutil.move(str(file),str(target))

print("sucess")
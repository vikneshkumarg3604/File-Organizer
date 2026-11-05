# 📁 Smart File Organizer

A Python-based automation tool that organizes files into separate folders based on their file extensions.

The project simplifies file management by automatically identifying file types, creating corresponding folders, and moving files into their respective categories.

## 🚀 Features

- **Automatic File Categorization:** Identifies files based on their extensions.
- **Dynamic Folder Creation:** Creates destination folders automatically.
- **File Organization:** Moves files into their respective category folders.
- **Folder Selection:** Allows users to select a folder using a graphical folder selection dialog.
- **Multiple File Types:** Supports documents, spreadsheets, images, videos, audio, archives, and code files.

## 🛠️ Technologies Used

- Python 3
- OS Module
- Pathlib
- Glob
- Shutil
- Tkinter

## 📂 Supported File Types

| Category | Extensions |
|---|---|
| Documents | `.pdf`, `.docx`, `.doc`, `.txt` |
| Spreadsheets | `.xlsx`, `.xls`, `.csv` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Videos | `.mp4`, `.mkv`, `.avi` |
| Audio | `.mp3`, `.wav` |
| Archives | `.zip`, `.rar`, `.7z` |
| Code | `.py`, `.js`, `.html`, `.css` |

## 📁 Project Structure

```text
Smart-File-Organizer/
│
├── main.py
├── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/vikneshkumarg3604/Smart-File-Organizer.git
```

### 2. Navigate to the project directory

```bash
cd Smart-File-Organizer
```

### 3. Run the application

```bash
python main.py
```

Or on Windows:

```bash
py main.py
```

## 🖥️ How It Works

1. Launch the application.
2. Select the folder you want to organize.
3. The application scans the files in the selected folder.
4. It identifies each file using its extension.
5. It creates category folders if they do not already exist.
6. It moves the files into their corresponding folders.

### Example

**Before organization:**

```text
Downloads/
│
├── report.pdf
├── image.jpg
├── data.xlsx
├── video.mp4
└── project.py
```

**After organization:**

```text
Downloads/
│
├── Documents/
│   └── report.pdf
│
├── Images/
│   └── image.jpg
│
├── Spreadsheets/
│   └── data.xlsx
│
├── Videos/
│   └── video.mp4
│
└── Code/
    └── project.py
```

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

- Python file and directory handling.
- Working with file paths using `os` and `pathlib`.
- Searching files using `glob`.
- Moving files using `shutil`.
- Using dictionaries and nested loops.
- Automating repetitive file management tasks.
- Debugging file and directory operation errors.

## 🔮 Future Enhancements

- Add support for additional file extensions.
- Handle duplicate filenames.
- Add an `Others` category for unsupported file types.
- Implement error handling and logging.
- Add a preview mode before moving files.
- Build a graphical user interface.

## 👨‍💻 Author

**Viknesh Kumar G.**

This project was developed as part of my hands-on learning journey in Python programming and automation.

## 📄 License

This project is open-source and available for learning and educational purposes.
# Smart File Organizer & Automation Tool

A Python command-line utility built with Object-Oriented Programming (OOP) to clean up messy directories. It scans a target folder, categorizes files by their extensions, prevents accidental data loss from duplicate names, and keeps a record of all moved files.

## Key Features
- **Object-Oriented Design:** Core logic is encapsulated inside a clean, reusable `FileOrganizer` class (`organizer.py`).
- **Automatic Categorization:** Sorts files into five main folders based on extension:
  - **Images:** `.jpg`, `.jpeg`, `.png`
  - **Documents:** `.pdf`, `.docx`, `.txt`
  - **Videos:** `.mp4`, `.mkv`
  - **Python Files:** `.py`
  - **Others:** Any other file types
- **Duplicate File Protection:** Checks if a file already exists in the destination folder before moving. If a match is found, it automatically renames the incoming file (e.g., `photo_1.jpg`) instead of overwriting the original.
- **Preview Mode:** Allows you to preview where each file will go before making any actual changes to your disk.
- **Activity Logs & Summary Report:** Generates a `summary_report.txt` with total file counts per category and appends every action with timestamps to `file_management.log`.

## Project Structure
```text
├── .vscode/             # VS Code workspace settings and launch configurations
├── screenshots/         # Screenshots demonstrating the tool in action
├── app.py               # Main entry point for user interaction
├── organizer.py         # Contains the FileOrganizer class and core logic
├── file_management.log  # Detailed log of moved files
├── summary_report.txt   # Summary count of processed files
└── README.md            # Project documentation
```

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   

   cd "SMART FILE ORGANISER & AUTOMOTION TOOL"
   ```

2. **Set up a virtual environment (Recommended):**
   Make sure you have Python 3.x installed, then create and activate a virtual environment:
   ```bash
   python -m venv .venv
   
   # On Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```
   *(Note: This project uses Python's built-in `os`, `shutil`, `logging`, and `datetime` modules, so no external third-party packages are required.)*

## Safe Testing Guide
Before running this script on an important folder like your personal `Downloads` directory, test it in an isolated folder:

1. Create a temporary folder on your Desktop (for example, `TestFolder`).
2. Add a few sample files with different extensions (e.g., `photo.jpg`, `document.pdf`, `sample.txt`, `video.mp4`, `script.py`, and `archive.zip`).
3. To test duplicate handling, add another file with the exact same name (like a second `photo.jpg`) after the first run.

## How to Run

1. Run the main application script from your terminal:
   ```bash
   python app.py
   ```
2. When prompted, paste the **absolute path** of your target folder (e.g., `C:\Users\User\Desktop\TestFolder`).
3. Choose whether to run in **Preview Mode** first (`y` to preview planned moves safely, or `n` to organize immediately).
4. Once finished, check `summary_report.txt` and `file_management.log` in the project directory for full details.

## Screenshots
*(Add screenshots of your terminal output, organized folders, and generated report inside a `screenshots` folder and link them below)*

- **Terminal Execution & Preview Mode:** `screenshots/terminal_output.png`
- **Organized Test Folder:** `screenshots/organized_folders.png`
- **Generated Summary Report:** `screenshots/summary_report.png`

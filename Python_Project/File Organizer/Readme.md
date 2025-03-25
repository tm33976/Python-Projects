# File Organizer

The **File Organizer** is a Python-based tool designed to help you manage and organize your files efficiently. It supports organizing files by their type or modification date, making your directory clean and well-structured.

## Features
- Organizes files by **File Type** (e.g., Images, Documents, Videos, Music)
- Organizes files by **Date** using their last modified timestamp
- Supports common file types such as `.jpg`, `.pdf`, `.mp4`, `.mp3`, and more
- Automatically creates folders if they don't exist
- Provides simple console-based interaction

## Prerequisites
Make sure you have Python installed on your system.

## Installation
1. Clone the repository or download the `file_organizer.py`.
2. Navigate to the directory where the script is located using the terminal or command prompt.

```bash
cd path/to/file_organizer
```

3. Install required dependencies (if not already installed):

```bash
pip install shutil
```

## Usage
1. Run the script using the following command:

```bash
python file_organizer.py
```

2. Enter the path of the directory you want to organize.
3. Choose one of the following options:
   - **1:** Organize files by File Type
   - **2:** Organize files by Date

4. The files will be moved to respective folders based on your choice.

## Example
**Before:**
```
Downloads/
├── report.docx
├── photo1.jpg
├── song.mp3
├── video.mp4
├── notes.txt
```

**After (By Type):**
```
Downloads/
├── Documents/
│   └── report.docx
├── Images/
│   └── photo1.jpg
├── Music/
│   └── song.mp3
├── Videos/
│   └── video.mp4
├── Others/
│   └── notes.txt
```


## Author
- **Tushar Mishra**
- **Email:** tm3390782@gmail.com

## License
This project is licensed under the MIT License.

---
Enjoy a cleaner directory with **File Organizer**! 🚀


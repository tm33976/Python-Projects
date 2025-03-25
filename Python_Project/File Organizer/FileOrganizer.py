import os
import shutil
from datetime import datetime

def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_file_type(extension):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar'],
    }
    for folder, extensions in file_types.items():
        if extension.lower() in extensions:
            return folder
    return 'Others'

def organize_by_type(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1]
            folder_name = get_file_type(extension)
            folder_path = os.path.join(directory, folder_name)
            create_folder(folder_path)
            shutil.move(file_path, folder_path)
            print(f"Moved: {file} -> {folder_name}")

def organize_by_date(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            modified_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(modified_time).strftime('%Y-%m')
            folder_path = os.path.join(directory, date_folder)
            create_folder(folder_path)
            shutil.move(file_path, folder_path)
            print(f"Moved: {file} -> {date_folder}")

def main():
    directory = input("Enter the directory path to organize: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    print("Choose an option:")
    print("1. Organize by File Type")
    print("2. Organize by Date")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        organize_by_type(directory)
    elif choice == '2':
        organize_by_date(directory)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

import os
import shutil

#GUI
import tkinter as tk
from tkinter import filedialog




def organize_files(directory):
    # Define file types and their corresponding folders
    file_types = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
        'Documents': ['pdf', 'docx', 'txt', 'xlsx', 'pptx'],
        'Videos': ['mp4', 'mkv', 'mov', 'avi'],
        'Music': ['mp3', 'wav', 'flac'],
        'Archives': ['zip', 'rar', 'tar', 'gz'],
        'Softwares':['exe','msi'],
    }

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = filename.split('.')[-1].lower()
            moved = False

            for folder, extensions in file_types.items():
                if extension in extensions:
                    destination_dir = os.path.join(directory, folder)
                    if not os.path.exists(destination_dir):
                        os.makedirs(destination_dir)
                    shutil.move(file_path, os.path.join(destination_dir, filename))
                    moved = True
                    break

            if not moved:
                # Move other files to an 'Others' folder
                other_dir = os.path.join(directory, 'Others')
                if not os.path.exists(other_dir):
                    os.makedirs(other_dir)
                shutil.move(file_path, os.path.join(other_dir, filename))

    print(f"Files organized in {directory}.")

# Example usage
organize_files('D:\Downloads')


#GUI

def select_directory():
    directory = filedialog.askdirectory()
    organize_files(directory)

root = tk.Tk()
root.title("File Management System")

button = tk.Button(root, text="Select Directory", command=select_directory)
button.pack()

root.mainloop()
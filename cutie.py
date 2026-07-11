#Automatic File Organizer

import os
import shutil

def organize_folder(target_dir):
    EXTENSION_MAP = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".tar", ".gz", ".rar"],
    }
    
    if not os.path.exists(target_dir):
        print("Directory not found!")
        return

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            for folder_name, extensions in EXTENSION_MAP.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(target_dir, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved: {filename} -> {folder_name}")
                    break


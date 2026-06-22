import os
import shutil

TARGET_DIR = "./my_downloads_folder"
EXT_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".pdf", ".docx", ".txt", ".xlsx"],
    "Media": [".mp3", ".mp4", ".mkv"],
}


def organize_folder(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        for folder_name, extensions in EXT_MAPPING.items():
            if ext.lower() in extensions:
                dest_folder = os.path.join(directory, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                break


if __name__ == "__main__":
    os.makedirs(TARGET_DIR, exist_ok=True)
    organize_folder(TARGET_DIR)
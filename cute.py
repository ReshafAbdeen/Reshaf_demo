import datetime
import shutil

folder_to_backup = "./my_project"
backup_name = f"backup_{datetime.date.today()}"

try:
    shutil.make_archive(backup_name, "zip", folder_to_backup)
    print("--- Backup Successful ---")
    print(f"Created: {backup_name}.zip")
except Exception as e:
    print(f"Backup failed: {e}")
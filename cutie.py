







    


import os
import sys
import paramiko


def sftp_upload_file(local_path, remote_path, hostname, username, password):
    """Uploads a local file to a remote server using SFTP."""

    if not os.path.exists(local_path):
        print(f" Local file error: '{local_path}' does not exist.")
        return

    print(f"Connecting to remote server {hostname}...")

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(
            hostname=hostname, port=22, username=username, password=password
        )
        print("SSH Connection established.")

        sftp = ssh.open_sftp()
        print(f"Uploading '{local_path}' to '{remote_path}'...")

        sftp.put(local_path, remote_path)
        print("✅ Upload complete!")

        sftp.close()
        ssh.close()
        print("Connections closed cleanly.")

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username/password.")
    except paramiko.SSHException as ssh_err:
        print(f"SSH error occurred: {ssh_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    SERVER_IP = "192.168.1.50"  
    USER = "my_username"
    PASS = "my_password"

    LOCAL_FILE = "my_report.txt"
    REMOTE_DESTINATION = "/home/my_username/backups/my_report.txt"

    sftp_upload_file(LOCAL_FILE, REMOTE_DESTINATION, SERVER_IP, USER, PASS)
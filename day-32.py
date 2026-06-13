import os
from tkinter import Button, Label, Tk, filedialog, messagebox


class FileUploaderApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Python Local File Processor")
        self.root.geometry("400x200")

        self.label = Label(
            root, text="Select a file to 'upload' into the system:"
        )
        self.label.pack(pady=20)

        self.upload_btn = Button(
            root, text="Browse & Upload File", command=self.process_file
        )
        self.upload_btn.pack(pady=10)

        self.status_label = Label(root, text="", fg="green")
        self.status_label.pack(pady=10)

    def process_file(self):
        file_path = filedialog.askopenfilename(
            title="Select File",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
        )

        if not file_path:
            return

        file_name = os.path.basename(file_path)
        self.status_label.config(
            text=f"Processing: {file_name}...", fg="blue"
        )

        messagebox.showinfo(
            "Success", f"File '{file_name}' successfully loaded into Python!"
        )

        self.status_label.config(text=f"✅ Loaded: {file_name}", fg="green")


if __name__ == "__main__":
    root = Tk()
    app = FileUploaderApp(root)
    root.mainloop()
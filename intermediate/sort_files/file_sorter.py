import os
from pathlib import Path
import shutil
import customtkinter as ctk
from tkinter import filedialog


class FolderSorter:
    def __init__(self):
        self.filepath = None
        self.window = ctk.CTk()
        self.window.title("File Sorter")

        # self.src: Path = Path("sample_folder")
        self.src: Path = Path(os.getcwd())

        self.window.geometry('2000 * 2000')
        self.padding: dict = {'padx': 20, 'pady': 20}

        self.font = ctk.CTkFont(size=18)
        self.header_lbl = ctk.CTkLabel(self.window, text="Select the folder to sort",
                                       compound="center", font=self.font)
        self.header_lbl.grid(row=2, column=1, **self.padding)

        # bg_color='white', fg_color='black'
        self.filename_lbl = ctk.CTkLabel(self.window, text='')
        self.filename_lbl.grid(row=3, column=0, columnspan=2, **self.padding)

        self.dir_btn = ctk.CTkButton(self.window,
                                     text='Browse', command=self.open_file_dialogue)
        self.dir_btn.grid(row=3, column=3, columnspan=2, **self.padding)

        self.sort_btn = ctk.CTkButton(self.window, command=self.sort_files,
                                      text="Sort Files", compound="left")
        self.sort_btn.grid(row=5, column=1, columnspan=3, **self.padding)

        self.msg_lbl = ctk.CTkLabel(self.window, text='')
        self.msg_lbl.grid(row=6, column=1)

    def run(self):
        self.window.mainloop()

    def open_file_dialogue(self):
        self.filepath = filedialog.askdirectory(title="Select folder", initialdir=self.src)
        if self.filepath:
            self.filename_lbl.configure(text=self.filepath.title())

    def sort_files(self):
        msg: str = ''

        try:
            folderName: Path = Path(self.filename_lbl.cget("text"))
            for root, dirs, files in os.walk(folderName):
                if Path(root) != folderName:
                    for file in files:
                        source = Path(os.path.join(root, file))
                        dest = Path(os.path.join(folderName, file))
                        shutil.move(source, dest)

            for file in os.listdir(folderName):
                name, ext = os.path.splitext(file)
                nf = f"{os.path.join(folderName, ext[1:])} files"
                if not os.path.exists(nf):
                    os.makedirs(nf)
                source = os.path.join(folderName, file)
                dest = os.path.join(nf, file)
                shutil.move(source, dest)
            self.delete_empty_folders(folderName)
            msg = "Files are sorted successfully!!!"
        except Exception as e:
            print(e)
            msg = "Technical issue occurred!!!"
        finally:
            self.msg_lbl.configure(text=msg)

    def delete_empty_folders(self, filepath):
        try:
            # filepath: Path = Path(self.filename_lbl.cget("text"))
            for root, dirs, files in os.walk(filepath):
                if len(dirs) == 0 and len(files) == 0:
                    os.removedirs(root)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    fs = FolderSorter()
    fs.run()

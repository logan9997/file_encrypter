import os
import time
import cryptography

from general import *

class SearchFolders():

    def __init__(self, path:str, **skipped_folders:list):
        self.files:list = []
        self.directories:list = os.listdir(path)
        self.skipped_folders:tuple = skipped_folders.get("skipped_folders", ())


    def extract_folders(self, directories:list, path:str):
        folders = []
        for directory in directories:
            full_path = path + "\\" + directory

            if os.path.isdir(full_path):
                folders.append(directory)
            else:
                self.files.append(full_path)
        return folders


    def parse_through_folders(self, initial_path:str, folders:list):

        folders = self.extract_folders(folders, initial_path)
        for folder in folders:
            path = initial_path + "\\" + folder 

            if folder in self.skipped_folders:
                continue

            try:
                folder_content = os.listdir(path)
                if os.path.isdir(path):
                    folder_content = os.listdir(path) 
                    folder_content = self.extract_folders(folder_content, path)

                path:str = path.replace(f"\\{folder}", "")
                try:
                    self.parse_through_folders(path + "\\" + folder, folder_content)    
                except RecursionError:
                    pass
            except PermissionError:
                pass


    def setup_search_files(self):
        return self.files


class SearchFiles():

    def __init__(self, files:list):
        self.files:list = files

       
    def loop_through_files(self):
        converted_count = 0
        num_files = len(self.files)
        for file in self.files:
            print(f"{str(converted_count)} / {str(num_files)} converted", end="\r")
            try:
                c = cryptography.Cryptography()
                c.file_setup(file)
                c.open_file()
                c.convert_file_data()
                c.rewrite()
                c.rename_file()
                converted_count += 1
            except FileNotFoundError:
                print("FILE NOT FOUND", file)


def main():

    print("""
        \r    ##############################################\n    Python File Encypter. Version 1.0\n    Created by Logan Baxter.
        \n    Please be AWARE that this program is currenlty 
        \r    still under development, with the potential for\n    bugs to occur. Type '/?' for help'\n    ##############################################\n""")

    base_path = os.path.expanduser('~') + "\\onedrive\\documents"

    rewrite_choice = input("Commit (en/de)cryption to files? (Y/N): " ).upper()
    paths = add_paths(base_path)

    start_time = time.time()
    
    for path in paths:
        folders = SearchFolders(path, skipped_folders=("My Games", "AppData", "Personal"))
        folders.parse_through_folders(initial_path=path, folders=os.listdir(path))
        files = folders.setup_search_files()
        
        scan_files = SearchFiles(files)
        if rewrite_choice == "Y":
            scan_files.loop_through_files()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"############################ COMPLETED IN: {round(total_time, 2)} SECONDS ###########################")
    
    
if __name__ == "__main__":
    main()

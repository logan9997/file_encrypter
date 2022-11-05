import os


def add_paths(base_path:str):
    paths = []
    while True:
        new_path = base_path + "\\" + input(f"select path ('.' to ESC) - {base_path}\\")
        while not os.path.exists(new_path):
            print("path does not exist...")
            new_path = base_path + "\\" + input(f"select path ('.' to ESC) - {base_path}\\")

        if "."  in new_path:
            return paths

        paths.append(new_path)
        add_another = input("Add Another path? (Y/N)").upper()

        if add_another != "Y":
            return paths
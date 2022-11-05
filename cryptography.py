import os

class Cryptography():

    def __init__(self):
        self.num = 1

        
    def file_setup(self, file):
        self.file:str = file
        if "_ENCRYPTED_" in self.file:
            self.value_change = self.num  
            self.new_file_name = "".join(self.file.split("_ENCRYPTED_"))
        else:
            self.value_change = -self.num
            self.new_file_name = self.file.split(".")[0] + "_ENCRYPTED_." + self.file.split(".")[1]


    def open_file(self):
        with open(self.file, "rb") as f:
            self.content = f.read()


    def convert_file_data(self):
        self.new_values = bytes((i + self.value_change) % 256 for i in self.content)


    def rewrite(self):  
        try: 
            with open(self.file, "wb") as f:
                f.write(self.new_values)
        except PermissionError:
            pass


    def rename_file(self):
        os.rename(self.file, self.new_file_name)




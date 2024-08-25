#Herramienta de eliminacion segura de archivos multimedia en (Android/Linux/Windows/macOS)

from cryptography.fernet import Fernet
from sys import argv
from os import remove, urandom, path

def delete_secure(path_local):
    overwrite = urandom(1024)
    for _ in range(2):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        key = overwrite
        del(key)
        with open(path_local,'rb') as read_local:
            file_read=read_local.read()
        encryption = fernet.encrypt(file_read)
        file_read = encryption
        del(file_read)
        fernet = overwrite
        del(fernet)
        with open(path_local,'wb') as write_local:
            write_local.write(encryption)
    remove(path_local)
    print("safely deleted file!")
    return
          
def delete_lite(path_local):
    #method not recommended because it does not guarantee complete overwriting 
    overwrite = urandom(2048)
    with open(path_local,'wb') as lite:
        for _ in range(1200):
            lite.write(overwrite)
        lite.truncate(1024)
    remove(path_local)
    print("File overwritten and deleted")
    return

def show_help():
    print("""
Cleaning: is a tool that allows you to safely delete multimedia files.
Usage:
    python3 cleaning.py -s  option that allows me to securely delete multimedia files (RECOMMENDED)
    python3 cleaning.py -l  option only when the multimedia file is very large and from a smartphone
    python3 cleaning.py [-h,--help]  print help menu
          """)


def data_entry():                                                                                 
   path_directory = input("Enter the path where your file is: ")                         
   file_name = input("Enter file name: ")
   if "'" in file_name:
        file_name = file_name.replace("'", "")
        path_local = path.join(path_directory, file_name)
        return path_local

   else:
        path_local = path.join(path_directory, file_name)
        return path_local

def main():
 try:
   if "-h" in argv or "--help" in argv:
            show_help()
   elif "-s" in argv:
            path_local = data_entry()
            delete_secure(path_local)
   elif "-l" in argv:
            path_local = data_entry()
            delete_lite(path_local)
                      
 except (KeyboardInterrupt,EOFError):
          print("\nOperation canceled by user!")
 except FileNotFoundError:
          print("Non-existent route!")
 except PermissionError:
          print("You do not have permissions on that file!")
 except IsADirectoryError:        
          print("Please enter a file name, not a directory!")
           
if __name__ == "__main__":
       main()

__name__="cleaning"
__version__="1.0"
__author__="WhiteHack"
__status__="Finish"

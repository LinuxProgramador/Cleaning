#Secure Media File Deletion Tool on (Android/Linux/Windows/macOS)

from sys import argv
from os import remove, urandom, path
        
def delete_secure(path_local):
    size = path.getsize(path_local)
    with open(path_local,'wb') as lite:
        for _ in range(size):
           lite.write(urandom(512))
    remove(path_local)
    print("File overwritten and deleted")


def show_help():
    print("""
Cleaning: is a tool that allows you to safely delete multimedia files.
Usage:
    python3 cleaning.py -s  option that allows me to securely delete multimedia files.
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

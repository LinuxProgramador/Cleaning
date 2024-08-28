#Secure Media File Deletion Tool on (Android/Linux/Windows/macOS)

from sys import argv, exit
from os import remove, urandom, path
from psutil import disk_usage
from platform import system

def disk_space():
    if system() in ["Linux","Darwin"]:
        disk_linux_and_macOS = disk_usage("/")
        return f"{disk.free / 1024**3 :.2f}"

    elif system() == "Windows":
        disk_windows = disk_usage("C:\\")
        return f"{disk.free / 1024**3 :.2f}"
    else:
         path = '/storage/emulated'
         stat = statvfs(path)
         return f"{stat.f_frsize * stat.f_bavail / (1024**3):.2f}"


def delete_secure(path_local):
    size = path.getsize(path_local)
    sizes_kb = size / 1024
    sizes_mb = sizes_kb / 1024
    if size >= 0 and sizes_kb <= 1024:
          salt = 1000
    elif sizes_mb >= 1 and sizes_mb <= 59:
          salt = 30000
    elif sizes_mb >= 59  and sizes_mb <= 235:
          salt = 120000
    elif sizes_mb >= 235 and sizes_mb <= 587:
          salt = 300000
    elif  sizes_mb >=587  and sizes_mb <= 978:
          salt = 500000
    elif sizes_mb >= 978 and sizes_mb <= 2000:
          salt = 1000000
    elif sizes_mb >= 2000 and sizes_mb <= 4400:
          salt = 2300000
    elif sizes_mb >= 4400 and sizes_mb <= 6200:
          salt = 3200000
    elif sizes_mb >= 6200 and sizes_mb <= 9600:
          salt = 5000000
    elif sizes_mb >= 9600 and sizes_mb <= 12000:
          salt = 6200000
    else:
         print("You have exceeded the maximum allowed length which is 12G ")
    with open(path_local,'wb') as lite:
        for _ in range(salt):
          lite.write(urandom(2048))
    remove(path_local)
    print("File overwritten and deleted!")


def show_help():
    print("Cleaning 1.0: is a tool that allows you to safely delete multimedia files.")
    print("""
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
          print('')
 except FileNotFoundError as e:
          print(f"Non-existent route => {e}")
 except PermissionError as p:
          print(f"You do not have permissions on that file => {p}")
 except IsADirectoryError:        
          print("Please enter a file name, not a directory!")
           
if __name__ == "__main__":
       main()

__name__="Cleaning"
__version__="1.0"
__author__="WhiteHack"
__status__="Finish"

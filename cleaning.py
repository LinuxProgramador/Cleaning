#Secure Media File Deletion Tool on (Android/Linux/macOS)

from sys import argv, exit
from os import remove, urandom, path, statvfs
from platform import system

def disk_space():
    if system() in ["Linux","Darwin"]:
        path_disk = '/'
        stat = statvfs(path_disk)
        return float(f"{stat.f_frsize * stat.f_bavail / (1024**3):.2f}")
    else:
         path_disk = '/storage/emulated'
         stat = statvfs(path_disk)
         return float(f"{stat.f_frsize * stat.f_bavail / (1024**3):.2f}")


def delete_secure(path_local):
    size = path.getsize(path_local)
    sizes_kb = size / 1024
    sizes_mb = sizes_kb / 1024
    if size >= 0 and sizes_kb <= 1024:
          salt = 2
    elif sizes_mb >= 1 and sizes_mb <= 59 and sizes_mb < disk_space():
          salt = 60
    elif sizes_mb >= 59  and sizes_mb <= 235 and sizes_mb < disk_space():
          salt = 236
    elif sizes_mb >= 235 and sizes_mb <= 587 and sizes_mb < disk_space():
          salt = 588
    elif  sizes_mb >=587  and sizes_mb <= 978 and sizes_mb < disk_space():
          salt = 979
    elif sizes_mb >= 978 and sizes_mb <= 2000 and sizes_mb < disk_space():
          salt = 2001
    elif sizes_mb >= 2000 and sizes_mb <= 4400 and sizes_mb < disk_space():
          salt = 4401
    elif sizes_mb >= 4400 and sizes_mb <= 6200 and sizes_mb < disk_space():
          salt = 6201
    elif sizes_mb >= 6200 and sizes_mb <= 9600 and sizes_mb < disk_space():
          salt = 9601
    elif sizes_mb >= 9600 and sizes_mb <= 12000 and sizes_mb < disk_space():
          salt = 12001
    else:
         print("You have exceeded the maximum allowed length which is 12G or you do not have enough disk space!")
         exit(1)
    with open(path_local,'wb') as lite:
        for _ in range(salt):
          lite.write(urandom(1048576))
    remove(path_local)
    print("File overwritten and deleted!")


def show_help():
    print("Cleaning: is a tool that allows you to safely delete multimedia files.")
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
        return path.join(path_directory, file_name)
        
   else:
        return path.join(path_directory, file_name)
        

def main():
 try:
   if "-h" in argv or "--help" in argv:
            show_help()
   elif "-s" in argv:
            delete_secure(data_entry())
       
                      
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

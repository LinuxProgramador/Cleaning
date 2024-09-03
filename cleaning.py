#Secure Media File Deletion Tool on (Android/Linux/macOS)

from sys import argv, exit
from os import remove, urandom, path, statvfs
from platform import system

def disk_space():
    if system() in ["Linux","Darwin"] and not path.isdir('/data/data/com.termux/files'):
        path_disk = '/'
        stat = statvfs(path_disk)
        return float(f"{stat.f_frsize * stat.f_bavail / (1024**2):.2f}")
    elif system() == 'Linux' and path.isdir('/data/data/com.termux/files'):
         path_disk = '/storage/emulated'
         stat = statvfs(path_disk)
         return float(f"{stat.f_frsize * stat.f_bavail / (1024**2):.2f}")
    else:
         print("System not supported!")
         exit(1)
  
def delete_secure(path_local):
    size = path.getsize(path_local)
    sizes_kb = size / 1024
    sizes_mb = sizes_kb / 1024
    if size >= 0 and sizes_kb <= 1024:
          interactions = 2
    elif sizes_mb < disk_space():
          interactions = round(sizes_mb)   
    else:
         print("You do not have enough disk space!")
         exit(1)
    with open(path_local,'wb') as file_overwrite:
        overwrite = urandom(1048576)
        for _ in range(interactions):
          file_overwrite.write(overwrite)
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

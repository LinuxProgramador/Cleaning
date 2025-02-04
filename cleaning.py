#Secure Media File Deletion Tool on (Windows/Android/Linux/macOS)

from sys import argv
from os import remove, urandom, path, fsync
 
def delete_secure(path_local):
    '''
      Files are overwritten for later remove
    '''
    size = path.getsize(path_local)
    sizes_kb = size / 1024
    sizes_mb = sizes_kb / 1024
    if size >= 0 and sizes_kb <= 1024:
          interactions = 2
    else:
          interactions = round(sizes_mb)   
    for _ in range(4):
      with open(path_local,'wb') as file_overwrite:
        overwrite = urandom(1048576)
        for _ in range(interactions):
          file_overwrite.write(overwrite)
          file_overwrite.flush()
          fsync(file_overwrite.fileno())
    remove(path_local)
    print("File overwritten and deleted!")


def show_help():
    '''
       Help menu is set 
    '''
    print("Cleaning: is a tool that allows you to safely delete multimedia files.")
    print("""
Usage:
    python3 cleaning.py -s  option that allows me to securely delete multimedia files.
    python3 cleaning.py [-h,--help]  print help menu
          """)


def data_entry(): 
   '''
     Validates the existence of quotes in file names 
   '''
   path_directory = input("Enter the path where your file is: ")                         
   file_name = input("Enter file name: ")
   if "'" in file_name or "\"" in file_name:
        file_name = file_name.replace("'", "").replace("\"", "")
        return path.join(path_directory, file_name)
   else:
        return path.join(path_directory, file_name)
        

def main():
 '''
   Performs tasks based on what the user selects 
 '''
 try:
   if "-h" in argv or "--help" in argv:
      show_help()
   elif "-s" in argv:
      delete_secure(data_entry())
   else:
      print("Cleaning: invalid arguments. Try --help for more information.")
       
 except (KeyboardInterrupt,EOFError):
          print('')
 except FileNotFoundError as e:
          print(f"Non-existent route => {e}")
 except PermissionError as p:
          print(f"You do not have permissions on that file => {p}")
 except IsADirectoryError:        
          print("Please enter a file name, not a directory!")
 except OSError as o:
          print(f"Error: {o}")
  
if __name__ == "__main__":
       main()

__name__="Cleaning"
__version__="1.0"
__author__="JP Rojas"
__status__="Finish"

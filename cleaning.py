#Secure Media File Deletion Tool on (Windows/Android/Linux/macOS)

from math import ceil
from sys import argv
from os import remove, urandom, path, fsync, listdir

confirm_delete_old = None
num_overwrites_old = None
counter = 0

def delete_secure(path_local):
    '''  Files are overwritten for later remove '''
    global counter,confirm_delete_old,num_overwrites_old
    
    if counter == 0:
      confirm_delete = input("Do you want to remove the files after overwriting them (y/n): ").strip().lower()
      num_overwrites = int(input("Number of overwrites: "))
        
    else:
      confirm_delete = confirm_delete_old
      num_overwrites = num_overwrites_old 
        
    num_overwrites = 4 if not (1 <= num_overwrites <= 15) else num_overwrites
    confirm_delete = "y" if not confirm_delete else confirm_delete
    size = path.getsize(path_local)
    sizes_kb = size / 1024
    sizes_mb = sizes_kb / 1024
    
    if size >= 0 and sizes_kb <= 1024:
          interactions = 2
        
    else:
          interactions = ceil(sizes_mb)
        
    for _ in range(num_overwrites):
      with open(path_local,'wb') as file_overwrite:
        overwrite = urandom(1048576)
          
        for _ in range(interactions):
          file_overwrite.write(overwrite)
            
        file_overwrite.flush()
        fsync(file_overwrite.fileno())
          
    if confirm_delete == "y":
       remove(path_local)
        
    confirm_delete_old = confirm_delete
    num_overwrites_old = num_overwrites
    counter += 1
    
def show_help():
    ''' Help menu is set '''
    print("Cleaning: is a tool that allows you to safely delete multimedia files.")
    print("""
Usage:
    python3 cleaning.py -s  option that allows me to securely delete multimedia files.
    python3 cleaning.py -R  an option to delete multiple files in a directory at once.
    python3 cleaning.py [-h,--help]  print help menu
          """)


def data_entry(file_name,path_directory):
   ''' Validates the existence of quotes in file names '''
   if not file_name:
     path_directory = input("Enter the path where your file is: ").strip()
     file_name = input("Enter file name: ").strip()
       
   if "'" in file_name or "\"" in file_name:
        file_name = file_name.replace("'", "").replace("\"", "")
        return path.join(path_directory, file_name)
       
   else:
        return path.join(path_directory, file_name)


def main():
 ''' Performs tasks based on what the user select '''
 file_name = path_directory = ''
 try:
   if any(help in argv for help in ["-h","--help"]):
      show_help()
       
   elif "-s" in argv:
      delete_secure(data_entry(file_name,path_directory))
       
   elif "-R" in argv:
      path_directory = input("Enter the path of the files to delete securely: ").strip()
      files = [file for file in listdir(path_directory) if path.isfile(path.join(path_directory,file))]
      for file_name in files:
          delete_secure(data_entry(file_name,path_directory))   
          
   else:
      print("Cleaning: invalid arguments. Try --help for more information.")

 except (KeyboardInterrupt,EOFError):
          print()
 except FileNotFoundError as e:
          print(f"Non-existent route => {e}")
 except PermissionError as p:
          print(f"You do not have permissions on that file => {p}")
 except IsADirectoryError:
          print("Please enter a file name, not a directory!")
 except Exception as f:
          print(f"Type Error: {f}")

if __name__ == "__main__":
       main()

__name__="Cleaning"
__version__="1.0"
__author__="JP Rojas"
__status__="Finish"

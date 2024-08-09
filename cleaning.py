#!/usr/bin/python3 

#Herramienta de eliminacion segura de archivos en (Linux/Windows/macOS)

from cryptography.fernet import Fernet
from sys import argv
from os import remove

def delete_secure(path):
          for _ in range(1):
              key = Fernet.generate_key()
              fernet = Fernet(key)
              key = None
              with open(path,'rb') as read:
                file_read=read.read()
              encryption = fernet.encrypt(file_read)
              fernet = None
              with open(path,'wb') as write:
                write.write(encryption)
          remove(path)
          print("safely deleted file!")
          
          

def show_help():
          print("""
Cleaning: is a tool that allows you to safely delete multimedia files.
Usage:
    python3 cleaning -f  option to delete multimedia files
Help:
    -h --help  show help menu
               """)


def main():
 try:
   if "-h" in argv or "--help" in argv:
            show_help()
         
   elif "-f" in argv:
            path_directory = input("Enter the path where your file is: ")
            file_name = input("Enter file name: ")
            if "'" in file_name:
                file_name = file_name.replace("'", "")
                path = path_directory + file_name
                delete_secure(path)
                    
            else:
                path= path_directory + file_name
                delete_secure(path)


 except (KeyboardInterrupt,EOFError):
          print("\noperation canceled by user!")
          
 except FileNotFoundError:
          print("non-existent route!")
          
 except PermissionError:
          print("You do not have permissions on that file!")
          

if __name__ == "__main__":
       main()


__name__="cleaning"
__version__="1.0"
__author__="WhiteHack"
__status__="Finish"

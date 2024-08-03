
from cryptography.fernet import Fernet
from sys import argv
from os import remove



#Herramienta de eliminacion segura de archivos en (Linux/Windows/macOS)



def delete_secure(path):
          for _ in range(1):
              key = Fernet.generate_key()
              fernet = Fernet(key)
              key = ""
              with open(path,'rb') as read:
                file_read=read.read()
              encryption = fernet.encrypt(file_read)
              fernet = ""
              with open(path,'wb') as write:
                write.write(encryption)
            remove(path)
            print("safely deleted file!")
          return




def main():
 try:
   if "-h" in argv or "--help" in argv:
         print("Cleaning: is a tool that allows you to safely delete multimedia files.")
         print("""
Usage:
    Examples:
    python3 cleaning -f  option to delete multimedia files
Help:
    -h --help  show help menu
               """)
         
   elif "-f" in argv:
            path_directory,file_name=input("Enter the path where your file is: "),input("Enter file name: ")
            quotation_marks =["'","\""]
            if file_name in quotation_marks:
               file_name = file_name.replace(quotation_marks, "", 2)
                path = path_directory + file_name
                delete_secure(path)
                    
            else:
                path= path_directory + file_name
                delete_secure(path)


 except (KeyboardInterrupt,OEFError):
          print()
          
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

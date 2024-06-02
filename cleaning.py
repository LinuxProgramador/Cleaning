
from cryptography.fernet import Fernet
from sys import argv,exit
from os import remove
from re import search


#Herramienta de eliminacion segura de archivos en (Linux/Windows/macOS)



def delete_secure(path):


         try:

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

         except FileNotFoundError:
             print("non-existent route!")
             exit(2)

         except PermissionError:
                print("You do not have permissions on that file!")
                exit(2)

         return




def main():

 try:

   for input_user in argv:

      if input_user in ["-h","--help"]:

         print("Cleaning: is a tool that allows you to safely delete multimedia files.")
         print("""
Usage:

    Examples:
    python3 cleaning -f  option to delete multimedia files

Help:

    -h --help  show help menu
               """)
         exit(2)


      elif input_user == "-f":


            path_directory,file_name=input("Enter the path where your file is: "),input("Enter file name: ")
            pattern_quote = r"\'"


            if search(pattern_quote, file_name):

               file_name = file_name.replace("'", "", 2)
               path = path_directory + file_name

            else:
                path= path_directory + file_name
                delete_secure(path)


 except KeyboardInterrupt:
          print()
          exit(2)






if __name__ == "__main__":
       main()


__name__="cleaning"
__version__="1.0"
__author__="WhiteHack"
__status__="Finish"

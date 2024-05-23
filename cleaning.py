from cryptography.fernet import Fernet
import sys
from os import remove,urandom

#Herramienta de eliminacion segura de archivos en (Linux/Windows/macOS)


def main():

 try:

   for input_user in sys.argv:
      if input_user in ["-h","--help"]:

         print("Cleaning: is a tool that allows you to safely delete multimedia files.")
         print("""
Usage:

    Examples:
    python3 cleaning -f  option to delete multimedia files

Help:

    -h --help  show help menu
               """)
         sys.exit(2)


      elif input_user == "-f":

         try:
            path=input("path of the file delete: ")
            salt = urandom(512)
            key = Fernet.generate_key()
            fernet = Fernet(key)
            key = salt

            file_local=open(path,'rb')
            file_read=file_local.read()
            file_local.close()
            encryption = fernet.encrypt(file_read)
            fernet = salt

            file_local_write=open(path,'wb')
            file_local_write.write(encryption)
            file_local_write.close()

            remove(path)
            print("safely deleted file!")

         except FileNotFoundError:
             print("non-existent route!")
             sys.exit(2)

         except PermissionError:
                print("You do not have permissions on that file!")
                sys.exit(2)


 except KeyboardInterrupt:
          print()
          sys.exit(2)



 return


if __name__ == "__main__":
       main()


__name__="cleaning"
__version__="1.0"
__author__="WhiteHack"
__status__="Finish"

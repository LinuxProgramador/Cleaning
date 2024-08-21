Tool that allows you to delete multimedia files without the possibility of recovery.

Program functionality: What it does is read the multimedia file in binary, then creates a secure key with the Fernet function and encrypts the multimedia file in binary in the ram with AES-128, then overwrites the file with the same file already encoded and deletes it, guaranteeing that even if it is recovered, it is not readable

Windows: 

cleaning.exe

directory path 

[here we enter the path of the directory where the file to be deleted is] 

file name 

[here we enter the name of the file to delete]


Linux: 

In GNU/Linux distributions derived from Debian

./dependencies.sh

python3 cleaning.py options [-h,--help,-f]

And in other GNU/Linux distros 

Install dependencies

python3 python3-pip 

python3 -m pip install cryptography

python3 cleaning.py options [-h,--help,-f]

macOS:

  install the 
     
  wine emulator and 
    
   run 
    
   cleaning.exe


Android:

 termux:

   install kali or Ubuntu on 
  
   termux 
  
   Installation link: https://github.com/MasterDevX/Termux-Kali

   then install 

   python3.11-venv on kali

   and run this command at home

   python3 -m venv path/to/venv

   to install cryptography

   with path/to/venv/bin/pip install cryptography

   ./dependencies.sh

   to run cleaning.py

   path/to/venv/bin/python3 cleaning.py options [-h,--help,-f]


 userland:

   just choose the Ubuntu distro 

   ./dependencies.sh
   

   python3 cleaning.py options [-h,--help,-f]

Tool that allows you to delete multimedia files without possibility of recovering the contents of the file.

Program functionality: What it does is read the multimedia file in binary, then creates a secure key with the Fernet function and encrypts the multimedia file in binary in the ram with AES-128, then overwrites the file with the same file already encoded and deletes it, guaranteeing that even if it is recovered, it is not readable

Windows: 

install python3 from this link: https://www.python.org/downloads/

install pip from this link https://pip.pypa.io/en/stable/cli/pip_download/

install the cryptography package with: pip install cryptography

to run the program from the console: python cleaning.py [-h,--help,-f]

Linux: 

In GNU/Linux distributions derived from Debian

./dependencies.sh

python3 cleaning.py options [-h,--help,-f]

And in other GNU/Linux distros 

Install dependencies

(python3/python3-pip)

python3 -m pip install cryptography

python3 cleaning.py options [-h,--help,-f]

macOS:

 Open terminal and run this command: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

 brew install python 

 pip3 install criptography 
 
 python cleaning.py [-h,--help,-f]

 
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

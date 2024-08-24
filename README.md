Tool that allows you to delete multimedia files without the possibility of recovering the content of the file. 

Program functionality: Reads the multimedia file in binary,
then creates a secure key with the Fernet function and encrypts the multimedia file in binary in RAM with AES-128 .
It then overwrites the file with the already encrypted file and deletes it, ensuring that even if it is recovered, it is not readable.

NOTE: The -l option does not guarantee complete overwriting as is the case with -s

Installation instructions:

Windows:

  Install Python 3 from this link: https://www.python.org/downloads/
  
  Install pip from this link: https://pip.pypa.io/en/stable/cli/pip_download/
  
  Open the console (cmd) and run: pip install cryptography
  
  To run the program from the console, 
  
  use: python cleaning.py [-h,--help,-s,-l]


Linux:

  On GNU/Linux distributions derived from Debian:
  
  Run ./dependencies.sh
  
  Run: python3 cleaning.py  [-h,--help,-s,-l]

  On other distributions GNU/Linux:
  
  Install dependencies (python3/python3-pip).
  
  Execute: python3 -m pip install cryptography
  
  Execute: python3 cleaning.py [-h,--help,-s,-l]



macOS:

  Open the terminal and execute: / bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  
  Install Python with: brew install python
  
  Install cryptography with: pip3 install cryptography
  
  Run the program with: python cleaning.py [-h,--help,-s,-l]



Android:

 Termux:
 
  Install Kali or Ubuntu on Termux from the following link: https://github.com/MasterDevX/Termux-Kali
  
  Install python3.11-venv on Kali.
  
  Run: python3 -m venv path/to/venv
  
  To install cryptography: path/to/venv/bin/pip install cryptography 
  
  Run: path/to/venv/bin/python3 cleaning.py [-h,--help,-s,-l]

 Userland:
 
  Choose the Ubuntu distribution.
  
  Execute: ./dependencies.sh
  
  Execute the program with: 
  
  python3 cleaning.py [-h,--help,-s,-l]

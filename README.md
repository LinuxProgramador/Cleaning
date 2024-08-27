Tool that allows you to delete multimedia files without the possibility of recovering the content of the file. 

Installation instructions:

Windows:

  Install Python 3 from this link: https://www.python.org/downloads/
   
  Download the zip file from the Github repository 

  extract it with WinRAR 

  open the console, I have to go to the route where the Cleaning directory is

  cd Cleaning
  
  use: python cleaning.py [-h,--help,-s]


Linux:
 
  Install dependencies (python3,git)

  git clone https://github.com/LinuxProgramador/Cleaning

  cd Cleaning
  
  Execute: python3 cleaning.py [-h,--help,-s]



macOS:

  Open the terminal and execute: / bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  
  Install Python with: brew install python

  Install git 
  
  git clone https://github.com/LinuxProgramador/Cleaning

  then go into the Cleaning directory
  
  Run the program with: python cleaning.py [-h,--help,-s]



Android:

 Install termux from f-droid.org
 
 update packages:  apt update && apt upgrade -y

 Install git: apt install git -y

 Install python3 on termux: apt install python3 -y

 git clone https://github.com/LinuxProgramador/Cleaning

 cd Cleaning
 
 Execute: python3 cleaning.py [-h,--help,-s]
  

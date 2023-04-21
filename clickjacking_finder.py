#!/usr/bin/env python3
# Version: v1.0.0 @2023

###########################################
#    Author: Mirabbas Aghalarov           #
#    Youtube: mirabbasaghalarov           #
#    Instagram: 1mirabbas                 #
#    Linkedin: mirabbasagalarov           #
#    Email: mirabbasagalarov0@gmail.com   #
###########################################


def prCyan(skk):print("\033[96m{}\033[00m".format(skk))

prCyan('''
  ____    _ _____ 
 / ___|  | |  ___|
| |   _  | | |_   
| |__| |_| |  _|  
 \____\___/|_|    
              
  Click Jacking Finder           
       Author: Mirabbas Aghalarov                           
''')


import sys
import subprocess as sp

if(len(sys.argv) != 2):
     print("Incorrect Usage")
     print("Usage: python3 click.py <file containing subdomains>")
     sys.exit()

sp.run("mkdir poc", shell=True)
inputFile = open(sys.argv[1],"r")
i=1

for line in inputFile:
     line=line.rstrip("\n")

     content="<html>\n<head>\n<title>Clickjacking PoC</title>\n</head>\n<body>\n<h3>CLICK JACKING</h3>\n"
     content+="<h1>"+line+"</h1>\n"
     content+="<iframe src=\""
     content+=line+"\" width=100% height=100% style=\"opacity: 0.5;\"></iframe>"
     content+="\n</body>\n</html>"

     outFileName="poc/"
     outFileName+="file"+str(i)+".html"
     i+=1
     outFile=open(outFileName,"w")
     outFile.write(content)
     outFile.close()
     
     content=""

inputFile.close()


#!/usr/bin/env python

# Emmanuel Kardaras
# Phil King

import re
import sys
import pandas as pd

def save_to_csv(list_buff) :

    results = input("Enter csv name: ")
    row = pd.DataFrame(list_buff, columns=["SrcIP"])    #Stores list in dataframe, then converts to CSV
    row.to_csv(results, index=False)
    print("Data successfully written to "+results)

def regex_ip_parser(file) :

   for line in file.readlines() :
      ipRegex = re.findall(r'(?:SRC)\=(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\w', line) #Parses IPtables log entries
      rm_duplicates(ipRegex)

def rm_duplicates(IPs) : #Removes duplicates, saves data into set

   for IP in IPs :
      if IP not in set_buff :
         set_buff.add(IP)
   return set_buff

try :

   set_buff = set()
   list_buff = list()

   if len(sys.argv) == 1 :
       with open(input("Enter Filename: "),'r') as file :
          regex_ip_parser(file)

   elif len(sys.argv) == 2 :    #Checks for file as a commandline argument
       with open(sys.argv[1],'r') as file :
           regex_ip_parser(file)

   else :
       print("Too many system arguments. Exiting.")
       quit()

   for i,line in enumerate(list(set_buff)) : #Strips 'SRC=' from set
       list_buff.append(line.split("=")[1])  # By Phil
   save_to_csv(list_buff)

except IOError :
   print("Error. File not found.\nExiting.")

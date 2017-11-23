#!/usr/bin/env python

# Emmanuel Kardaras
# Phil King rumoured to have contributed 

import re
import sys
import json

def save_to_json(set_buff) :

   with open("logs.json", 'wb') as file :
      json.dump(set_buff, file)
      file.close

def regex_ip_parser(file) :

   for line in file.readlines() :
      ipRegex = re.findall(r'(?:SRC)\=(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\w', line) #Reads IPtables log entries
      rm_duplicates(ipRegex)

def rm_duplicates(IPs) :

   for IP in IPs :
      if IP not in set_buff :
         set_buff.add(IP)
         return set_buff

try :

   set_buff = set()
   list_buff = list()

   with open(raw_input("Enter Filename: "),'r') as file :
      regex_ip_parser(file)
      file.close

      for i,line in enumerate(list(set_buff)):
         list_buff.append(line.split("=")[1])
      save_to_json(list_buff)

except IOError:

   print("Error. File not found.")
   print("Exiting.")

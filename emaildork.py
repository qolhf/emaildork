from googlesearch import search
import sys 
import requests
import random
from colorama import Fore, Style
from time import sleep
try:
  data = sys.argv[1]
except:
  print(Fore.RED + "[ERROR] The arguments are incorrect!")
  sys.exit()
query = "intext: '{}' site:pastebin.com".format(data)
query2 = "filetype:sql '{}' 'INSERT INTO' -site:github.com -site:gitlab.com -site:githubusercontent.com -site:gitlab.".format(data)
query3 = "filetype:env intext:'{}'".format(data)
query4 = 'filetype:xls inurl:"email.xls" intext:"{}"'.format(data)
query5 = 'inurl:logs intext:GET https:// ext:txt intext:password intext:email intext:"{}"'.format(data)
query6 = 'intext:"{}" site:leakeddata.cc'.format(data)

print(Fore.YELLOW + "Searching for {} in Pastebin data leaks".format(data) + Fore.RED)

for j in search(query, num=15): 
  a = j.replace("https://pastebin.com/", "https://pastebin.com/raw/")
  print("Information was found @: " + a)

print(Fore.YELLOW + "Searching for {} in accidentally exposed databases".format(data) + Fore.RED)

sleep(9)

for j in search(query2, num=15): 
  print("Information was found for " + data + " at " + j)
  
print(Fore.YELLOW + "Searching for your email in misconfigured website database info!" + Fore.RED)

sleep(7)

for j in search(query3, num=15): 
  print("Information was found for " + data + " at " + j)

print(Fore.YELLOW + "Searching for {} in accidentally/intentionally exposed emails".format(data))

sleep(10)

for j in search(query4, num=15): 
  print("Information was found for " + data + " at " + j)
  
print(Fore.YELLOW + "Searching for {} in exposed excel spreadsheets".format(data) + Fore.RED)

sleep(10)

for j in search(query5, num=15): 
  print("Information was found for " + data + " at " + j)
  
print(Fore.YELLOW + "Searching for {} in exposed debug logs".format(data) + Fore.RED)

sleep(8)

for j in search(query6, num=15): 
  print("Information was found for " + data + " at " + j)
  
print()
print(Fore.GREEN + "The search for {} is complete!".format(data) + Fore.RESET)


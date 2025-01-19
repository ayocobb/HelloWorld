#!/usr/bin/python3

### Info: This script generates the ini file that contains login info, used to setup the Domain
###
### Date: 11/15/2023
##  Author: Ayo Olukotun@IPC Cloud Engineering

import os, sys,base64, shutil
import json,csv,requests,re
import datetime,calendar,time
import ipaddress
import glob
import socket
#import vfc_vars
from contextlib import closing

def val_ipaddr (ipaddr,*message):
   try:
      ip = ipaddress.ip_address(ipaddr)
      #print("IP address {} is valid. The object returned is {}".format(ipaddr, ip))
      print(f'{message} - {ip} is valid')
      return
   except ValueError:
      print(f'{message} - {ip} is not valid') 
      sys.exit()

## Begin main {
def main():

   for row in range(10):
     print(f'{row}.... Hello World') 
     print(f'{row}.... Whats up ') 


## End main }
if __name__ == '__main__':
   main()

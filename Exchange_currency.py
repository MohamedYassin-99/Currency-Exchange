# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:47:00 2022

@author: hamoy
"""

import urllib3
import json
url ="https://api.exchangerate.host/latest/"
http=urllib3.PoolManager()
response  =http.request('GET',url)
data = response.data
currency = json.loads(data)
currency_data= currency['rates']
user= input("Enter a cuurency : ")
Dollar= currency_data["USD"]
for i,j in currency_data.items():
    if i==user:
        print('Current Value =',j-Dollar)

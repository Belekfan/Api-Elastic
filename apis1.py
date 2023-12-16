import json
import os
import requests

class Api:
    def __init__(self,apilist):
        
        self.apilist=["https://api-elastic-api1.onrender.com"]
        
    def __str__(self) -> str:
        print("Apilist: "+str(self.apilist[0]))


    def find(self,addr,str):
        if addr=="api1":
            resp=requests.get(str(self.apilist[0])+"/search/docs/?searchs="+str(str))
            return resp.text
        elif addr=="api2":
             resp=requests.get(str(self.apilist[1])+"/search?searchs="+str(str))
             return resp.text



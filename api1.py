from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)


f=open("data1.json")

data=json.load(f)

f2=open("data2.json")

data2=json.load(f2)

f3=open("data3.json")

data2=json.load(f3)

@app.route('/search/docs-web/')
def choise():
     arrmain=[]
     searchs = request.args.get('searchs')
     for i in data["data-web"]:
            if searchs in i["name"]:
                 arrmain.append(i)
      
     if len(arrmain)==0:
          return "not found"
     return arrmain

@app.route('/search/docs-os/')
def choise2():
     arrmain=[]
     searchs = request.args.get('searchs')
     for i in data2["data-os"]:
            if searchs in i["name"]:
                 arrmain.append(i)
      
     if len(arrmain)==0:
          return "not found"
     return arrmain

@app.route('/search/docs-mobile/')
def choise3():
     arrmain=[]
     searchs = request.args.get('searchs')
     for i in data3["data-mobile"]:
            if searchs in i["name"]:
                 arrmain.append(i)
      
     if len(arrmain)==0:
          return "not found"
     return arrmain

@app.route('/')
def hello_world():
  return "Api 1"

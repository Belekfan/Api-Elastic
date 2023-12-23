from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)


f=open("data1.json")

data=json.load(f)

@app.route('/search/docs/')
def choise():
     arrmain=[]
     searchs = request.args.get('searchs')
     for i in data["data-web"]:
            if searchs in i["name"]:
                 arrmain.append(i)
      
     if len(arrmain)==0:
          return "not found"
     return arrmain


@app.route('/')
def hello_world():
  return "Api 1"

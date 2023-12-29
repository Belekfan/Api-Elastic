from flask import Flask, jsonify, request
import os
import json
from apis1 import Api


app = Flask(__name__)


f = open('offsets.json')

apilist=["api1"]
offsets = json.load(f)
arrmain=[]


for i in offsets["offsets"]:
    arrmain.append(i["offset"]+"&&"+i["addr"])

api1=Api(apilist)

@app.route('/choose')
def choose():
     offset = request.args.get('offset')
     searchs = request.args.get('searchs')
     subject = request.args.get('subject')
     for i in arrmain:
        arrtemp=i.split("&&")
        if offset==arrtemp[0]:
            conc=api1.find(arrtemp[1],searchs,subject)
            return conc



@app.route('/')
def hello_world():
  return "Hello World"


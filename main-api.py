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

print(api1)

@app.route('/choose')
def choose():
     offset = request.args.get('offset')
     searchs = request.args.get('searchs')
     for i in arrmain:
        arrtemp=i.split("&&")
        if offset==arrtemp[0]:
            conc=api1.find(arrtemp[1],searchs)
            return jsonify(conc)



@app.route('/')
def hello_world():
  return "Hello World"


from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)

arrmain=[]
f=open("data1.json")

data=json.load(f)

@app.route('/search/docs')
def choose():
     searchs = request.args.get('searchs')
     for i in data["cve-data-web"]:
            if searchs==i.name:
              return jsonify(i)



@app.route('/')
def hello_world():
  return "Api 1"

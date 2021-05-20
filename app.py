from flask import Flask,request
import db_operations as db
import json

app = Flask(__name__)

@app.route("/insert",methods = ['POST'])
def insert():
    audioFileType= request.form['audioFileType']
    audioFileMetadata= json.loads(request.form['meta'])
    return db.insert(audioFileType,audioFileMetadata)

@app.route('/<audioFileType>/<audioFileID>',methods=['GET'])
def get(audioFileType,audioFileID):
    return db.get(audioFileType,audioFileID)

@app.route('/update/<audioFileType>/<audioFileID>',methods=['POST'])
def update(audioFileType,audioFileID):
    metaData=json.loads(request.form['meta'])
    return db.update(audioFileType,audioFileID,metaData)

@app.route('/delete/<audioFileType>/<audioFileID>',methods=['GET'])
def delete(audioFileType,audioFileID):
    return db.delete(audioFileType,audioFileID)

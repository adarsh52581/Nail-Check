from flask import Blueprint, render_template , request, flash,redirect
from flask_bootstrap import Bootstrap

import urllib.request
import os
from werkzeug.utils import secure_filename
from roboflow import Roboflow
import json
import numpy as np

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/UpAndPredict', methods =['GET','POST'])
def UpAndPredict():
    if request.method=='POST':
      submit()   
    return render_template("Up&Predict.html")

@views.route('/submit',methods=['POST'])
def submit():
  ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
  
  def upload_file():
       file_path = request.data.decode('utf-8')  # Assuming the file path is sent as plain text in the request body
       # Process the file path or perform desired operations with it
       return file_path
  
  def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS             
  
  print(request.files)
  if 'file' not in request.files:
      flash('No file part')
      return render_template("Up&Predict.html")   #This statement has to be changed with file not recieved at backkend.
        
  file = request.files['file']
      
  if file.filename == '':
    flash('No image selected for uploading')
    return render_template("Up&Predict.html")   #This statement has to be changed with file not selected for upload.
      
  if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      rf = Roboflow(api_key="S0ZRXr8KslM5xZVGkV9N")
      project = rf.workspace().project("nailcheck")
      model = project.version(1).model
      data=model.predict("D:/NadiNoufal/Files/Carreer/Projects/NailDiseaseDetectionSystem - S6 MiniProject/website/static/uploads/"+file.filename).json()
      value = data['predictions'][0]['top']
      print(value)
      return render_template("Result.html",text=value)
  else:
      flash('Allowed image types are - png, jpg, jpeg, gif')
      return render_template("Up&Predict.html")
      
     


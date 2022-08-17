from urllib import request
from flask import Flask,Response
from flask import render_template as rt
import numpy as np
import jsonpickle
from predict_func import predict


app = Flask(__name__)
@app.route('/')
def home():
    return rt('home')

@app.route('/api/predict',methods=['POST'])
def predict_api():
    r = request
    img_data = r.files('img')
    Result = predict(img_data)
    return Result


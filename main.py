from urllib import request
from flask import Flask,Response
from flask import render_template as rt
import numpy as np
import jsonpickle
#heroku ID sur.one9309@gmail.com
#pass surone_0955407529

app = Flask(__name__)
from predict_func import predict
@app.route('/')
def home():
    return "HI"

@app.route('/api/predict',methods=['POST'])
def predict_api():
    r = request
    img_data = r.files('img')
    Result = predict(img_data)
    return Result


if __name__ == '__main__':
  print('Now is running')
  app.run(host='0.0.0.0',port=8080)
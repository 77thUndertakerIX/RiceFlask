from flask import Flask,Response,request
from flask import render_template as rt
from predict_func import predict


app = Flask(__name__)
@app.route('/')
def home():
    return rt('home.html')

@app.route('/api/predict',methods=['POST'])
def predict_api():
    r = request
    img_data = r.files['image']
    img_data.save("data/RD.jpg")
    data_result = predict(img_data)
    
    return data_result

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=8000)




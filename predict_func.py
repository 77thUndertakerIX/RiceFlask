from tensorflow import keras
from tensorflow.keras.models import load_model
import numpy as np
from call_dict import Get_info
import cv2
from flask import jsonify

model = load_model("Better_model.h5")
def predict(img_data):
  
    percen_list = []
    img_data = cv2.imread('data/RD.jpg')
    img_data = cv2.resize(img_data, (128,128))

    img_data =  np.array(img_data)
    img_data = img_data.astype('float32')
    img_data /= 255
    #print(img_data)
    img_data = np.reshape(img_data,(1,128,128,3))
    predict = model.predict(img_data) #the prediction here uses model from Better_model.h5
    label_name = ['Sheath Rot Disease',
    'Sheath blight Disease',
    'Bacterial Blight Disease','Leaf Scald Disease',
    'Narrow Brown Spot Disease',
    'Brown Spot Disease',
    'Dirty Panicle Disease']
    result = label_name[np.argmax(predict)] #show the most possible percentage of Disease's name


    '''
    if it cant to send the percent of predict then change to str b4 return to user then do something on client
    all_percent_of_predict = str(predict[0])

    '''  

    #make conclusion and then send to client
    '''
    add the results to data
    vvv
    
    '''
    
    
    ListPredict = predict.tolist() #change to list
    percentage = ListPredict[0] #select the first one
    #loop to make a conclusion
    for item in range(len(percentage)):
      NameWithPercen = label_name[item] + " =>> "+ str(percentage[item]*100)+"%"
      percen_list.append(NameWithPercen)
    #print(percen_list)

    data_result = jsonify({
          "Result" :result, #The most possible Disease's name
          "percentage": percentage,
          "NameWithPercen": percen_list,
          "Info": Get_info(result), #send the Disease name to get the information 
      })

    

    '''
    then ==>> return result
    vvvv
    '''
    #print(data_result)
    return data_result
  
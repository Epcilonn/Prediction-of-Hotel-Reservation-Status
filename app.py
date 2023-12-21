import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
import math


app=Flask(__name__,template_folder="template",static_folder='staticFiles')
model=pickle.load(open('build.pkl','rb'))   #import model

@app.route('/')
def home():
    return render_template('index.html') 
@app.route('/predict',methods=['POST'])

def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    if prediction==0:
        return render_template('index.html',prediction_text="Customer will Cancle the reservation".format(prediction))
    else:
        return render_template('index.html',prediction_text="Customer will not cancle the reservation".format(prediction))
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)

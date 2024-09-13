import joblib
from flask import Flask,request,jsonify,url_for,render_template,app
import numpy as np
import pandas as pd
import json
app = Flask(__name__)

model = joblib.load('player_rating_model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict():
    data = request.json['data']
    print(data)
    Pandas_data = pd.DataFrame(data,index=[0])
    prediction = model.predict(Pandas_data)
    print(prediction)
    pred = json.dumps({'prediction': prediction.tolist()})
    print(pred)
    return pred

if __name__ == '__main__' :
    app.run(debug=True)
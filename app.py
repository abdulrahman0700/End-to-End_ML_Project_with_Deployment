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
def predicts():
    data = request.json['data']
    print(data)
    Pandas_data = pd.DataFrame(data,index=[0])
    prediction = model.predict(Pandas_data)
    print(prediction)
    pred = json.dumps({'prediction': prediction.tolist()})
    print(pred)
    return pred

@app.route("/predict",methods=["POST"])
def predication():
    data = [d for d in request.form.values()]
    print(data)
    Pandas_data = pd.DataFrame({"Teams":data[0],"Seasons":data[1],"Players":data[2],"Matches":int(data[3]),"Goals":int(data[4]),"Assists":int(data[5])},index=[0])
    print(Pandas_data)
    predicts = model.predict(Pandas_data)
    print(predicts)
    return render_template("home.html",prediction_text="The Season Rate Prediction is {}".format(predicts[0]))
    

if __name__ == '__main__':
    app.run(debug=True)
import joblib
from flask import Flask,request,jsonify,url_for,render_template,app
import numpy as np
import pandas as pd
import json
from Database_PostgreSQL import database

app = Flask(__name__)

model = joblib.load('player_rating_model.pkl')

db = database()

@app.route('/')
def home():
    return render_template('home.html')

"""

This Function is for testing API on postman

"""

@app.route('/predict_api',methods=['POST'])
def predicts():
    data = request.json['data']
    listed_data = [values_data for values_data in data.values()]
    print(data)
    print(listed_data)
    Pandas_data = pd.DataFrame(data,index=[0])
    db.insert_data(0,listed_data[0],listed_data[1],listed_data[2],listed_data[3],listed_data[4],listed_data[5])
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
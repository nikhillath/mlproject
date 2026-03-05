from flask import Flask,request,render_template
import numpy as np
import pandas as pd


from src.pipeline.predict_pipeline import CustomData,Predictpipeline

from sklearn.preprocessing import StandardScaler


application=Flask(__name__)

app=application

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_data',methods=['Get','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('predict.html')
    else:
        data=CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            average=float(request.form.get('average'))
        )
        pred_data=data.get_data_as_dataframe()
        print (pred_data) 
        predict_pipeline=Predictpipeline()
        results=predict_pipeline.predict(pred_data)

        return render_template('predict.html',results=results[0])

if __name__=="__main__":
    app.run(host="0.0.0.0")
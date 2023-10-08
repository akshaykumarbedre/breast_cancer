from flask import Flask,request,render_template,jsonify
from src.pipeline.predict_pipeline import Custom_data,predict
import pandas as pd 

application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')


features = [
    "mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness",
    "mean compactness", "mean concavity", "mean concave points", "mean symmetry",
    "mean fractal dimension", "radius error", "texture error", "perimeter error",
    "area error", "smoothness error", "compactness error", "concavity error",
    "concave points error", "symmetry error", "fractal dimension error",
    "worst radius", "worst texture", "worst perimeter", "worst area", "worst smoothness",
    "worst compactness", "worst concavity", "worst concave points", "worst symmetry",
    "worst fractal dimension"
]

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html',features=features)
    
    if request.method == 'POST':
        # Create an empty dictionary to store feature values
        feature_values = {}
        # Iterate through the features and retrieve their values from the form data
        for feature in features:
            value = float(request.form.get(feature))
            feature_values[feature] = value

        print(feature_values)
        df = pd.DataFrame(feature_values, index=[0])
        print(df)

        predict_pipeline=predict()
        pred=predict_pipeline.model_predtion(df)

        results=round(pred[0])
        key=""
        if(results==0):
            key="Don't have cancer"
        else:
            key="your have cancer"


        return render_template('form.html',final_result=key)
    

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
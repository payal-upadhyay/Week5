# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:51:48 2021

@author: Payal
"""

#Using flask to make an API
#Import necessary libraries and functions

from flask import Flask,jsonify,request
import pickle
import pandas as pd

app= Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    if (request.method=='GET'):
        data= "Hello World"
        return jsonify({'data':data})
    

@app.route('/predict/')

def write_predict():
    model=pickle.load(open('model.pickle','rb'))
    math = request.args.get('math score')
    read = request.args.get('reading score')
    
    test_df = pd.DataFrame({'Math Score':[math], 'Reading Score':[read]})

    pred_write = model.predict(test_df)

    return jsonify({'Writing Score': str(pred_write)})

#driver function
if __name__ == '__main__':
    app.run(debug=True)
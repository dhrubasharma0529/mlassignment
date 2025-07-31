import streamlit as st
import joblib
import pandas as pd
import numpy as np
def classify_iris(*args):
    arraylist = []
    for arg in args:
        arraylist.append(arg)
    new_sample = np.array(arraylist)
    z = new_sample.reshape(1,4)
    flower_list = ['setosa', 'versicolor', 'virginic']
    loadedmodel = joblib.load("C:\\Users\\Acer-nitro5\\Desktop\\ml\\iris_classifier_knn_model.joblib")
    get_predict = loadedmodel.predict(z)
    return flower_list[get_predict[0]]

    
sepal_length = st.number_input("Enter the sepal length")
sepal_width = st.number_input("Enter the sepal width")
petal_length  = st.number_input("Enter the petal length")
petal_width = st.number_input("Enter the petal width")
clicked_button = st.button("Predict")
if clicked_button:
    predict = classify_iris(sepal_length,sepal_width,petal_length,petal_width)
    st.write("The flower class is ", predict)

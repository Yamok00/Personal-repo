# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 09:41:08 2022

@author: USER
"""

import sklearn
import pandas as pd
import streamlit as st
import pickle

filename = 'Heart_attack.sav'
model = pickle.load(open(filename, 'rb'))

st.title('Heart Disease Prediction Model')
st.subheader('This model takes in health vairables of user to predict the occurence of heart disease or attack')

def user_input():
    bp = st.selectbox('Do you have high blood pressure?', ['Yes', 'No'])
    chol = st.selectbox('Do you have high cholesterol level?', ['Yes', 'No'])
    diab = st.selectbox('Are you suffering from Diabetes?', ['Yes', 'No'])
    smoke = st.selectbox('Are you a smoker?', ['Yes', 'No'])
    strk = st.selectbox('Do you have Stroke?', ['Yes', 'No'])
    GenHlth = st.slider('On a scale of 0 - 5, how do you rate your general health?', 0, 5)
    PhysHlth = st.slider('On a scale of 0 -30, how do you rate your physical health?', 0, 30)
    diffwalk = st.selectbox('Do you have difficulties walking?', ['Yes', 'No'])
    Age = st.text_input('What is your age?', 0, 3)
    education = st.selectbox('What is your level of education?', ['Primary', 'Junior High', 'Senior High', 'Undergraduate', 'Msc', 'PhD'])
    income = st.selectbox('What is the level of your annual income?', ['0 - £8000', '£8001 - £40000', '£40001 - £80000', '£80001 - £120000', '£120001 - £250000', '£250001 - £1000000', '£1000001 - £5000000', 'Greater than £1000000'])
    
    if (bp=='Yes'):
        HighBP = 1
    else:
        HighBP = 0
    
    if (chol=='Yes'):
        HighChol = 1
    else:
        HighChol = 0
    if (diab=='Yes'):
        Diabetes = 1
    else:
        Diabetes = 0
    if (smoke=='Yes'):
        Smoker = 1
    else:
        Smoker = 0
    if (strk=='Yes'):
        Stroke = 1
    else:
        Stroke = 0
    if (diffwalk=='Yes'):
        DiffWalk = 1
    else:
        DiffWalk = 0
    if (education=='Primary'):
        Education = 0
    elif (education == 'Junior High'):
        Education = 1
    elif (education == 'Senior High'):
        Education = 2
    elif (education == 'Undergraduate'):
        Education = 3
    elif (education == 'Msc'):
        Education = 4
    else:
        Education = 5
        
        
    if (income=='0 - £8000'):
        Income = 0
    elif (income == '£8001 - £40000'):
        Income = 1
    elif (income == '£40001 - £80000'):
        Income = 2
    elif (income == '£80001 - £120000'):
        Income = 3
    elif (income == '£120001 - £250000'):
        Income = 4
    elif (income == '£250001 - £1000000'):
        Income = 5
    elif (income == '£1000001 - £5000000'):
        Income = 6
    else:
        Income = 7
    
    
    data = {'Blood Pressure': HighBP,
            'Cholesterol level': HighChol,
            'Smoker': Smoker,
            'Stroke': Stroke,
            'Diabetes': Diabetes, 
            'Gen health': GenHlth,
            'Phys health': PhysHlth,
            'Difficulty walking': DiffWalk,
            'Age': Age,
            'Edu': Education,
            'Income': Income}
    
    
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input()

def prediction():
    predict_ = model.predict(df)
    result = ''
    if predict_ == 0:
        result = 'You do not have heart attack or disease'
    else:
        result = 'Sorry to inform you, you are most likely to have a heart attack or disease'
    return result

if st.button("predict"):
    result = prediction()
    st.success('Thank you for filling the form. {}'.format(result))
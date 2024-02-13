import streamlit as st
import pandas as pd
import pickle
from sklearn import preprocessing

# Load the model
model = pickle.load(open("forest_model.pkl", "rb"))

# Load the data
data = pd.read_excel("bankruptcy.xlsx")

st.title("Bankruptcy-Prevention")

risk_mapping = {
    'Low': 0,
    'Medium': 0.5,
    'High': 1
}

# Now you can use the assigned numerical values in your predictions or further processing

Industrial_risk = st.selectbox('Industrial_risk', ('Low','Medium','High'))
Management_risk = st.selectbox(' Management_risk', ('Low','Medium','High'))
Financial_flexibility = st.selectbox(' Financial_flexibility',('Low','Medium','High'))
Credibility = st.selectbox(' Credibility',('Low','Medium','High'))
Competitiveness = st.selectbox(' Competitiveness',('Low','Medium','High'))
Operating_risk = st.selectbox(' Operating_risk', ('Low','Medium','High'))


if st.button('Prevention Type'):
    df = {
        'industrial_risk': risk_mapping[Industrial_risk],
        ' management_risk': risk_mapping[Management_risk],
        ' financial_flexibility': risk_mapping[Financial_flexibility],
        ' credibility': risk_mapping[Credibility],
        ' competitiveness': risk_mapping[Competitiveness],
        ' operating_risk': risk_mapping[Operating_risk]
    }

data = preprocessing.scale(data)

# Making the prediction
prediction = model.predict(data)

# Displaying the result
if prediction == '1':
    st.write('The company is at risk of bankruptcy')
else:
    st.write('The company is not at risk of bankruptcy')

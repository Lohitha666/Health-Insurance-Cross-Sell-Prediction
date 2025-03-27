import streamlit as st
import joblib
import numpy as np

# Load the pre-trained model


def predict_fraud(Gender,Age,Driving_License,Region_Code,Previously_Insured,
                  Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage):
    # Create a NumPy array with the input features
    input_data = np.array([[Gender,Age,Driving_License,Region_Code,Previously_Insured,
                  Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage]])

    # Make a prediction
    prediction = model.predict(input_data)

    return prediction[0]


with open(r'D:\2-PROJECTS\2-IPT\gradient_boosting_model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)
# Streamlit app layout
st.title('Customer Insurance Prediction')

# Input fields
Gender = st.checkbox('Gender')
Age = st.number_input('Age', value=0.0)
Driving_License = st.checkbox('Driving License')
Region_Code = st.number_input('Region Code', value=0.0)
Previously_Insured = st.checkbox('Previously Insured')
Vehicle_Age = st.number_input('Vehicle Age', value=0.0)
Vehicle_Damage = st.checkbox('Online Order')
Annual_Premium = st.number_input('Annual Premium', value=0)
Policy_Sales_Channel = st.number_input('Policy Sales Channel', value=0.0)
Vintage = st.number_input('Vintage', value=0)

# Make prediction on button click
if st.button('Predict'):
   
    result = predict_fraud(Gender,Age,Driving_License,Region_Code,Previously_Insured,
                  Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage)

    if result == 1:
        st.success("Yes Intrested In Taking")
    else:
        st.error("Not Intrested In Taking")

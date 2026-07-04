import streamlit as st
import pickle
import numpy as np
import joblib
if "is_update_result" not in st.session_state:
     st.session_state.is_update_result = False


folder_path='/Users/chandra/Desktop/FSDS_GenAI_Training/FSDS_Classes/Python_Workspace/ML/Students_Info_Regression_Model/'
file_name = 'students_linear_regression_model.pkl'
file_path=folder_path+file_name

model = joblib.load(file_path)


# model = pickle.load(open(file_path,'rb'))

model= joblib.load(file_path)
# hours = 11
# study_hours_input = np.array([[hours]])
# prediction = model.predict(study_hours_input)
# print("prediction = ",prediction)


st.title("Study Hours and Marks Prediction ")


st.write("This app predicts the Marks on the study hours using a simple linear regression model.")

study_hours_input = st.sidebar.number_input("Enter Study Hours :", min_value=1,max_value=24, value=1, step=1)

# When the button is clicked, make predictions
if st.sidebar.button("Predict Percentage"):
    # Make a prediction using the trained model
    experience_input = np.array([[study_hours_input]])  # Convert the input to a 2D array for prediction
    prediction = model.predict(experience_input)
   
    favorite_color ='Green'
    st.write(f"## If Students study for :{favorite_color.lower()}[**{study_hours_input}**] hours, they will get :{favorite_color.lower()}[**{prediction [0][0]:,.2f} %**] of Marks")

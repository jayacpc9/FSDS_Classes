import streamlit as st
import pickle
import numpy as np

if "is_update_result" not in st.session_state:
     st.session_state.is_update_result = False

folder_name ="/Users/chandra/Desktop/FSDS_GenAI_Training/FSDS_Classes/Python_Workspace/ML/Students_Info_Regression_Model/"
pickle_fileName ="Students_marks.pkl" 
pickle_fileName ='linear_regression_model.pkl'
file_path =folder_name+pickle_fileName
print("File path = ",file_path)

model = pickle.load(open(file_path,'rb'))
hours = 11
study_hours_input = np.array([[hours]])
prediction = model.predict(study_hours_input)
print("prediction = ",prediction)


st.title("Study Hours and Marks Prediction ")


st.write("This app predicts the Marks on the study hours using a simple linear regression model.")
# is_update_result =False

def handle_experience_change():
    # st.toast(f"Experience level updated! {study_hours_input}")
    experience_input = np.array([[study_hours_input]])  # Convert the input to a 2D array for prediction
    st.session_state.prediction = model.predict(experience_input)
    # st.write(f"If Students study for {study_hours_input} hours, they will get { st.session_state.prediction [0][0]:,.2f} % of Marks")
    st.session_state.is_update_result = True
    # st.write(f" in handle_experience_change() :: st.session_state.is_update_result  = {st.session_state.is_update_result }")
   
   

study_hours_input = st.sidebar.number_input("Enter Study Hours :", min_value=0.0,max_value=24.0, value=1.0, step=0.5,on_change=handle_experience_change)
# st.write(f" st.session_state.is_update_result  = {st.session_state.is_update_result }")

if  st.session_state.is_update_result :
    favorite_color ='Green'
    st.write(f"## If Students study for :{favorite_color.lower()}[**{study_hours_input}**] hours, they will get :{favorite_color.lower()}[**{ st.session_state.prediction [0][0]:,.2f} %**] of Marks")

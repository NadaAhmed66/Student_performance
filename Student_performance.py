import streamlit as st
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\GEEK\Downloads\archive (4)\Student_Performance.csv")

st.title('Student Performance')
st.write(df.head())

plt.figure(figsize=(6, 4))
plt.scatter(df['Hours Studied'], df['Performance Index'], color='blue')
plt.xlabel('Hours Studied')
plt.ylabel('Performance Index')
plt.title('Hours Studied vs Performance Index')

st.pyplot(plt)

#load model
with open(r"C:\Users\GEEK\lr_student.pkl",'rb') as file:
    model=pickle.load(file)
st.sidebar.header('user input')
def user_input():
    Hourse_studied=st.sidebar.slider('Hours Studied',1,9,5)
    Previous_Scores=st.sidebar.slider('Previous Scores',1,100,50)
    Extracurricular_Activities=st.sidebar.selectbox('Extracurricular Activities',['Y','N'])
    Extracurricular_Activities = 1 if Extracurricular_Activities == 'Y' else 0
    Sleep_Hours=st.sidebar.slider('Sleep Hours',1,9,5)
    Sample_Question_Papers_Practiced=st.sidebar.slider('Sample Question Papers Practiced',0,9,5)

    data={
        'Hours Studied':Hourse_studied,
        'Previous Scores':Previous_Scores,
        'Extracurricular Activities':Extracurricular_Activities,
        'Sleep Hours':Sleep_Hours,
        'Sample Question Papers Practiced':Sample_Question_Papers_Practiced
    }

    feature=pd.DataFrame([data])
    return feature

input_user=user_input()
if st.sidebar.button("Predict"):
    prediction=model.predict(input_user)
    st.sidebar.write('Model prediction',prediction)
        

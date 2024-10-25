# import pandas
# import sklearn
# import pickle
# import streamlit as st
# file1=open(r"C:\Users\lumin\Downloads\file.pkl",'rb')
# dict1=pickle.load(file1)
# le_education=dict1['label_Encoder']['Education']
# le_city=dict1['label_Encoder']['City']
# le_gender=dict1['label_Encoder']['Gender']
# le_everbenched=dict1['label_Encoder']['EverBenched']
# model=dict1['model']
# st.title('Employee Leave Taking Behaviour Model')
# ed=st.selectbox('Education',['Bachelors','Masters','PHD'])
# year=st.selectbox('Joining Year',[2012,2013,2014,2015])
#
#
# city=st.selectbox('Select a city',[''])
# ret=st.button('Predict')
# def prediction(Education,JoiningYear,City, PaymentTier,Age,Gender,
#        EverBenched,Experienc):
#     Education=le_education.transform([Education])[0]
#     City=le_city.transform([City])[0]
#     Gender=le_gender.transform([Gender])[0]
#     EverBenched=le_everbenched.transform([EverBenched])[0]
#     two_d_input=[[Education,JoiningYear,City,PaymentTier,Age,Gender,EverBenched,Experienc]]
#     return model.predict(two_d_input)[0]
# if ret:
#     res=prediction()
#     if res==1:
#         st.subheader('Positive')
#     elif res==0:
#         st.subheader('Negative')
# # print(prediction('Bachelors',2017,'Bangalore',2,21,'Male','Yes',2))
s='hello'
print(dir(s))

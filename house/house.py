import pandas as pd
import streamlit as st
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("C:\\Users\\payal\\Desktop\\Housing.csv")
dataset=data[["area","bedrooms","bathrooms","stories","mainroad","price"]]

dataset["parking"]=data[["parking"]]
ma=LabelEncoder()
ma.fit(dataset[["mainroad"]])
dataset["mainroad"]=ma.transform(dataset[["mainroad"]])
dataset["mainroad"]=dataset["mainroad"].astype("int64")

x=dataset[['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad','parking']]
y=dataset[["price"]]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=20)
lr=LinearRegression()
lr.fit(x_train,y_train)
print(lr.score(x_train,y_train))
joblib.dump(lr,"model")
joblib.dump(ma,"model1")
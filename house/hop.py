import streamlit as st
import joblib
from PIL import Image
imag=Image.open("a.jpg")
st.image(imag,caption="HOUSE",width=500)
model=joblib.load("model")
model1=joblib.load("model1")

st.markdown(f"# :orange[HOUSE PREDICTION MODEL]")
#'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad','parking
a=st.number_input("ENTER THE AREA OF HOUSE IN SQUARE FIT",min_value=200,max_value=10000,value=200,step=100)
b=st.number_input("ENTER THE NUMBER OF BADROOME",min_value=1,max_value=10,value=1,step=1)
c=st.number_input("ENTER THE NUMBER OF BATHROOM",min_value=1,max_value=10,value=1,step=1)
d=st.number_input("ENTER THE NUMBER OF STORIES ROOM",min_value=1,max_value=10,value=1,step=1)
e=st.text_input("HOUSE MAINROAD IS yes / no",value="yes").lower()
f=st.number_input("ENTER THE NUMBER OF PARKING  AREA",min_value=1,max_value=10,value=1,step=1)
g=model1.transform([[e]])
i=g[0]
if st.button("SUNMIT"):
    h=model.predict([[a,b,c,d,i,f]])
    x=h[0]
    x=int(x)
    y=f"YOUR HOUSE PRICE BASED ON INPUT VALUE IS :-- {x} RUPEES"
    st.success(y)


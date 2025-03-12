import streamlit as st #web frontend whithout using HTML CSS JS
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

model = LinearRegression() #creating a model
x = df[["diametro"]] #giving to AI the data [] - returns column - [[]] - returns dataframe
y = df[["preco"]]

model.fit(x,y)

st.title("predicting the value of a pizza")
st.divider()

diameter = st.number_input("Type the diameter of the pizza:")

if diameter:
    predicted_price = model.predict([[diameter]])[0][0]
    st.write(f"the pizza value with the diameter {diameter:.2f} cm is: ${predicted_price:.2f}.")
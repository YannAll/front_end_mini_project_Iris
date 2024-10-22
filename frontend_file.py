import streamlit as st
import requests

st.title('Iris predictor')

st.write('This is an app to predict the type of Iris')

sepal_length= st.slider('Select the sepal length',0,4,3)
sepal_width= st.slider('Select the sepal width',0,4,3)
petal_length = st.slider('Select the petal length',0,4,3)
petal_width= st.slider('Select the petal width',0,4,3)

API_url="https://mini-ml-project-847896799784.europe-west1.run.app"

predict_url=f"{API_url}/predict"

params= {'sepal_length':sepal_length,
         'sepal_width':sepal_width,
         'petal_length': petal_length,
         'petal_width':petal_width}

response = requests.get(predict_url, params)

if response.status_code==200:
    st.write(response.json())

else:
    print(response)

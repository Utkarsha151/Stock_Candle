import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here


#import libraries
import pyrebase

from datetime import datetime



#configuration
firebaseConfig = {
  'apiKey': "AIzaSyD77BfmCYnREsOm5ccGPcICR4NGXuzHqP4",
  'authDomain': "stock-eb968.firebaseapp.com",
  'projectId': "stock-eb968",
  'databaseURL': "https://stock-eb968-default-rtdb.firebaseio.com/",
  'storageBucket': "stock-eb968.appspot.com",
  'messagingSenderId': "983107711191",
  'appId': "1:983107711191:web:f655d875f4170c617bc092",
 ' measurementId': "G-HT1ETMS7J1"
}


#firebase authentication

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#database
db= firebase.database()
storage = firebase.storage()


st.sidebar.title("About Us")
st.sidebar.info("This web page predicts stock prices of various companies till next 4 years.            One can search and view information about various stocks like predicted data and raw data as well")
st.sidebar.success("If you have any query contact us :     teamstockcandle@gmail.com          987654321")


app = MultiApp()

#st.markdown("""
# Multi-Page App

#This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).

#""")



# Add all your application here
app.add_app("Home", home.app)
#app.add_app("Data", data.app)
app.add_app("Model", model.app)
# The main app
app.run()

from cgitb import html
import streamlit as st

from PIL import Image

import streamlit.components.v1 as components

def app():
    st.title('Welcome to stock candle')

    #video2 = open("Video1.mp4", "rb") 
    #st.video(video2)
    #st.video(video1, start_time = 25)

    
    #image = Image.open('img2.jpeg')

   # col1, col2 = st.columns([1, 1])

   # video_html = """
    #<video controls width="250" autoplay="true" muted="true" loop="true">
   # <source 
     #       src="https://www.youtube.com/watch?v=DrKLYvLPidw" 
      #      type="video/mp4" />
    #</video>
    #"""

    #col2.markdown(video_html, unsafe_allow_html=True)
    st.info('Refer below video if you are beginner')
    st.video("https://www.youtube.com/watch?v=NOX53AJPypw")
    st.info('Below video describes about future and option trading')
    st.video("https://www.youtube.com/watch?v=MiybniIIvx0" , start_time = 30)
     # st.video("https://media.istockphoto.com/videos/moving-financial-chart-with-downtrend-line-candlestick-graph-and-in-video-id1157256430")
    #st.image("https://www.google.com/search?q=online+stock+market+images&tbm=isch&ved=2ahUKEwjytq2XmKr3AhW_k9gFHXYZA-4Q2-cCegQIABAA&oq=online+stock+market+images&gs_lcp=CgNpbWcQAzoHCCMQ7wMQJzoGCAAQCBAeUNsFWL8XYMwYaABwAHgAgAHVAYgB1AmSAQUwLjcuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=cvFjYvK1Br-n4t4P9rKM8A4&bih=746&biw=1536&rlz=1C1CHBF_enIN867IN871#imgrc=DTMQECynulqK3M", caption='Sunrise by the mountains')

    #st.write('This is the `home page` of this multi-page app.')

    #st.write('In this app, we will be building a simple classification model using the Iris dataset.')
 
    
    # bootstrap 4 collapse example
  
   # """https://medium.com/analytics-vidhya/ep5-adding-media-files-in-our-streamlit-web-app-74564af03642#:~:text=To%20add%20a%20video%20we,saved%20your%20opened%20video%20file."""
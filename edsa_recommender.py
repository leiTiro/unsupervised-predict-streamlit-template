"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
from PIL import Image
import time
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

st.sidebar.write('Film-Drive')
image = Image.open('resources/imgs/logo M.png')
st.sidebar.image(image, caption='')


# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Home","Solution Architecture","Datasets","Visual Aids","About us",
                    "Contact Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    
        
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
   
    if page_selection == "Home":
        st.title("Intuition-Tech")
        col1, col2= st.columns([2,1])
        
        with col2.expander('The Company'):
            st.write("Intuition-Tech is a leading African knowledge solutions company. We help clients develop the systems and expertise they need to unlock their potential")
            image = Image.open('resources/imgs/cinema style.jpg')
            st.image(image, caption='')
            st.write("We help companies give their customers what they want based on what the like")
            
      
        
        col1.write("Are you looking to watch a Movie? A series or even Youtube Videos? ")
        col1.write("if so, then you have come to the right place!")
        col1.write("We can recommend something for you to watch based on something that you have already seen and very much liked.")
        col1.write("We use comparison algorithms to make movie recomendations that have similar items to other movies of your choice and liking.")
        image = Image.open('resources/imgs/Think.PNG')
        col1.image(image, caption='')
        col1.title("We think so that you don't have too :) ")
        col1.write("Check out our recommenders now!")
        
        st.markdown("## Recommend a movie to other user")
        title = st.text_input('Movie title', ' ')
        st.write('I recommend the movie', title)
    
        
        
        
    if page_selection == "Solution Architecture":
        st.markdown("Explore our architectural principles")
        image = Image.open('resources/imgs/Recommeder-Engine-Banner-1280x576.jpg')
        st.image(image, caption='')
        st.write("**Collaborative Filtering**")
        with st.expander('Read more'):
        	st.write("collaborative filtering uses similarities between users and items simultaneously to provide recommendations. It is also known as social filtering. Collaborative filtering uses algorithms to filter data from user reviews to make personalized recommendations for users with similar preferences.")
        
        
        
        
        st.write("**Content-Based Filtering**")
        with st.expander('Read more'):
            st.write("Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback. it uses features of an item you have already seen to recommend others based on similarity.")
       
        image= Image.open('resources/imgs/fetch.PNG')
        st.image(image, caption='')
        st.write("**Overall solution exploration**")
        st.write("Recommender systems are information retrieval tool that allocates accurate recommendations to the specific users.In the current era of big data, the recommender system aspires to provide users with a tailored set of personalized items from a pool of a large population.Personalization systems have proved to be one of the most powerful tools for e-commerce sites, assisting users in discovering the most relevant products across enormous product catalogues.A highly performing recommendation System will suggest items that match the similarities with the highest degree of performance.")
        
        image= Image.open('resources/imgs/film.PNG')
        st.image(image, caption='')
        
        name1 = st.text_input('Enter your Username', ' ')
        txt = st.text_input('Leave a Comment', ' ')
        st.write(' ',name1 + ' :'+ txt )
        
    
        
        
    if page_selection == "Datasets":
        st.markdown("Database for recommender systems")
        col1, col2 = st.columns([2,1])
        col1.markdown('Movies DataFrame')
        if col1.button('open movies'):
            dfmovies= pd.read_csv('resources/data/movies.csv')
            col1.write(dfmovies)
        
        col1.markdown('Ratings DataFrame')
        if col1.button('open ratings'):
            dfrating= pd.read_csv('resources/data/ratings.csv')
            col1.write(dfrating)
            
        col2.markdown('Add to our Database')
        uploaded_file = col2.file_uploader("Choose a file")
        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)
            bar=col2.progress(0)
            for perc in range(100):
                time.sleep(0.05)
                bar.progress(perc+1)
            col2.success('File uploaded successfully')
            col2.write(dataframe)
            
        col1.markdown('Distribution of Ratings')
        if col1.button('Pie Chart'):
            image= Image.open('resources/imgs/dist_of ratings.PNG')
            st.image(image, caption='')
            
            
            
    if page_selection == "Visual Aids":
         st.title("Descriptive statistics")
         st.write("The visuals outline an imaginary roadmap to which movies,actors or genres to focus on for a good reliable recommendation.")
         
         st.markdown('Top 20 Genres with the highest Average Ratings')
         
         if  st.button('Bar Graph'):
             image= Image.open('resources/imgs/Vgenres.PNG')
             st.image(image, caption='')
             
         st.markdown('Top 10 rated Movies')
        
         if  st.button('List'):
            image= Image.open('resources/imgs/top_rated.PNG')
            st.image(image, caption='')
            
         st.markdown('Actors with the most number of movies')
        
         if  st.button('open'):
            image= Image.open('resources/imgs/actor vs movies.PNG')
            st.image(image, caption='')
        
        
    if page_selection == "About us":
        
        st.title("We are Intuition-Tech")
        st.write("Intuition-Tech is a leading global knowledge solutions company. We help companies develop the systems and expertise they need to unlock their potential.")

        st.write("Meet The Team")
        
        col1, col2= st.columns([3,1])
        images = ['resources/imgs/zwane.PNG']
        col1.image(images, use_column_width=10,  caption=["Chief Executive Officer: Honey Zwane"] )
        
        images=['resources/imgs/KRB.PNG']
        col2.image(images, use_column_width=10,  caption=["Ai Engineer: Karabo Eugene Hlahla"] )
        
        images= ['resources/imgs/Lesego.PNG' ]
        col2.image(images,use_column_width=10, caption=["Lesego Tiro: Product Manager"])
        
        images = ['resources/imgs/Ruth.PNG']
        col1.image(images, use_column_width=10,  caption=["Business Analyst"] )
                 
    if page_selection == "Contact Us":
        col1, col2 = st.columns([1,1])
        col1.title("Call")
        images=['resources/imgs/phone.PNG']
        col1.image(images, use_column_width=10,  caption=[""] )
        col1.write("**+27716123800**")
        col1.write("**+27781234566**")
        
        
        col1.title("Email")
        images=['resources/imgs/email.PNG']
        col1.image(images, use_column_width=10,  caption=[""] )
        col1.write("Inttech@gmail.com")
        col1.write("DataTech@gmail.com")
        
        col2.title("Instagram")
        images=['resources/imgs/gram.PNG']
        col2.image(images, use_column_width=10,  caption=[""] )
        col2.write("Intuition-Tech")
        
        col2.title("Twitter")
        images=['resources/imgs/twit.PNG']
        col2.image(images, use_column_width=10,  caption=[""] )
        col2.write("@Intuition-Tech")
        
        images=['resources/imgs/social.PNG']
        st.image(images, use_column_width=10,  caption=["Copyright © 2023, Intuition-Tech"] )
        
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()

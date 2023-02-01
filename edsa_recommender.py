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

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Home","Solution Architecture","About us",
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
        st.write("We are a leading global knowledge solutions company. We help clients develop the systems and expertise they need to unlock their potential")
        st.write("We help companies give their customers what they want based on what the like")
        image = Image.open('resources/imgs/cinema style.jpg')
        st.image(image, caption='')
        
        st.write("Are you looking to watch a Movie? A series or even Youtube Videos? ")
        st.write("if so, then you have come to the right place!")
        st.write("We can recommend something for you to watch based on something that you have already seen and very much liked.")
        st.write("We use comparison algorithms to make movie recomendations that have similar items to other movies of choice and liking.")
        image = Image.open('resources/imgs/Think.PNG')
        st.image(image, caption='')
        st.title("We think so that you don't have too :) ")
        st.write("Check out our recommenders now!")
        
        
    if page_selection == "Solution Architecture":
        st.title("Explore our architectural principles")
        image = Image.open('resources/imgs/Recommeder-Engine-Banner-1280x576.jpg')
        st.image(image, caption='')
        st.write("**Collaborative Filtering**")
        st.write("collaborative filtering uses similarities between users and items simultaneously to provide recommendations. It is also known as social filtering. Collaborative filtering uses algorithms to filter data from user reviews to make personalized recommendations for users with similar preferences.")
        
        st.write("**Content-Based Filtering**")
        st.write("Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback. it uses features of an item you have already seen to recommend others based on similarity.")
       
        image= Image.open('resources/imgs/fetch.PNG')
        st.image(image, caption='')
        st.write("**Overall solution exploration**")
        st.write("Recommender systems are information retrieval tool that allocates accurate recommendations to the specific users.In the current era of big data, the recommender system aspires to provide users with a tailored set of personalized items from a pool of a large population.Personalization systems have proved to be one of the most powerful tools for e-commerce sites, assisting users in discovering the most relevant products across enormous product catalogues.A highly performing recommendation System will suggest items that match the similarities with the highest degree of performance")
        
        image= Image.open('resources/imgs/film.PNG')
        st.image(image, caption='')
        
    if page_selection == "About us":
        st.title("We are Intuition-Tech")
        st.write("Intuition-Tech is a leading global knowledge solutions company. We help companies develop the systems and expertise they need to unlock their potential")

        st.write("Meet The Team")
        images = ['resources/imgs/zwane.PNG']
        st.image(images, use_column_width=10,  caption=["Chief Executive Officer: Honey Zwane"] )
        
        images=['resources/imgs/KRB.PNG']
        st.image(images, use_column_width=10,  caption=["Ai Engineer: Karabo Eugene Hlahla"] )
        
        images= ['resources/imgs/Lesego.PNG' ]
        st.image(images, caption=["Lesego Tiro: Product Manager"] * len(images))
        images = ['resources/imgs/Ruth.PNG']
        st.image(images, use_column_width=10,  caption=["Business Analyst"] )
                 
    if page_selection == "Contact Us":
        st.title("Call")
        images=['resources/imgs/phone.PNG']
        st.image(images, use_column_width=10,  caption=[""] )
        st.write("**+27716123800**")
        st.write("**+27781234566**")
        
        
        st.title("Email")
        images=['resources/imgs/email.PNG']
        st.image(images, use_column_width=10,  caption=[""] )
        st.write("Inttech@gmail.com")
        st.write("DataTech@gmail.com")
        
        images=['resources/imgs/social.PNG']
        st.image(images, use_column_width=10,  caption=["Copyright © 2023, Intuition-Tech"] )
        
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()

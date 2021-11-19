import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import requests
from bs4 import BeautifulSoup

def app():
    #markdown syntax
    df = pd.read_csv('college_data.csv')

    barchart = px.bar(
        data_frame = df,
        x = "college_name",
        #color = "out-of-state_tuition",
        y = "in-state_tuition",
        opacity = 0.9,
        orientation = "v",
        barmode = 'group',
        title='Annual In-State Tuition vs Out-of-state Tuition',
    )
    pio.show(barchart)
        st.write("""
        ### Average Cost: $3,957/year
        National Cost: $15,523\n

        """)

    #px.style.use('seaborn')
    #fig1, ax1 = px.subplots()
    df = pd.read_csv("pokemon_data.csv")
    df.head()
    df.columns
    df.Name.unique()
    df_Name = df
    df_Name
    #fig = px.gcf()
    px.scatter(df_Name, x='Acceptance Rate', y='Acceptance Rate', range_x=[], range_y=[], color="Name")
    #st.pyplot(fig1)
    #st.write(df.groupby('Acceptance Rate').mean())




    baseurl = 'https://www.niche.com/colleges/search/best-colleges/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
    }
    '''
    import streamlit as st
    from scrape import getData

    st.title("Github Scraper")

    userName = st.text_input('Enter Github Username')

    if userName != '':
        try:
            info, repo_info = getData(userName)

            for key , value in info.items():
                if key != 'image_url':
                    st.subheader(
                        
                        {} : {} 
                        .format(key, value)
                    )
                else:
                    st.image(value)
            st.subheader(" Recent Repositories")
            st.table(repo_info)
        except:
            st.subheader("User doesn't exist")

            '''
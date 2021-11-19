import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from bs4 import BeautifulSoup


def app():
    #markdown syntax

    df = pd.read_csv('college_data.csv')
    selected_college = st.sidebar.selectbox('Type of College', ['CUNY'])
    four_year = sorted(df.college_name.unique())
    selected_four_year = st.sidebar.multiselect('4-Year & 2-Year Colleges', four_year, four_year)    
    mask_four_year = df['college_name'].isin(selected_four_year)
    df = df[mask_four_year]

    fig = px.bar(
        data_frame = df,
        x = selected_four_year,
        y = ["in-state_tuition","out-of-state_tuition"],
        opacity = 0.9,
        orientation = "v",
        barmode = 'group',
        title='Annual In-State Tuition vs. Out-of-state Tuition',
        width = 1120,
        height = 820,
        labels={
                        "in-state_tuition": "In-State Tuition",
                        "out-of-state_tuition": "Out-of-state Tuition",
                        "x": "CUNY Colleges",
                        "value": "Tuition Cost (Annual)",
                        "variable": "In-State/Out-of-State:",
                },
    )
    fig.update_layout(
        font_family="Georgia",
        font_color="grey",
        font_size=16,
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="black"
    )

    


    st.plotly_chart(fig)   
    
    

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
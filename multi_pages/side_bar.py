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
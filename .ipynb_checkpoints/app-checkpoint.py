import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from multiapp import MultiApp
from multi_pages import cuny_data, cuny_tuition # import your app modules here

app = MultiApp()

st.markdown("""
# CUNY Statistics
""")

# Add all your application here
app.add_app("CUNY Tuition", cuny_tuition.app)
app.add_app("CUNY Ethnicity", cuny_data.app)
st.sidebar.header('User input features')

selected_college = st.sidebar.selectbox('Type of College', ['CUNY','SUNY','Private University'])

if selected_college == 'CUNY':

    four_year = sorted(['Hunter','City','Baruch','Macaulay Honors',
    'Brooklyn','Queens','City Tech','Staten Island','York',
    'Lehman','John Jay','Medgar Evers'])
    selected_four_year = st.sidebar.multiselect('4-Year Colleges', four_year, four_year)    
    
    two_year = sorted(['Borough of Manhattan CC','Bronx CC',
    'Hostos CC','Kingsborough CC','Guttman CC',
    'LaGuardia CC','Queensborough CC'])
    selected_two_year = st.sidebar.multiselect('2-Year Community Colleges', two_year, two_year)  

elif selected_college == 'SUNY':

    four_year = sorted(['Albany','New Paltz','Oswego','Buffalo','Cornell','Purchase'])
    selected_four_year = st.sidebar.multiselect('4-Year Colleges', four_year, four_year)    
    
    two_year = sorted(['ds'])
    selected_two_year = st.sidebar.multiselect('2-Year Community Colleges', two_year, two_year) 

elif selected_college == 'Private University':

    four_year = sorted(['Pace','NYU Tandon','NYU Main','Pratt Institute','Columbia','Barnard',"St John's"])
    selected_four_year = st.sidebar.multiselect('4-Year Colleges', four_year, four_year)    

    two_year = sorted(['Asa College'])
    selected_two_year = st.sidebar.multiselect('2-Year Community Colleges', two_year, two_year)
    
# The main app
app.run()
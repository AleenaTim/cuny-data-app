import streamlit as st
import pandas as pd
from multiapp import MultiApp
from multi_pages import cuny_data, cuny_tuition, cuny_home # import your app modules here


app = MultiApp()

st.markdown("""
# CUNY Statistics
""")

df = pd.read_csv('college_data.csv')
# Add all your application here
app.add_app("CUNY Home Page", cuny_home.app)
app.add_app("CUNY Tuition", cuny_tuition.app)
app.add_app("CUNY Test Scores", cuny_data.app)




#selected_college = st.sidebar.selectbox('Type of College', ['CUNY','SUNY','Private University'])


    #two_year = sorted(['Borough of Manhattan CC','Bronx CC','Kingsborough CC',
    #'LaGuardia CC','Queensborough CC'])
    #selected_two_year = st.sidebar.multiselect('2-Year Community Colleges', two_year, two_year)  

#elif selected_college == 'SUNY':
#
#    four_year = sorted(['Albany','New Paltz','Oswego','Buffalo','Cornell','Purchase'])
#    selected_four_year = st.sidebar.multiselect('4-Year Colleges', four_year, four_year)    
    
#    two_year = sorted(['ds'])
#    selected_two_year = st.sidebar.multiselect('2-Year Community Colleges', two_year, two_year) 

#elif selected_college == 'Private University':

#    four_year = sorted(['Pace','NYU Tandon','NYU Main','Pratt Institute','Columbia','Barnard',"St John's"])
#    selected_four_year = st.sidebar.multiselect('4-Year Colleges', four_year, four_year)    

#    two_year = sorted(['Asa College'])
#    selected_two_year = st.sidebar.multiselect('2-Year Community Colleges', two_year, two_year)
    
# The main app

app.run()
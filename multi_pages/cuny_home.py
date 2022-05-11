import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.figure_factory as ff
from bs4 import BeautifulSoup
import requests

def app():
    st.markdown("* *Data parsed from datausa.io*")

    df = pd.read_csv('college_data.csv')
    df1 = df[df.years > 2]
    df2 = df[df.years < 3]

    page_names = ['4-Year', '2-Year']
    cuny_type = st.sidebar.radio('Type:', page_names)
    college_selected = ''

    if cuny_type == '4-Year':
        college_selected = st.sidebar.selectbox('4-Year CUNY Colleges', sorted(df1['college_name']))
    elif cuny_type == '2-Year':
        ccollege_selected = st.sidebar.selectbox('2-Year CUNY Colleges', sorted(df2['college_name']))
    #Baruch
    if college_selected == 'Baruch':
        url = requests.get('https://datausa.io/profile/university/cuny-bernard-m-baruch-college')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()
        data_matrix = [[college_selected + ' College', 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        sizes = [8.74, 23.5, 31.7, 22.3, 2.132]
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)

    #Brooklyn
    elif college_selected == 'Brooklyn':
        url = requests.get('https://datausa.io/profile/university/cuny-brooklyn-college')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()

         
        data_matrix = [[college_selected  + ' College', 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        #Other is Two/More Races + American Indian/Alaska Native + Native Hawaiian/Other Pacific Islanders
        sizes = [22.5,23.2,19.6,29,(2.24+.225+.152)] 
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)
    #City
    elif college_selected == 'City':
        url = requests.get('https://datausa.io/profile/university/cuny-city-college')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()
        data_matrix = [[college_selected + ' College', 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        sizes = [15.5,36.6,22.8,16.8,2.18+.164+.152]
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)

    #City Tech
    elif college_selected == 'City Tech':
        url = requests.get('https://datausa.io/profile/university/cuny-new-york-city-college-of-technology')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()
        data_matrix = [['City College of Technology', 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        sizes = [28.9,34.4,19.9,9.98,1.98+.34+.252]
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)
    #City Tech
    elif college_selected == 'Hunter College':
        url = requests.get('https://datausa.io/profile/university/cuny-hunter-college')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()
        data_matrix = [[college_selected, 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        sizes = [11.1,29.2,23.9,28.5,2.52+.172+.16]
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)
    elif college_selected == 'John Jay':
        url = requests.get('https://datausa.io/profile/university/cuny-john-jay-college-of-criminal-justice')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()
        data_matrix = [[college_selected, 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        sizes = [17.3,48.2,10.7,17.6,2.32+.384+.258]
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)
    elif college_selected == 'Lehman':
        url = requests.get('https://datausa.io/profile/university/cuny-lehman-college')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()
        data_matrix = [[college_selected, 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        sizes = [27.2,55.1,6.32,7.24,1.04+.198+.185]
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)
    elif college_selected == 'Medgar Evers':
        url = requests.get('https://datausa.io/profile/university/cuny-medgar-evers-college')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()
        data_matrix = [[college_selected, 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        sizes = [76.1,15,2.81,1.66,1.6+.224+.138]
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)
    elif college_selected == 'Queens':
        url = requests.get('https://datausa.io/profile/university/cuny-queens-college')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()
        data_matrix = [[college_selected, 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        sizes = [8.62,28.4,28.1,26.9,2.28+.346+.316]
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)
    elif college_selected == 'York':
        url = requests.get('https://datausa.io/profile/university/cuny-york-college')
        soup = BeautifulSoup(url.text, 'html.parser')
        rb = soup.find('div',class_='stat-title',text="Room and Board").find_previous()
        rb = rb.get_text()
        bks = soup.find('div',class_='stat-title',text="Books and Supplies").find_previous()
        bks = bks.get_text()
        net = soup.find('div',class_='stat-title',text="2020 Value").find_previous()
        net = net.get_text()
        retention_rate = soup.find('div',class_='stat-title',text="2020 Retention Rate").find_previous()
        retention_rate = retention_rate.get_text()
        data_matrix = [[college_selected, 'Annual Cost'],
               ['Room and Board', rb],
               ['Books and Supplies', bks],
               ['Net Price (After Grants and Loans)', net],
               ['Retention Rate (2020)', retention_rate]]
        table = ff.create_table(data_matrix, index=True)
        # Make text size larger
        for i in range(len(table.layout.annotations)):
            table.layout.annotations[i].font.size = 20
        st.plotly_chart(table)
        
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Black/African American', 'Hispanic/Latino', 'Asian', 'White', 'Other'
        sizes = [38.6, 26, 22.8, 5.17, 3.994]
        explode = (0, 0, 0, 0, 0)
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']
        fig, ax1 = plt.subplots()
        patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
        colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        st.pyplot(fig)
        
        


    #CUNY College Table
    '''
    fig = go.Figure(data=[go.Table(
        header=dict(values=["4-year", "2-year"],
                    fill_color='paleturquoise',
                    font_color='gray',
                    align='left',
                    height = 50,
                    font=dict(size=26),
                    ),
        cells=dict(values=[df1.college_name, df2.college_name],
                height = 50,
                fill_color='lavender',
                align='left',
                font=dict(size=20),
                ))
    ])
    fig.update_layout(title = "CUNY Colleges",
                        width = 900,
                        height = 1320,
                        font_family='Palanquin',
                        font=dict(size=30),
                        showlegend = False)

    st.plotly_chart(fig)
    '''

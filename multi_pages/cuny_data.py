import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def app():
    #markdown syntax
    st.write("""
    (2-year colleges are filtered out)\n
    Data is sorted by average min and max scores of SAT English and Math for each 4-year CUNY college.\n
    Total max SAT score is 1600 points. Both English and Math sections each have a total of 800 points.
    """)

    page_names = ['ELA Score', 'Math Score']
    page = st.sidebar.radio('Subjects:', page_names)

    df = pd.read_csv('college_data.csv')
    df = df[df.years > 2]

    #df = pd.DataFrame({'college_name': ["Doctorate Degree",
    #                            "Master's Degree",
    #                            "Bachelor's Degree",
    #                            "Associate Degree",
    #                            "Some college, no degree",
    #                            "Hight School",
    #                            "9th 12th(no degree)",
    #                            "Less Than 9th college_name"],
    #                'sat_ela_min': [91, 69, 54, 38, 35, 29, 22, 21],
    #                'sat_ela_max': [151, 99, 84, 56, 53, 47, 37, 34]})

    sat_ela_min = list(map(lambda y: str(y), df['sat_ela_min']))
    sat_ela_max = list(map(lambda y: str(y), df['sat_ela_max']))

    sat_math_min = list(map(lambda y: str(y), df['sat_math_min']))
    sat_math_max = list(map(lambda y: str(y), df['sat_math_max']))

    fig = go.Figure()

    if page == 'ELA Score':
        for i in range(0, len(df)):

            fig.add_trace(go.Scatter(y = np.linspace(df['sat_ela_min'][i], df['sat_ela_max'][i], 1000),
                                    x = 1000*[df['college_name'][i]],
                                    mode = 'markers',
                                    marker = {'color': np.linspace(df['sat_ela_min'][i], df['sat_ela_max'][i], 1000),
                                            'colorscale': ['#E1A980', '#8DAEA6'],
                                            'size': 8}))

        fig.add_trace(go.Scatter(y = df['sat_ela_min'],
                                x = df['college_name'],
                                marker = dict(color = '#CC5600', size = 14),
                                mode = 'markers+text',
                                text = sat_ela_min,
                                textposition = 'middle left',
                                textfont = {'color': '#CC5600'},
                                name = 'Woman'))

        fig.add_trace(go.Scatter(y = df['sat_ela_max'],
                                x = df['college_name'],
                                marker = dict(color = '#237266', size = 14),
                                mode = 'markers+text',
                                text = sat_ela_max,
                                textposition = 'middle right',
                                textfont = {'color': '#237266'},
                                name = 'sat_ela_max'))

        fig.update_layout(title = "Average SAT ELA Scores",
                        width = 1120,
                        height = 820,
                        showlegend = False)

        fig.update_yaxes(range = [200,800])

        st.plotly_chart(fig) 

    elif page == 'Math Score':
        for i in range(0, len(df)):

            fig.add_trace(go.Scatter(y = np.linspace(df['sat_math_min'][i], df['sat_math_max'][i], 1000),
                                    x = 1000*[df['college_name'][i]],
                                    mode = 'markers',
                                    marker = {'color': np.linspace(df['sat_math_min'][i], df['sat_math_max'][i], 1000),
                                            'colorscale': ['#E1A980', '#8DAEA6'],
                                            'size': 8}))

        fig.add_trace(go.Scatter(y = df['sat_math_min'],
                                x = df['college_name'],
                                marker = dict(color = '#CC5600', size = 14),
                                mode = 'markers+text',
                                text = sat_ela_min,
                                textposition = 'middle left',
                                textfont = {'color': '#CC5600'},
                                name = 'Woman'))

        fig.add_trace(go.Scatter(y = df['sat_math_max'],
                                x = df['college_name'],
                                marker = dict(color = '#237266', size = 14),
                                mode = 'markers+text',
                                text = sat_ela_max,
                                textposition = 'middle right',
                                textfont = {'color': '#237266'},
                                name = 'sat_math_max'))

        fig.update_layout(title = "Average SAT Math Scores",
                        width = 1120,
                        height = 820,
                        showlegend = False)

        fig.update_yaxes(range = [200,800])

        st.plotly_chart(fig) 

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    
    #df = pd.read_csv("college_data.csv")
    #labels = 'Black', 'White', 'Asian', 'Hispanic', 'Other'
    #sizes = [15, 30, 45, 10, 10]
    #explode = (0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    #colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']

    #fig1, ax1 = plt.subplots()
    #patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
    #colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    #ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    #draw circle
    #centre_circle = plt.Circle((0,0),0.70,fc='white')
    #fig = plt.gcf()
    #fig.gca().add_artist(centre_circle)

   # for text in texts:
   #     text.set_color('grey')

   # for autotext in autotexts:
    #    autotext.set_color('grey')

    #st.pyplot(fig1)
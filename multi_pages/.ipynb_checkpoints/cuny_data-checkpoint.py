import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def app():
    #markdown syntax
    st.write("""

    Data is sorted by ethnicity, tuition cost, in-campus housing, etc.

    """)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    
    df = pd.read_csv("pokemon_data.csv")
    labels = set(df['Name'])
    #'Black', 'White', 'Asian', 'Hispanic', 'Other'
    sizes = [15, 30, 45, 10, 10]
    explode = (0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#99ffff']

    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, 
    colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    for text in texts:
        text.set_color('grey')

    for autotext in autotexts:
        autotext.set_color('grey')

    

    st.pyplot(fig1)
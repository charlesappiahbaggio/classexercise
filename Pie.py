import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

st.title("My First Place")

st.subheader('Raw Data')

st.write("This shows the Scatter plot")

data = pd.read_csv("https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv")

st.scatter_chart(data, x="flipper_length_mm", y="body_mass_g", color="species")

st.sidebar.header("Filter the Options")

selected_category = st.sidebar.selectbox('Select Category', options=['All', 'Adeilade', 'Gento', 'Chinstrap'])

if selected_category != "All":
    filtered_data = data[data['species'] == selected_category]
    st.scatter_chart(filtered_data, x="flipper_length_mm", y="body_mass_g", color="sex")
else:
    st.scatter_chart(data, x="flipper_length_mm", y="body_mass_g", color="sex")


st.write(data)

species_count = data['species'].value_counts()

st.bar_chart(species_count)

import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv("https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv")

# Check for missing data and handle it if necessary
data = data.dropna(subset=['species'])

# Create a pie chart for the species distribution
species_counts = data['species'].value_counts()

# Display the pie chart in Streamlit
st.title("Penguins Species Distribution")
st.write("This pie chart represents the distribution of different penguin species in the dataset.")

# Streamlit's pie chart functionality
st.write(species_counts)
st.pyplot(species_counts.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8)).get_figure())





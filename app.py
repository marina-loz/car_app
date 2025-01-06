import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv('cleaned_vehicles.csv')

# Streamlit App Header
st.header("Car Sales Dashboard")

# Layout: Filters in a Row
col1, col2, col3 = st.columns(3)

with col1:
    # Price Slider
    price_min, price_max = st.slider(
        "Select Price Range:",
        min_value=int(df['price'].min()),
        max_value=int(df['price'].max()),
        value=(int(df['price'].min()), int(df['price'].max()))
    )

with col2:
    # Model Year Slider
    model_year_min, model_year_max = st.slider(
        "Select Model Year Range:",
        min_value=int(df['model_year'].min()),
        max_value=int(df['model_year'].max()),
        value=(int(df['model_year'].min()), int(df['model_year'].max()))
    )

with col3:
    # Car Type Multiselect
    car_types = df['type'].unique()
    selected_types = st.multiselect(
        "Select Car Type(s):",
        options=car_types,
        default=car_types
    )
# Filter the data based on slider values
filtered_data = df[
    (df['price'] >= price_min) &
    (df['price'] <= price_max) &
    (df['model_year'] >= model_year_min) &
    (df['model_year'] <= model_year_max) &
    (df['type'].isin(selected_types))
]

# Layout: Visualizations in Columns
st.subheader("Visualizations")

# Row 1: Histogram and Scatter Plot side by side
col4, col5 = st.columns(2)

with col4:
    st.subheader("Price Distribution")
    fig_histogram = px.histogram(
        filtered_data,
        x='price',
        nbins=100,
        title='Distribution of Prices',
        labels={'price': 'Price (USD)'},
        color_discrete_sequence=['#636EFA']
    )
    st.plotly_chart(fig_histogram)

with col5:
    st.subheader("Price vs Model Year")
    fig_scatter = px.scatter(
        filtered_data,
        x='model_year',
        y='price',
        color='type',
        title='Price Distribution by Model and Type of Car',
        labels={'price': 'Price (USD)', 'model_year': 'Model Year'},
        hover_data=['type'],
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(fig_scatter)

# Optional: Show Filtered Data
if st.checkbox("Show Filtered Data"):
    st.write(filtered_data)


# Car Sales Dashboard
Link to my project: https://car-app-4i42.onrender.com
This project is an interactive web application built using **Streamlit** to visualize and explore car sales advertisements. The application allows users to filter data dynamically and analyze car prices, model years, and types through various visualizations.

---

## Features

- **Interactive Price Filter**: Adjust the price range to view cars within a specific budget.
- **Car Type Filter**: Select one or more car types to refine the dataset.
- **Dynamic Visualizations**:
  - Histogram showing the distribution of car prices.
  - Scatter plot exploring the relationship between model year, price, and car type.
- **Cleaned Dataset**: Preprocessed data ensures accurate and insightful analysis.

---

## Technologies Used

- **Python**: Core programming language for data manipulation and web app development.
- **Streamlit**: Framework for building interactive web applications.
- **Pandas**: Data analysis and preprocessing.
- **Plotly Express**: Creating dynamic and interactive visualizations.

---

## Installation and Setup

Follow these steps to run the application locally:

1. **Clone the Repository**:
   git clone https://github.com/marina-loz/car_app.git
   cd car_app
2. **Set Up the Virtual Environment**:
      python -m venv env
      source env/bin/activate  # On Windows: env\Scripts\activate
3. **Install Dependencies**:
pip install -r requirements.txt

4. **Run the Application**:
streamlit run app.py

5. **Open your browser and navigate to the URL provided** (typically http://localhost:8506).

## Dataset

The dataset used for this project is the **Vehicles US Dataset** (`vehicles_us.csv`). It contains information on car sales advertisements, including price, model year, type, and other relevant features.

---

## Deployment

The application is deployed on **Render**, making it accessible to the public. You can view the live demo here:


---

## How to Use the Application

1. **Use the Price Slider**: Filter cars within a specific price range.
2. **Use the Car Type Multiselect**: Choose the car types you want to analyze.
3. **Explore the Visualizations**:
   - **Histogram**: Analyze price distribution.
   - **Scatter Plot**: Examine price trends by model year and car type.
4. **View the Filtered Dataset**: Use the checkbox to see the filtered data directly.

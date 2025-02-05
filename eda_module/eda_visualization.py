import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
from eda import *

st.header("Exploratory Data Analysis")
# File uploader for CSV files
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    # Load data
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())
    # Streamlit App
    data_overview(df)

    # Check for missing values
    check_missing_values(df)

    # Display data types and unique values
    data_types_and_uniques(df)

    # Handle duplicate rows
    handle_duplicates(df)

    #univariate analysis
    st.title("Univariate Analysis")
    # Perform univariate analysis
    univariate_analysis(df)
    st.title("Bivariate Analysis")
    # Perform univariate analysis
    # Let the user select the target column
    target_column = st.selectbox("Select Target Column", df.columns)
    
    # Perform bivariate analysis if a target column is selected
    if target_column:
        st.write(f"Performing bivariate analysis with target column: {target_column}")
        bivariate_analysis(df, target_column)

    st.title("Categorical Count Plot Analysis")
    # Perform univariate analysis
    visualize_categorical(df)


    # Generate Correlation Heatmap
    correlation_heatmap(df)

    # Outlier Detection for numeric columns
    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns
    detect_outliers(df, numeric_columns)


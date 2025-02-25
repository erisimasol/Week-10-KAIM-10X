# Week-10-Task-01.ipynb

## Overview
This project file contains a detailed analysis of Brent Oil Prices that takes advantage of Python's sophisticated data analysis modules. Data loading, exploration, statistical summaries, visualisations, and preliminary predictive modelling stages are all part of the procedure.

### Importing Libraries
The notebook begins by importing essential libraries:

- **Pandas**: For efficient data manipulation and analysis through DataFrames.
- **NumPy**: Offers support for large, multi-dimensional arrays and matrices, along with mathematical functions.
- **Seaborn**: A statistical data visualization library built on Matplotlib, used for creating attractive and informative graphics.
- **Matplotlib**: A foundational plotting library for creating static, animated, and interactive visualizations in Python.
- **scikit-learn**: A machine learning library that provides tools for data mining and data analysis, including **regression models and metrics**.
**sklearn.model_selection import train_test_split**
**sklearn.ensemble import RandomForestRegressor**
from **sklearn.metrics import mean_squared_error**
**import requests**
**import time**
from **IPython.display import clear_output**
**ruptures matplotlib pandas**
**import ruptures as rpt**
**pip install requests pandas matplotlib ipywidgets**
**statsmodels.tsa.arima.model import ARIMA**
 **statsmodels.tsa.stattools import adfuller**
**pandas numpy matplotlib arch**
**import yfinance as yf**
**import pandas as pd**
 **flask import Flask, request, jsonify**
 **sklearn.model_selection import train_test_split**
**sklearn.linear_model import LinearRegression**
**import numpy as np**
**import json**

### Loading Data
- The dataset `BrentOilPrices.csv` is loaded into a DataFrame called `BOP` using `pd.read_csv()`.
- The `head()` method displays the first five rows, giving an overview of the data structure, which includes columns for date and price.

### Checking Data Types and Missing Values or EDA
- A markdown cell introduces this section.
- The `info()` method is called to summarize the DataFrame, providing insights into data types (e.g., object for dates and float64 for prices) and checking for missing values.
- This is critical for ensuring data quality before analysis, as missing values can skew results.

- The notebook provides a statistical summary using the `describe()` method, which includes:
  - **Count**: Total number of entries.
  - **Mean**: Average price of Brent oil.
  - **Standard Deviation (std)**: Measure of price volatility.
  - **Min/Max**: Minimum and maximum price observed.
  - **Quartiles (25%, 50%, 75%)**: Provide insights into the distribution of prices.

###  Data Visualization
- A section dedicated to visualizing the price trends over time.
- The notebook utilizes Matplotlib and Seaborn for plotting a line graph that illustrates how Brent Oil prices have changed.
- This visualization helps identify trends, seasonal patterns, and potential outliers in the data.

### Future Directions
- While the notebook provides a foundational analysis, several additional steps can be taken for deeper insights:
  - **Time Series Analysis**: Decomposing the time series to understand seasonality and trends.
  - **Forecasting**: Using machine learning models like ARIMA or Random Forest to predict future prices.
  - **Correlation Analysis**: Examining how Brent Oil prices correlate with other economic indicators, such as currency exchange rates or global oil demand.
  - **Anomaly Detection**: Identifying unusual spikes or drops in prices to inform trading strategies or economic predictions.


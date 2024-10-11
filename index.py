import csv
from bs4 import BeautifulSoup
import glob
import os
import requests
import pandas as pd


def getPM():
    # Let's calculate the average annual growth rate based on the provided profit data.
    profits = [96773, 81462, 53823, 31536]
    
    # Number of years between the first and last data points
    years = len(profits) - 1
    
    # Using the formula for average annual growth rate:
    # (Final Value / Initial Value)^(1/years) - 1
    average_growth_rate = ((profits[0] / profits[-1]) ** (1 / years)) - 1
    
    # Converting to percentage
    average_growth_rate_percentage = average_growth_rate * 100
    return average_growth_rate_percentage


# Function to fetch data from Yahoo Finance
def getDataYahoo(stonk):
    url = f"https://finance.yahoo.com/quote/{stonk}/"


# Define the folder path
folder_path = 'input'

# Use glob to find all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Initialize an empty DataFrame to store the data
data = pd.DataFrame()

# Loop through each file and read its content
for file in csv_files:
    with open(file, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            stock_data = getDataYahoo(row[0])  # Get data for each stock

# Display the collected data
print(data)

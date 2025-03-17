#This is a data cleaning application 
# importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os 
import random

def data_cleaning_wizard(data_path,data_name):
    print("thank you for giving me the opportunity to clean your data")
    t=random.randint(1,10)
    print(f"Cleaning your data will take {t} seconds")
    time.sleep(t)
    print("Data cleaning in progress")
    #checking if the path is valid

    while not os.path.exists(data_path):
        print("oops! the path is not valid")
        print("Please enter a valid path")
        data_path = input("Enter the path of the data file: ")

    #checking the file type
    if data_path.endswith('.csv'):
        print("The file is a csv file")
        data=pd.read_csv(data_path, encoding_errors='ignore')

    elif data_path.endswith('.xlsx'):
        print("The file is an excel file")
        data=pd.read_excel(data_path)
    elif data_path.endswith('.xls'):
        print("The file is an excel file")
        data=pd.read_excel(data_path)
    else:
        print("The file is not in a valid format")
        return
    #showing the number of records in the data
    
    print("please wait things are happening")
    time.sleep(t)
    print("The number of records in the data is: ", len(data))
    #showing the number of rows and cloumns in the data
    print(f"Data contains total rows: {data.shape[0]} and columns {data.shape[1]} in the data")

    #cleaning

    #checking for duplicates
    print("Checking for duplicates")
    time.sleep(t)
    duplicates=data.duplicated()
    total_duplicates=duplicates.sum()
    print(f"The number of duplicates in the data is: {total_duplicates}")

    #saving the duplicates in a new file
    if total_duplicates>0:

        duplicates_data=data[duplicates]
        duplicates_data.to_csv(f"{data_name}_duplicates.csv", index=None)
        print("Duplicates saved in duplicates.csv")

    #deleting the duplicates
    df= data.drop_duplicates()
    print("Duplicates deleted")
    
    print("Checking for missing values")
    time.sleep(t)

    #finding missing values
    total_missing_value=df.isnull().sum().sum()
    missing_value_by_column=df.isnull().sum()
    print(f"The total missing values in the data is: {total_missing_value}")
    print(f"The missing values by column is:\n {missing_value_by_column}")

    print("Dealing with missing values")
    time.sleep(t)
    #dealing with missing values
    #filling missing values with the mean of the column
    #fillna-- int or float
    #dropna-- any object
    columns=df.columns
    for col in columns:
        #replacing missing values with the mean for int and float
        if df[col].dtype in ['int64', 'float64']:
            mean=df[col].mean()
            df[col]=df[col].fillna(mean)
        else:
            #dropping missing values for any object
            df.dropna


    
 
    print(f"Data is cleaned,number of Rows {df.shape[0]} and columns {df.shape[1]}")
#saving the cleaned data
    df.to_csv(f"{data_name}_cleaned.csv", index=None)
    print("Data saved as cleaned.csv")
    
if __name__ == "__main__":
    data_path=input("Enter the path of the data file: ")
    data_name=input("Enter the name of the data file: ")
    data_cleaning_wizard(data_path,data_name)

import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd
import numpy as np

def populate_with_mutlpile_boolean_columns(dataframe_to_use_for_total_of_num_rows,list_to_use):

    # Define the number of rows and columns
    num_rows = len(dataframe_to_use_for_total_of_num_rows) 
    num_columns = len(list_to_use) #50 campos

    # Create an empty dictionary to store column data
    column_data = {}

    # Populate the dictionary with default values for each column
    for i in range(num_columns):
        column_name = list_to_use[i]
        default_value = False
        column_data[column_name] = [default_value] * num_rows

    # Create the DataFrame using the populated dictionary
    df_result= pd.DataFrame(column_data)
    return df_result

def totals_of_a_string_column(pandas_df,columns_as_a_list,column_name=''):
    if column_name=='':
        column_name='Generic_Column'
    pandas_df_counts = pandas_df[columns_as_a_list].value_counts().reset_index()
    pandas_df_counts.columns = [column_name, 'Count']
    #df_genres_totals = pd.DataFrame(dict_genres_totals)
    return pandas_df_counts

def save_totals_of_a_string_column(pandas_df,column_name_as_string,date_column_name_as_string,date_start='1963-01-01',date_end='2023-12-31',frequency='5Y'):
    #frequency =freq
    start_date = pd.to_datetime(date_start)
    end_date = pd.to_datetime(date_end)
    date_range = pd.date_range(start=start_date, end=end_date, freq=frequency)
    
    
    ##check if folder exists
    folder_path=f"./data_{column_name_as_string}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    list_of_dataframes=[]
    # Iterate through date intervals
    for i in range(len(date_range) - 1):
        
        start = date_range[i]
        end = date_range[i + 1]
        # Filter the dataset for the current interval
        interval_data = pandas_df[(pandas_df[date_column_name_as_string] >= start) & (pandas_df[date_column_name_as_string] < end)]

        # Calculate genre counts for the current interval
        #genre_columns = interval_data.loc[:, genres]  # Adjust column names accordingly
        pandas_df_counts = interval_data[column_name_as_string].value_counts().reset_index()
        pandas_df_counts.columns = [column_name_as_string, 'Count']
        str_start_date= str(start.year)+"/01/01"
        str_end_date= str(end.year)+"/12/31"
        pandas_df_counts['start_date'] = pd.to_datetime(str_start_date)
        pandas_df_counts['end_date'] =  pd.to_datetime(str_end_date)
        
        # Save the dataset for the current interval (you can save it to a file or use as needed)
        file_name = f"./data_{column_name_as_string}/{column_name_as_string}/{column_name_as_string}_counts_{start.year}-{end.year}.csv"
        pandas_df_counts.reset_index(inplace=True)
        pandas_df_counts.index.name="index"
        pandas_df_counts.to_csv(file_name, index=False,sep=";")  # Save to a CSV file
        list_of_dataframes.append(pandas_df_counts)
    return list_of_dataframes
    #in groups of five years by default

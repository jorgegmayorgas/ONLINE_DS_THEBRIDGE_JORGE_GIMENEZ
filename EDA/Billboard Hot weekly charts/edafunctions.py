import matplotlib.pyplot as plt
import seaborn as sns
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
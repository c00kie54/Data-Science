#This file will contain the function to load data.

def data_read(name): 
    data =pd.read_csv(name)
    print('Data Loaded Sucessfully')
    return data
# Remeber to set the variable name from data.
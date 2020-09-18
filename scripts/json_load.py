#This script will load JSON and if the shape(m,n) is m<n then it will transpose it
import pandas as pd
import numpy as np
def json_load(json_name):
    data = pd.read_json(json_name) #Read JSON
    print('JSON Loaded Sucessfully') 
    m,n = data.shape #Provides two variables of the shape
    if n>m: #IF n>m then data needs to be transposed.
        data = data.T
        return data   
    return data

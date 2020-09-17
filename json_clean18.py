#This script will clean the json needed for the 2018/2019 dataset
import pandas as pd
import numpy as np
def json_clean18(json_data18):
    json_data18.drop(json_data18.columns.difference(['Club','Position']), 1, inplace=True)
    json_data18 =json_data18.reset_index()
    json_data18.columns = ['name', 'Club','Position']
    json_data18 =json_data18.sort_values(by=['name'])
    json_data18 = json_data18.replace({' ':''}, regex=True)
    print('JSON data cleaned')
    return json_data18
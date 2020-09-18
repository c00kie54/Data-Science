# This script will bring together all the seperate function scripts to predict the best fantasy football team for the 2020/2021 season.

## Start with importing the correct packages.
import pandas as pd
import numpy as np

# Import the correct scripts.

from Load_data import data_read
from json_load import json_load
from players1819_clean import data_clean1819
from json_clean18 import json_clean18
from data1819_merge import data1819_merge
from fixtures18_clean import fix18_clean
from players1920_clean import player1920_clean
from fixtures1920_clean import fix1920_clean
from matchweek1920_clean import mw1920_clean
from fixt_mw_merge import fix_mw2021
from data1819_1920_merge import data_merge

# Lets load the 2018/2019 player data. 
name = '/Users/alexcooke/Desktop/Player_Prices/players_1819.csv'
player1819 = data_read(name)

# Lets load the 2018/2019 player/team JSON
json_name = '/Users/alexcooke/Desktop/Player_Prices/fpl_data_2018_2019.json'
json1819 = json_load(json_name)

# Lets clean the 2018/2019 player data
player1819 = data_clean1819(player1819)

# Lets clean the 2018/2018 JSON data
json1819 = json_clean18(json1819)

# Merging the data and cleaning the merge
data1819 = data1819_merge(player1819,json1819)

# View the head of the cleaned data
data1819.head()

# Loading the Fixtures for 2018/2019 season
name = '/Users/alexcooke/Desktop/Player_Prices/Fixtures_1819.csv'
fixtures1819 = data_read(name)

# Cleaning the Fixtures for 2018/2019 season
fixtures1819 = fix18_clean(fixtures1819)

# Load in the 2019/2020 player data
name = '/Users/alexcooke/Desktop/Player_Prices/players_1920_fin.csv'
player1920 = data_read(name)

# Clean the 2019/2020 player data
player1920 = player1920_clean(player1920)

# Load the fixtures for 2019/2020
name = '/Users/alexcooke/Desktop/Player_Prices/fixtures.csv'
fixtures1920 = data_read(name)

# Load the matchweeks foro 2019/2020
name = '/Users/alexcooke/Desktop/Player_Prices/Matchweeks.csv'
matchweeks1920 = data_read(name)

# Clean the fixtures for 2019/2020 
fixtures1920 = fix1920_clean(fixtures1920)

# Clean the matchweeks for 2019/2020
matchweeks1920 = mw1920_clean(matchweeks1920)

# Setting the matchweeks for each date in 2020/2021 season. 
fixtures2021 = fix_mw2021(fixtures1920,matchweeks1920)
print(fixtures1920)

#Merge the 2018/2019 and 2019/2020 datasets
player_data = data_merge(data1819, player1920)

print(data1819)
print(player1920)
print(data1819.columns)
print(player1920.columns)
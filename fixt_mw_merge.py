#Merging the fixtures and matchweek to create new dataframe
import pandas as pd
import numpy as np 
import datetime
def fix_mw2021(fixtures, matchweeks):
    matchweeks.End[15:] = matchweeks.End[15:] + pd.offsets.DateOffset(years=1)
    matchweeks.Start[16:] = matchweeks.Start[16:] + pd.offsets.DateOffset(years=1)
    for i in range(39):
        for g in range(380):
            if fixtures.game_date[g]>= matchweeks.Start[i] and fixtures.game_date[g]<= matchweeks.End[i]:
                fixtures.Matchweek[g] = matchweeks.Matchweek[i]
    return fixtures        
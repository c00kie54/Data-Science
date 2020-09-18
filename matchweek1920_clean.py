# Cleaning the 2019/2020 matchweek data
import pandas as pd
import numpy as np
import datetime
from datetime import datetime
def mw1920_clean(matchweek):
    matchweek = matchweek.replace({':':''}, regex=True)
    look_up = {'January':'01','February' :'02', 'March' :'03', 'April' :'04', 'May' :'05',
            'June':'06', 'July' :'07',  'August':'08',  'September':'09','October':'10', 'November':'11', 'December':'12'}
    matchweek['Start_Month'] = matchweek['Start_Month'].apply(lambda x: look_up[x])
    matchweek['End_Month'] = matchweek['End_Month'].apply(lambda x: look_up[x])
    matchweek["Year"] = 2020
    temp1 = matchweek[["Year", "Start_Month", "Start_Date"]].copy()
    temp1.columns = ["year", "month", "day"]
    temp2 = matchweek[["Year", "End_Month", "End_Date"]].copy()
    temp2.columns = ["year", "month", "day"]
    matchweek["Start"] = pd.to_datetime(temp1)
    matchweek["End"] = pd.to_datetime(temp2)
    matchweek = matchweek.drop(['Day','Start_Date','Start_Month','End_Date','End_Month','Year'], axis=1)
    print('Matchweeks 2019/2020 cleaned')
    return matchweek
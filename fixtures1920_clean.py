# Clean the fixtures for 2019/2020 season
import pandas as pd
import numpy as np
import datetime
from datetime import datetime
def fix1920_clean(fixtures):
    fixtures['game_date']= pd.to_datetime(fixtures['game_date']) 
    fixtures['Matchweek']=''
    fixtures['home_team'] = fixtures.home_team.replace({'Wolves':'8',
                                                    'West Ham United':'11',
                                                    'Sheffield United':'10',
                                                    'Tottenham Hotspur':'4',
                                                    'Southampton':'12',
                                                    'Newcastle United':'15',
                                                    'Man United':'5',
                                                    'Man City':'3',
                                                    'Liverpool':'1',
                                                    'Leicester City':'6',
                                                    'Aston Villa':'18',
                                                    'Fulham':'19',
                                                    'Everton':'9',
                                                    'Crystal Palace':'13',
                                                    'Chelsea':'2',
                                                    'West Brom':'20',
                                                    'Burnley':'14',
                                                    'Brighton':'16',
                                                    'Leeds United':'17',
                                                    'Arsenal':'7',                         
                                                   
                                                   }, regex=True)
    fixtures['away_team'] = fixtures.away_team.replace({'Wolves':'8',
                                                    'West Ham United':'11',
                                                    'Sheffield United':'10',
                                                    'Tottenham Hotspur':'4',
                                                    'Southampton':'12',
                                                    'Newcastle United':'15',
                                                    'Man United':'5',
                                                    'Man City':'3',
                                                    'Liverpool':'1',
                                                    'Leicester City':'6',
                                                    'Aston Villa':'18',
                                                    'Fulham':'19',
                                                    'Everton':'9',
                                                    'Crystal Palace':'13',
                                                    'Chelsea':'2',
                                                    'West Brom':'20',
                                                    'Burnley':'14',
                                                    'Brighton':'16',
                                                    'Leeds United':'17',
                                                    'Arsenal':'7',                         
                                                   
                                                   }, regex=True)

    return fixtures
                    


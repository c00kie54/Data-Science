#This function will clean the 2018/2019 fixtures data.

def fix18_clean(fixtures):
    fixtures = fixtures.drop(['code',
                              'deadline_time',
                               'deadline_time_formatted',
                               'event_day',
                               'finished',
                               'finished_provisional',
                               'id',
                               'kickoff_time',
                               'kickoff_time_formatted',
                               'minutes',
                               'provisional_start_time',
                               'started',
                               'stats'
                               ],axis=1)
    cols = ['event','team_h_difficulty','team_a_difficulty','team_h','team_a','team_h_score','team_a_score']
    fixtures = fixtures[cols]
    fixtures['team_h'] = fixtures['team_h'].astype(str) 
    fixtures['team_a'] = fixtures['team_a'].astype(str) 
    fixtures['team_h'] = fixtures.team_h.replace({'20':'WolverhamptonWanderers',
                                                    '19':'WestHamUnited',
                                                    '18':'Watford',
                                                    '17':'TottenhamHotspur',
                                                    '16':'Southampton',
                                                    '15':'NewcastleUnited',
                                                    '14':'ManchesterUnited',
                                                    '13':'ManchesterCity',
                                                    '12':'Liverpool',
                                                    '11':'LeicesterCity',
                                                    '10':'HuddersfieldTown',
                                                    '9':'Fulham',
                                                    '8':'Everton',
                                                    '7':'CrystalPalace',
                                                    '6':'Chelsea',
                                                    '5':'CardiffCity',
                                                    '4':'Burnley',
                                                    '3':'BrightonandHoveAlbion',
                                                    '2':'AFCBournemouth',
                                                    '1':'Arsenal'                         
                                                   }, regex=True)
    fixtures['team_a'] = fixtures.team_a.replace({'20':'WolverhamptonWanderers',
                                                    '19':'WestHamUnited',
                                                    '18':'Watford',
                                                    '17':'TottenhamHotspur',
                                                    '16':'Southampton',
                                                    '15':'NewcastleUnited',
                                                    '14':'ManchesterUnited',
                                                    '13':'ManchesterCity',
                                                    '12':'Liverpool',
                                                    '11':'LeicesterCity',
                                                    '10':'HuddersfieldTown',
                                                    '9':'Fulham',
                                                    '8':'Everton',
                                                    '7':'CrystalPalace',
                                                    '6':'Chelsea',
                                                    '5':'CardiffCity',
                                                    '4':'Burnley',
                                                    '3':'BrightonandHoveAlbion',
                                                    '2':'AFCBournemouth',
                                                    '1':'Arsenal'                        
                                                   }, regex=True)
    print(fixtures)                                              
    return fixtures

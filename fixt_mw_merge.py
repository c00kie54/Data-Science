#Merging the fixtures and matchweek to create new dataframe

def fix_mw1920(fixtures, matchweeks):
    for i in range(38):
        for g in range(380):
            if fixtures.game_date[g] >= matchweeks.Start[i] and fixtures.game_date[g]  < matchweeks.End[i]:
                fixtures.Matchweek[g] = matchweeks.Matchweek[i]
    return

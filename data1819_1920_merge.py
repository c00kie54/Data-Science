# Concatting the data. Need to make the columns uniform. Some neeed dropping, others need renaming.

def data_merge(data1819, data1920):
    data1819 = data1819.drop(['attempted_passes',
                                'big_chances_created',
                                'bps',
                                'clearances_blocks_interceptions',
                                'completed_passes',
                                'dribbles',
                                'ea_index',
                                'element',
                                'errors_leading_to_goal',
                                'fixture',
                                'errors_leading_to_goal_attempt',
                                'fixture',
                                'fouls',
                                'ict_index',
                                'id',
                                'key_passes',
                                'kickoff_time',
                                'kickoff_time_formatted',
                                'loaned_in',
                                'loaned_out',
                                'offside',
                                'open_play_crosses',
                                'penalties_conceded',
                                'recoveries',
                                'selected',
                                'tackled',
                                'tackles',
                                'target_missed',
                                'value',
                                'winning_goals',
                                'GW'],axis=1)
    
    #player_data = pd.concat(data1819,data1920)
    return player_data


#This script will merge the player 2018/2019 data with the JSON 2018/2019 data.
# There is some clean up needed after the merge. 
def data1819_merge(Players1819,json1819):
    #Merge
    data1819 = Players1819.merge(json1819, how='left')
    #Data Clean up
    data1819 =data1819.sort_values(by=['name'])
    data1819.loc[data1819["name"]=="AaronRowe", "Club"] = 'HuddersfieldTown'
    data1819.loc[data1819["name"]=="AaronRowe", "Position"] = 'Midfielder'
    data1819.loc[data1819["name"]=="Abd-Al-AliMorakinyoOlaposiKoiki", "Club"] = 'Burnley'
    data1819.loc[data1819["name"]=="Abd-Al-AliMorakinyoOlaposiKoiki", "Position"] = 'Defender'
    data1819.loc[data1819["name"]=="AdamaTraoré", "Club"] = 'WolverhamptonWanderers'
    data1819.loc[data1819["name"]=="AdamaTraoré", "Position"] = 'Midfielder'
    data1819.loc[data1819["name"]=="AlexMcCarthy", "Club"] = 'Southampton'
    data1819.loc[data1819["name"]=="", "Position"] = 'Goalkeeper'
    data1819.loc[data1819["name"]=="BenDavies", "Club"] = 'TottenhamHotspur'
    data1819.loc[data1819["name"]=="", "Position"] = 'Defender'
    data1819.loc[data1819["name"]=="BonatiniLohnerMaiaBonatini", "Club"] = 'WolverhamptonWanderers'
    data1819.loc[data1819["name"]=="BonatiniLohnerMaiaBonatini", "Position"] = 'Forward'
    data1819.loc[data1819["name"]=="CharlieTaylor", "Club"] = 'Burnley'
    data1819.loc[data1819["name"]=="CharlieTaylor", "Position"] = 'Defender'
    data1819.loc[data1819["name"]=="DavinsonSánchez", "Club"] = 'TottenhamHotspur'
    data1819.loc[data1819["name"]=="DavinsonSánchez", "Position"] = 'Defender'
    data1819.loc[data1819["name"]=="GonzaloHiguain", "Club"] = 'Chelsea'
    data1819.loc[data1819["name"]=="GonzaloHiguain", "Position"] = 'Forward'
    data1819.loc[data1819["name"]=="HarveyBarnes", "Club"] = 'LeicesterCity'
    data1819.loc[data1819["name"]=="HarveyBarnes", "Position"] = 'Midfielder'
    data1819.loc[data1819["name"]=="JackStephens", "Club"] = 'Southampton'
    data1819.loc[data1819["name"]=="JackStephens", "Position"] = 'Defender'
    data1819.loc[data1819["name"]=="JoelWard", "Club"] = 'CrystalPalace'
    data1819.loc[data1819["name"]=="JoelWard", "Position"] = 'Defender'
    data1819.loc[data1819["name"]=="KayneRamsay", "Club"] = 'Southampton'
    data1819.loc[data1819["name"]=="KayneRamsay", "Position"] = 'Defender'
    data1819.loc[data1819["name"]=="MasonGreenwood", "Club"] = 'ManchesterUnited'
    data1819.loc[data1819["name"]=="MasonGreenwood", "Position"] = 'Forward'
    data1819.loc[data1819["name"]=="MichaelObafemi", "Club"] = 'Southampton'
    data1819.loc[data1819["name"]=="MichaelObafemi", "Position"] = 'Forward'
    data1819.loc[data1819["name"]=="MiguelAlmiron", "Club"] = 'NewcastleUnited'
    data1819.loc[data1819["name"]=="MiguelAlmiron", "Position"] = 'Forward'
    data1819.loc[data1819["name"]=="PhilJones", "Club"] = 'ManchesterUnited'
    data1819.loc[data1819["name"]=="PhilJones", "Position"] = 'Defender'
    data1819.loc[data1819["name"]=="RaheemSterling", "Club"] = 'ManchesterCity'
    data1819.loc[data1819["name"]=="RaheemSterling", "Position"] = 'Forward'
    data1819.loc[data1819["name"]=="ShaneLong", "Club"] = 'Southampton'
    data1819.loc[data1819["name"]=="ShaneLong", "Position"] = 'Forward'
    data1819.loc[data1819["name"]=="StuartArmstrong", "Club"] = 'Southampton'
    data1819.loc[data1819["name"]=="StuartArmstrong", "Position"] = 'Midfielder'
    data1819.loc[data1819["name"]=="YouriTielemans", "Club"] = 'LeicesterCity'
    data1819.loc[data1819["name"]=="YouriTielemans", "Position"] = 'Midfielder'
    data1819 = data1819.dropna()
    print('2018/2019 datasets have been merged and cleaned')
    data1819['opponent_team'] = data1819['opponent_team'].astype(str) 
    data1819['opponent_team'] = data1819.opponent_team.replace({'20':'WolverhamptonWanderers',
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
                                                    '1':'Arsenal' ,                       

                                                   }, regex=True)
    return data1819

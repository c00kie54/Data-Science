#!/usr/bin/env python
# coding: utf-8

# # Fantasy Football Prediction

# ### By Alex Cooke

# This project aims to predict fantasy football points for players in the Premier League using historical data.
# 
# So far the project has loaded the correct datasets and cleaned the data ready for data exploration. 
# 

# ### Table of Contents
# 
# 
# * [Importing Packages](#chapter1)
# * [Loading Data](#chapter2)
# * [Cleaning data](#chapter3)
#     * [Player 2018/2019 data](#Section_3_1)
#     * [Cleaning JSON 2018/2019 data](Section_3_2)
#     * [Cleaning Player 2018/2019 after merge](#Section_3_3)
#     * [Cleaning Player 2019/2020 data  ](#Section_3_4)
#     * [Clean the 2020/2021 fixtures](#Section_3_5)
#     * [Clean the 2020/2021 matchweek](#Section_3_6)
#     * [Clean the 2020/2021 fantasy player data](#Section_3_7)

# ### Importing Packages  <a class="anchor" id="chapter1"></a>

# This section will contain all of the packages needed for the project

# In[1]:


import pandas as pd
import numpy as np
import datetime


# ### Loading Data  <a class="anchor" id="chapter2"></a>

# This section will load all of the data needed for the projects and will show the main properties of each dataset.

# In[2]:


#Defining a function of reading CSV
def data_read(name): 
    data =pd.read_csv(name)
    print('Data Loaded Sucessfully')
    return data

#Defining a function for reading JSON
def json_load(json_name):
    data = pd.read_json(json_name) #Read JSON
    print('JSON Loaded Sucessfully') 
    m,n = data.shape #Provides two variables of the shape
    if n>m: #IF n>m then data needs to be transposed.
        data = data.T
        return data   
    return data


# In[3]:


player1819 = data_read('/Users/alexcooke/Desktop/Player_Prices/players_1819.csv') # 2018/2019 player data CSV
json1819 = json_load('/Users/alexcooke/Desktop/Player_Prices/fpl_data_2018_2019.json') # 2019/2019 player data JSON
player1920 = data_read('/Users/alexcooke/Desktop/Player_Prices/players_1920_fin.csv') # 2019/2020 player data CSV
fixtures2021 = data_read('/Users/alexcooke/Desktop/Player_Prices/fixtures.csv') # 2020/2021 fixtures CSV
matchweeks2021 = data_read('/Users/alexcooke/Desktop/Player_Prices/Matchweeks.csv') # 2020/2021 matchweeks CSV
GK_data = data_read('/Users/alexcooke/Desktop/Player_Prices/GK-Table 1.csv') # Load goalkeeper players + prices
DF_data = data_read('/Users/alexcooke/Desktop/Player_Prices/DF-Table 1.csv') # Load defender players + prices
MF_data = data_read('/Users/alexcooke/Desktop/Player_Prices/MF-Table 1.csv') # Load midfielders players + prices
FW_data = data_read('/Users/alexcooke/Desktop/Player_Prices/FW-Table 1.csv') # Load forwards players + prices


# Looking at the top rows and the columns of the data to decide how to clean.

# In[4]:


player1819.head(10) 


# In[5]:


player1819.columns


# In[6]:


json1819.head()


# In[7]:


json1819.columns


# In[8]:


player1920.head()


# In[9]:


player1920.columns


# In[10]:


fixtures2021.head()


# In[11]:


matchweeks2021.head()


# In[12]:


GK_data.head()


# In[13]:


DF_data.head()


# In[14]:


MF_data.head()


# In[15]:


FW_data.head()


# ## Cleaning Data  <a class="anchor" id="chapter3"></a>

# ### Player 2018/2019 data   <a class="anchor" id="Section_3_1"></a>
# - The player 2018/2019 has many columns that can be dropped as they are not needed.
# - The data does not contain the players team or position therefore these will be taken from the json1819 file and merged.
# - The player names have a underscores and numbers that need to be removed.
# - Player names with diacritics have a symbol therefore these need to be replaced with the correct name.
# - Players that played 0 minutes can be dropped.

# In[16]:


#Cleaning the 2018/2019 player data

#Dropping the Columns that are not needed.
player1819 = player1819.drop(['attempted_passes',
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
    


player1819['name'] = player1819['name'].astype(str).str[:-3] #Removing the last 3 digits from player name.
player1819 = player1819.replace({'_':' '}, regex=True) #Removing the _ from player name.
player1819 = player1819.replace({'�':'symb'}, regex=True) #Getting rid of the symbol and replace with unique identifier
player1819 = player1819.replace({' ':''}, regex=True) #Removing spaces for ease.
    
## This next bit takes the platers names with symbols in and corrects thier names.
player1819 = player1819.replace({'symbaglar Ssymbysymbncsymb':'CaglarSöyüncü'}, regex=True)
player1819 = player1819.replace({'symblvaroMorata':'ÁlvaroMorata'}, regex=True)
player1819 = player1819.replace({'AdalbertoPesymbaranda':'AdalbertoPeñaranda'}, regex=True)
player1819 = player1819.replace({'AdamaTraorsymb':'AdamaTraoré'}, regex=True)
player1819 = player1819.replace({'AdrisymbnSanMigueldelCastillo':'Adrián'}, regex=True)
player1819 = player1819.replace({'AlexanderSsymbrloth':'AlexanderSørloth'}, regex=True)
player1819 = player1819.replace({'AlexisSsymbnchez':'AlexisSánchez'}, regex=True)
player1819 = player1819.replace({'Andrsymb-FrankZamboAnguissa':'André-FrankZamboAnguissa'}, regex=True)
player1819 = player1819.replace({'AndrsymbFilipeTavaresGomes':'AndréGomes'}, regex=True)
player1819 = player1819.replace({'AndrsymbSchsymbrrle':'AndréSchürrle'}, regex=True)
player1819 = player1819.replace({'AntonioRsymbdiger':'AntonioRüdiger'}, regex=True)
player1819 = player1819.replace({'AyozePsymbrez':'AyozePérez'}, regex=True)
player1819 = player1819.replace({'BernardAnsymbcioCaldeiraDuarte':'Bernard'}, regex=True)
player1819 = player1819.replace({'CsymbdricSoares':'CédricSoares'}, regex=True)
player1819 = player1819.replace({'CsymbsarAzpilicueta':'CésarAzpilicueta'}, regex=True)
player1819 = player1819.replace({'CaglarSsymbysymbncsymb':'CaglarSöyüncü'}, regex=True)
player1819 = player1819.replace({'CarlosSsymbnchez':''}, regex=True)
player1819 = player1819.replace({'CescFsymbbregas':'CescFàbregas'}, regex=True)
player1819 = player1819.replace({'CheikhouKouyatsymb':'CheikhouKouyaté'}, regex=True)
player1819 = player1819.replace({'ChrisLsymbwe':'ChrisLöwe'}, regex=True)
player1819 = player1819.replace({'DavinsonSsymbnchez':'DavinsonSánchez'}, regex=True)
player1819 = player1819.replace({'DavyPrsymbpper':'DavyPröpper'}, regex=True)
player1819 = player1819.replace({'DenisSusymbrez':'DenisSuarez'}, regex=True)
player1819 = player1819.replace({'EmilianoMartsymbnez':'EmilianoMartínez'}, regex=True)
player1819 = player1819.replace({'FabisymbnBalbuena':'FabiánBalbuena'}, regex=True)
player1819 = player1819.replace({'FabianSchsymbr':'FabianSchär'}, regex=True)
player1819 = player1819.replace({'FabricioAgostoRamsymbrez':'Fabricio Agosto'}, regex=True)
player1819 = player1819.replace({'FedericoFernsymbndez':'FedericoFernández'}, regex=True)
player1819 = player1819.replace({'FloydAyitsymb':'FloydAyité'}, regex=True)
player1819 = player1819.replace({'FousseniDiabatsymb':'FousseniDiabaté'}, regex=True)
player1819 = player1819.replace({'FranciscoFemensymbaFar ':'KikoFemenía'}, regex=True)
player1819 = player1819.replace({'GasymbtanBong':'GaëtanBong'}, regex=True)
player1819 = player1819.replace({'Georges-KsymbvinNkoudou':'Georges-KévinNkoudou'}, regex=True)
player1819 = player1819.replace({'GonzaloHiguasymbn':'GonzaloHiguain'}, regex=True)
player1819 = player1819.replace({'HsymbctorBellersymb':'HéctorBellerín'}, regex=True)
player1819 = player1819.replace({'HsymblderCosta':'HélderCosta'}, regex=True)
player1819 = player1819.replace({'HsymbvardNordtveit':'HåvardNordtveit'}, regex=True)
player1819 = player1819.replace({'IbrahimaCisssymb':'IbrahimaCissé'}, regex=True)
player1819 = player1819.replace({'IlkayGsymbndogan':'IlkayGündogan'}, regex=True)
player1819 = player1819.replace({'JsymbrgenLocadia':'JürgenLocadia'}, regex=True)
player1819 = player1819.replace({'JavierHernsymbndezBalcsymbzar':'JavierHernandez'}, regex=True)
player1819 = player1819.replace({'JosymboFilipeIriaSantosMoutinho':'JoãoMoutinho'}, regex=True)
player1819 = player1819.replace({'JonasLsymbssl':'JonasLössl'}, regex=True)
player1819 = player1819.replace({'JossymbDiogoDalotTeixeira':'DiogoDalot'}, regex=True)
player1819 = player1819.replace({'JossymbHeribertoIzquierdoMena':'JoséIzquierdo'}, regex=True)
player1819 = player1819.replace({'JossymbHolebas':'JoséHolebas'}, regex=True)
player1819 = player1819.replace({'JoseLuisMatoSanmartsymbn':'NA'}, regex=True)
player1819 = player1819.replace({'LeroySansymb':'LeroySané'}, regex=True)
player1819 = player1819.replace({'LosymbcDamour':'LoïcDamour'}, regex=True)
player1819 = player1819.replace({'LucasPsymbrez':'LucasPérez'}, regex=True)
player1819 = player1819.replace({'MartsymbnMontoya':'MartínMontoya'}, regex=True)
player1819 = player1819.replace({'Mesutsymbzil':'MesutÖzil'}, regex=True)
player1819 = player1819.replace({'MiguelAlmirsymbn':'MiguelAlmiron'}, regex=True)
player1819 = player1819.replace({'MohamedDiamsymb':'MohamedDiamé'}, regex=True)
player1819 = player1819.replace({'MousaDembsymblsymb':'MousaDembélé'}, regex=True)
player1819 = player1819.replace({'N\'GoloKantsymb':'N\'GoloKanté'}, regex=True)
player1819 = player1819.replace({'NathanAksymb':'NathanAké'}, regex=True)
player1819 = player1819.replace({'NicolsymbsOtamendi':'NicolásOtamendi'}, regex=True)
player1819 = player1819.replace({'PapeSouarsymb':'PapeSouaré'}, regex=True)
player1819 = player1819.replace({'PascalGrosymb':'PascalGroß'}, regex=True)
player1819 = player1819.replace({'PedroRodrsymbguezLedesma':'Pedro'}, regex=True)
player1819 = player1819.replace({'Pierre-EmileHsymbjbjerg':'Pierre-EmileHøjbjerg'}, regex=True)
player1819 = player1819.replace({'RsymbbenDiogodaSilvaNeves':'RúbenNeves'}, regex=True)
player1819 = player1819.replace({'RsymbbenGonsymbaloSilvaNascimentoVinagre ':'RúbenVinagre'}, regex=True)
player1819 = player1819.replace({'RasymblJimsymbnez':'RaúlJiménez'}, regex=True)
player1819 = player1819.replace({'RoderickJeffersonGonsymbalvesMiranda':'RoderickMiranda'}, regex=True)
player1819 = player1819.replace({'RomainSasymbss':'RomainSaïss'}, regex=True)
player1819 = player1819.replace({'RuiPedrodosSantosPatrsymbcio':'RuiPatrício'}, regex=True)
player1819 = player1819.replace({'SadioMansymb':'SadioMané'}, regex=True)
player1819 = player1819.replace({'SalomsymbnRondsymbn':'SalomónRondón'}, regex=True)
player1819 = player1819.replace({'SandroRamsymbrez':'SandroRamírez'}, regex=True)
player1819 = player1819.replace({'SebastianPrsymbdl':'SebastianPrödl'}, regex=True)
player1819 = player1819.replace({'SergioAgsymbero':'SergioAgüero'}, regex=True)
player1819 = player1819.replace({'TiemousymbBakayoko':'TiemouéBakayoko'}, regex=True)
player1819 = player1819.replace({'symbctorCamarasa':'VíctorCamarasa'}, regex=True)
player1819 = player1819.replace({'VictorLindelsymbf':'VictorLindelöf'}, regex=True)
player1819 = player1819.replace({'symbaglarSsymbysymbncsymb':'CaglarSöyüncü'}, regex=True)
player1819 = player1819.replace({'AlissonRamsesBecker':'Alisson'}, regex=True)
player1819 = player1819.replace({'BamideleAlli':'DeleAlli'}, regex=True)
player1819 = player1819.replace({'BenjaminChilwell':'BenChilwell'}, regex=True)
player1819 = player1819.replace({'BernardoFernandesdaSilvaJunior':'Bernardo'}, regex=True)
player1819 = player1819.replace({'BernardoMotaVeigadeCarvalhoeSilva':'BernardoSilva'}, regex=True)
player1819 = player1819.replace({'BerndLen':'BerndLeno'}, regex=True)
player1819 = player1819.replace({'BrunoSaltorGrau':'Bruno'}, regex=True)
player1819 = player1819.replace({'CalumChamber':'CalumChambers'}, regex=True)
player1819 = player1819.replace({'DaniloLuizdaSilva':'Danilo'}, regex=True)
player1819 = player1819.replace({'DavidLuizMoreiraMarinho':'DavidLuiz'}, regex=True)
player1819 = player1819.replace({'EdersonSantanadeMoraes':'Ederson'}, regex=True)
player1819 = player1819.replace({'EmersonPalmieridosSantos':'Emerson'}, regex=True)
player1819 = player1819.replace({'FabioHenriqueTavares':'Fabinho'}, regex=True)
player1819 = player1819.replace({'FelipeAndersonPereiraGomes':'FelipeAnderson'}, regex=True)
player1819 = player1819.replace({'FernandoLuizRosa':'Fernandinho'}, regex=True)
player1819 = player1819.replace({'FranciscoFemensymbaFar':'KikoFemenía'}, regex=True)
player1819 = player1819.replace({'FredericoRodriguesdePaulaSantos':'Fred'}, regex=True)
player1819 = player1819.replace({'GabrielFernandodeJesus':'GabrielJesus'}, regex=True)
player1819 = player1819.replace({'Heung-MinSon':'SonHeung-Min'}, regex=True)
player1819 = player1819.replace({'IsaacSuccessAjayi':'IsaacSuccess'}, regex=True)
player1819 = player1819.replace({'JonathanCastroOtto':'Jonny'}, regex=True)
player1819 = player1819.replace({'JorgeLuizFrelloFilho':'Jorginho'}, regex=True)
player1819 = player1819.replace({'LaurentKoscieln':'LaurentKoscielny'}, regex=True)
player1819 = player1819.replace({'LucasRodriguesMouradaSilva':'LucasMoura'}, regex=True)
player1819 = player1819.replace({'MathewRyan':'MatRyan'}, regex=True)
player1819 = player1819.replace({'NachoMonrea':'NachoMonreal'}, regex=True)
player1819 = player1819.replace({'PetrCec':'PetrCech'}, regex=True)
player1819 = player1819.replace({'RsymbbenGonsymbaloSilvaNascimentoVinagre':'RúbenVinagre'}, regex=True)
player1819 = player1819.replace({'RicardoDomingosBarbosaPereira':'RicardoPereira'}, regex=True)
player1819 = player1819.replace({'RicharlisondeAndrade':'Richarlison'}, regex=True)
player1819 = player1819.replace({'RobHoldin':'RobHolding'}, regex=True)
player1819 = player1819.replace({'SeadKolasina':'SeadKolasinac'}, regex=True)
player1819 = player1819.replace({'ShkodranMustaf':'ShkodranMustafi'}, regex=True)
player1819 = player1819.replace({'SokratisPapastathopoulos':'Sokratis'}, regex=True)
player1819 = player1819.replace({'SolomonMarch':'SollyMarch'}, regex=True)
player1819 = player1819.replace({'Sung-yuengKi':'KiSung-yueng'}, regex=True)
player1819 = player1819.replace({'VVíctorCamarasa':'VíctorCamarasa'}, regex=True)
player1819 = player1819.replace({'WillianBorgesDaSilva':'Willian'}, regex=True)
player1819 = player1819.replace({'AbdoulayeDoucoursymb':'AbdoulayeDoucouré'}, regex=True)


## Removing Players that played 0 minutes
player1819 = player1819[player1819.minutes != 0]
print('Players 2018/2019 cleaned')


# In[17]:


player1819.head()


# ### Cleaning JSON 2018/2019 data   <a class="anchor" id="Section_3_2"></a>
# - Drop all columns except name, Club and position
# - Merge with Player 2018/2019 data

# In[18]:


# Cleaning the 2018/2019 JSON data
json1819.drop(json1819.columns.difference(['Club','Position']), 1, inplace=True) # Keep only these columns
json1819 =json1819.reset_index() #Reset index
json1819.columns = ['name', 'Club','Position'] # Rename columns
json1819 =json1819.sort_values(by=['name']) # Sort by name
json1819 = json1819.replace({' ':''}, regex=True) # Get rid of spaces
print('JSON data cleaned')
player1819 = player1819.merge(json1819, how='left')
print('JSON merged with player1819')


# In[19]:


player1819.head()


# ### Cleaning Player 2018/2019 after merge   <a class="anchor" id="Section_3_3"></a>
# - Drop all columns except name, Club and position
# - Merge with Player 2018/2019 data
# - Some Clubs and positions are missing
# - Empty rows will be dropped 
# - Opponent team column in number format should be changed to team name

# In[20]:


# Cleaning the 2018/2019 player data after CSV and JSON merge

# Sort by name
player1819 =player1819.sort_values(by=['name'])

# Fixing missing data
player1819.loc[player1819["name"]=="AaronRowe", "Club"] = 'HuddersfieldTown'
player1819.loc[player1819["name"]=="AaronRowe", "Position"] = 'Midfielder'
player1819.loc[player1819["name"]=="Abd-Al-AliMorakinyoOlaposiKoiki", "Club"] = 'Burnley'
player1819.loc[player1819["name"]=="Abd-Al-AliMorakinyoOlaposiKoiki", "Position"] = 'Defender'
player1819.loc[player1819["name"]=="AdamaTraoré", "Club"] = 'WolverhamptonWanderers'
player1819.loc[player1819["name"]=="AdamaTraoré", "Position"] = 'Midfielder'
player1819.loc[player1819["name"]=="AlexMcCarthy", "Club"] = 'Southampton'
player1819.loc[player1819["name"]=="", "Position"] = 'Goalkeeper'
player1819.loc[player1819["name"]=="BenDavies", "Club"] = 'TottenhamHotspur'
player1819.loc[player1819["name"]=="", "Position"] = 'Defender'
player1819.loc[player1819["name"]=="BonatiniLohnerMaiaBonatini", "Club"] = 'WolverhamptonWanderers'
player1819.loc[player1819["name"]=="BonatiniLohnerMaiaBonatini", "Position"] = 'Forward'
player1819.loc[player1819["name"]=="CharlieTaylor", "Club"] = 'Burnley'
player1819.loc[player1819["name"]=="CharlieTaylor", "Position"] = 'Defender'
player1819.loc[player1819["name"]=="DavinsonSánchez", "Club"] = 'TottenhamHotspur'
player1819.loc[player1819["name"]=="DavinsonSánchez", "Position"] = 'Defender'
player1819.loc[player1819["name"]=="GonzaloHiguain", "Club"] = 'Chelsea'
player1819.loc[player1819["name"]=="GonzaloHiguain", "Position"] = 'Forward'
player1819.loc[player1819["name"]=="HarveyBarnes", "Club"] = 'LeicesterCity'
player1819.loc[player1819["name"]=="HarveyBarnes", "Position"] = 'Midfielder'
player1819.loc[player1819["name"]=="JackStephens", "Club"] = 'Southampton'
player1819.loc[player1819["name"]=="JackStephens", "Position"] = 'Defender'
player1819.loc[player1819["name"]=="JoelWard", "Club"] = 'CrystalPalace'
player1819.loc[player1819["name"]=="JoelWard", "Position"] = 'Defender'
player1819.loc[player1819["name"]=="KayneRamsay", "Club"] = 'Southampton'
player1819.loc[player1819["name"]=="KayneRamsay", "Position"] = 'Defender'
player1819.loc[player1819["name"]=="MasonGreenwood", "Club"] = 'ManchesterUnited'
player1819.loc[player1819["name"]=="MasonGreenwood", "Position"] = 'Forward'
player1819.loc[player1819["name"]=="MichaelObafemi", "Club"] = 'Southampton'
player1819.loc[player1819["name"]=="MichaelObafemi", "Position"] = 'Forward'
player1819.loc[player1819["name"]=="MiguelAlmiron", "Club"] = 'NewcastleUnited'
player1819.loc[player1819["name"]=="MiguelAlmiron", "Position"] = 'Forward'
player1819.loc[player1819["name"]=="PhilJones", "Club"] = 'ManchesterUnited'
player1819.loc[player1819["name"]=="PhilJones", "Position"] = 'Defender'
player1819.loc[player1819["name"]=="RaheemSterling", "Club"] = 'ManchesterCity'
player1819.loc[player1819["name"]=="RaheemSterling", "Position"] = 'Forward'
player1819.loc[player1819["name"]=="ShaneLong", "Club"] = 'Southampton'
player1819.loc[player1819["name"]=="ShaneLong", "Position"] = 'Forward'
player1819.loc[player1819["name"]=="StuartArmstrong", "Club"] = 'Southampton'
player1819.loc[player1819["name"]=="StuartArmstrong", "Position"] = 'Midfielder'
player1819.loc[player1819["name"]=="YouriTielemans", "Club"] = 'LeicesterCity'
player1819.loc[player1819["name"]=="YouriTielemans", "Position"] = 'Midfielder'

## Dropping missing rows
player1819 = player1819.dropna()

## Changing away team from number to team name
player1819['opponent_team'] = player1819['opponent_team'].astype(str) 
player1819['opponent_team'] = player1819.opponent_team.replace({'20':'WolverhamptonWanderers',
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


# In[21]:


player1819.head()


# ### Cleaning Player 2019/2020 data   <a class="anchor" id="Section_3_4"></a>
#  - Drop columns that are not useful (should end up with the same as the 2018/2019 data).
#  - Player names with diacritics have a symbol therefore these need to be replaced with the correct name.
#  - Drop players that played 0 minutes.
#  - Rename full to name and team to Club  

# In[22]:


## Cleaning the 2019/2020 player data

#Dropping columns
player1920 = player1920.drop(['Unnamed: 0',
                            'fixture',
                          'ict_index',
                          'kickoff_time',
                          'selected',
                          'ppm',
                            'bps',
                            'element',
                            'transfers_in',
                            'transfers_out',
                            'value',
                            'transfers_balance'
                            
                           ], axis=1)
# Setting ? to unique identifier
player1920 = player1920.replace({'\?':'1104'}, regex=True)
# Removing spaces
player1920 = player1920.replace({' ':''}, regex=True)
# Replacing player names
player1920 = player1920.replace({'1104aglarS1104y1104nc1104':'CaglarSöyüncü'}, regex=True)
player1920 = player1920.replace({'1104lvaroMorata':'ÁlvaroMorata'}, regex=True)
player1920 = player1920.replace({'AdalbertoPe1104aranda':'AdalbertoPeñaranda'}, regex=True)
player1920 = player1920.replace({'AdamaTraor1104':'AdamaTraoré'}, regex=True)
player1920 = player1920.replace({'Adri1104nSanMigueldelCastillo':'Adrián'}, regex=True)
player1920 = player1920.replace({'AlexanderS1104rloth':'AlexanderSørloth'}, regex=True)
player1920 = player1920.replace({'AlexisS1104nchez':'AlexisSánchez'}, regex=True)
player1920 = player1920.replace({'Andr1104-FrankZamboAnguissa':'André-FrankZamboAnguissa'}, regex=True)
player1920 = player1920.replace({'Andr1104FilipeTavaresGomes':'AndréGomes'}, regex=True)
player1920 = player1920.replace({'Andr1104Sch1104rrle':'AndréSchürrle'}, regex=True)
player1920 = player1920.replace({'AntonioR1104diger':'AntonioRüdiger'}, regex=True)
player1920 = player1920.replace({'AyozeP1104rez':'AyozePérez'}, regex=True)
player1920 = player1920.replace({'BernardAn1104cioCaldeiraDuarte':'Bernard'}, regex=True)
player1920 = player1920.replace({'C1104dricSoares':'CédricSoares'}, regex=True)
player1920 = player1920.replace({'C1104sarAzpilicueta':'CésarAzpilicueta'}, regex=True)
player1920 = player1920.replace({'CaglarS1104y1104nc1104':'CaglarSöyüncü'}, regex=True)
player1920 = player1920.replace({'CarlosS1104nchez':''}, regex=True)
player1920 = player1920.replace({'CescF1104bregas':'CescFàbregas'}, regex=True)
player1920 = player1920.replace({'CheikhouKouyat1104':'CheikhouKouyaté'}, regex=True)
player1920 = player1920.replace({'ChrisL1104we':'ChrisLöwe'}, regex=True)
player1920 = player1920.replace({'DavinsonS1104nchez':'DavinsonSánchez'}, regex=True)
player1920 = player1920.replace({'DavyPr1104pper':'DavyPröpper'}, regex=True)
player1920 = player1920.replace({'DenisSu1104rez':'DenisSuarez'}, regex=True)
player1920 = player1920.replace({'EmilianoMart1104nez':'EmilianoMartínez'}, regex=True)
player1920 = player1920.replace({'Fabi1104nBalbuena':'FabiánBalbuena'}, regex=True)
player1920 = player1920.replace({'FabianSch1104r':'FabianSchär'}, regex=True)
player1920 = player1920.replace({'FabricioAgostoRam1104rez':'Fabricio Agosto'}, regex=True)
player1920 = player1920.replace({'FedericoFern1104ndez':'FedericoFernández'}, regex=True)
player1920 = player1920.replace({'FloydAyit1104':'FloydAyité'}, regex=True)
player1920 = player1920.replace({'FousseniDiabat1104':'FousseniDiabaté'}, regex=True)
player1920 = player1920.replace({'FranciscoFemen1104aFar ':'KikoFemenía'}, regex=True)
player1920 = player1920.replace({'Ga1104tanBong':'GaëtanBong'}, regex=True)
player1920 = player1920.replace({'Georges-K1104vinNkoudou':'Georges-KévinNkoudou'}, regex=True)
player1920 = player1920.replace({'GonzaloHigua1104n':'GonzaloHiguain'}, regex=True)
player1920 = player1920.replace({'H1104ctorBeller1104':'HéctorBellerín'}, regex=True)
player1920 = player1920.replace({'H1104lderCosta':'HélderCosta'}, regex=True)
player1920 = player1920.replace({'H1104vardNordtveit':'HåvardNordtveit'}, regex=True)
player1920 = player1920.replace({'IbrahimaCiss1104':'IbrahimaCissé'}, regex=True)
player1920 = player1920.replace({'IlkayG1104ndogan':'IlkayGündogan'}, regex=True)
player1920 = player1920.replace({'J1104rgenLocadia':'JürgenLocadia'}, regex=True)
player1920 = player1920.replace({'JavierHern1104ndezBalc1104zar':'JavierHernandez'}, regex=True)
player1920 = player1920.replace({'Jo1104oFilipeIriaSantosMoutinho':'JoãoMoutinho'}, regex=True)
player1920 = player1920.replace({'JonasL1104ssl':'JonasLössl'}, regex=True)
player1920 = player1920.replace({'Jos1104DiogoDalotTeixeira':'DiogoDalot'}, regex=True)
player1920 = player1920.replace({'Jos1104HeribertoIzquierdoMena':'JoséIzquierdo'}, regex=True)
player1920 = player1920.replace({'Jos1104Holebas':'JoséHolebas'}, regex=True)
player1920 = player1920.replace({'JoseLuisMatoSanmart1104n':'NA'}, regex=True)
player1920 = player1920.replace({'LeroySan1104':'LeroySané'}, regex=True)
player1920 = player1920.replace({'Lo1104cDamour':'LoïcDamour'}, regex=True)
player1920 = player1920.replace({'LucasP1104rez':'LucasPérez'}, regex=True)
player1920 = player1920.replace({'Mart1104nMontoya':'MartínMontoya'}, regex=True)
player1920 = player1920.replace({'Mesut1104zil':'MesutÖzil'}, regex=True)
player1920 = player1920.replace({'MiguelAlmir1104n':'MiguelAlmiron'}, regex=True)
player1920 = player1920.replace({'MohamedDiam1104':'MohamedDiamé'}, regex=True)
player1920 = player1920.replace({'MousaDemb1104l1104':'MousaDembélé'}, regex=True)
player1920 = player1920.replace({'N\'GoloKant1104':'N\'GoloKanté'}, regex=True)
player1920 = player1920.replace({'NathanAk1104':'NathanAké'}, regex=True)
player1920 = player1920.replace({'Nicol1104sOtamendi':'NicolásOtamendi'}, regex=True)
player1920 = player1920.replace({'PapeSouar1104':'PapeSouaré'}, regex=True)
player1920 = player1920.replace({'PascalGro1104':'PascalGroß'}, regex=True)
player1920 = player1920.replace({'PedroRodr1104guezLedesma':'Pedro'}, regex=True)
player1920 = player1920.replace({'Pierre-EmileH1104jbjerg':'Pierre-EmileHøjbjerg'}, regex=True)
player1920 = player1920.replace({'R1104benDiogodaSilvaNeves':'RúbenNeves'}, regex=True)
player1920 = player1920.replace({'R1104benGon1104aloSilvaNascimentoVinagre ':'RúbenVinagre'}, regex=True)
player1920 = player1920.replace({'Ra1104lJim1104nez':'RaúlJiménez'}, regex=True)
player1920 = player1920.replace({'RoderickJeffersonGon1104alvesMiranda':'RoderickMiranda'}, regex=True)
player1920 = player1920.replace({'RomainSa1104ss':'RomainSaïss'}, regex=True)
player1920 = player1920.replace({'RuiPedrodosSantosPatr1104cio':'RuiPatrício'}, regex=True)
player1920 = player1920.replace({'SadioMan1104':'SadioMané'}, regex=True)
player1920 = player1920.replace({'Salom1104nRond1104n':'SalomónRondón'}, regex=True)
player1920 = player1920.replace({'SandroRam1104rez':'SandroRamírez'}, regex=True)
player1920 = player1920.replace({'SebastianPr1104dl':'SebastianPrödl'}, regex=True)
player1920 = player1920.replace({'SergioAg1104ero':'SergioAgüero'}, regex=True)
player1920 = player1920.replace({'Tiemou1104Bakayoko':'TiemouéBakayoko'}, regex=True)
player1920 = player1920.replace({'1104ctorCamarasa':'VíctorCamarasa'}, regex=True)
player1920 = player1920.replace({'VictorLindel1104f':'VictorLindelöf'}, regex=True)
player1920 = player1920.replace({'1104aglarS1104y1104nc1104':'CaglarSöyüncü'}, regex=True)
player1920 = player1920.replace({'AlissonRamsesBecker':'Alisson'}, regex=True)
player1920 = player1920.replace({'BamideleAlli':'DeleAlli'}, regex=True)
player1920 = player1920.replace({'BenjaminChilwell':'BenChilwell'}, regex=True)
player1920 = player1920.replace({'BernardoFernandesdaSilvaJunior':'Bernardo'}, regex=True)
player1920 = player1920.replace({'BernardoMotaVeigadeCarvalhoeSilva':'BernardoSilva'}, regex=True)
player1920 = player1920.replace({'BerndLen':'BerndLeno'}, regex=True)
player1920 = player1920.replace({'BrunoSaltorGrau':'Bruno'}, regex=True)
player1920 = player1920.replace({'CalumChamber':'CalumChambers'}, regex=True)
player1920 = player1920.replace({'DaniloLuizdaSilva':'Danilo'}, regex=True)
player1920 = player1920.replace({'DavidLuizMoreiraMarinho':'DavidLuiz'}, regex=True)
player1920 = player1920.replace({'EdersonSantanadeMoraes':'Ederson'}, regex=True)
player1920 = player1920.replace({'EmersonPalmieridosSantos':'Emerson'}, regex=True)
player1920 = player1920.replace({'FabioHenriqueTavares':'Fabinho'}, regex=True)
player1920 = player1920.replace({'FelipeAndersonPereiraGomes':'FelipeAnderson'}, regex=True)
player1920 = player1920.replace({'FernandoLuizRosa':'Fernandinho'}, regex=True)
player1920 = player1920.replace({'FranciscoFemen1104aFar':'KikoFemenía'}, regex=True)
player1920 = player1920.replace({'FredericoRodriguesdePaulaSantos':'Fred'}, regex=True)
player1920 = player1920.replace({'GabrielFernandodeJesus':'GabrielJesus'}, regex=True)
player1920 = player1920.replace({'Heung-MinSon':'SonHeung-Min'}, regex=True)
player1920 = player1920.replace({'IsaacSuccessAjayi':'IsaacSuccess'}, regex=True)
player1920 = player1920.replace({'JonathanCastroOtto':'Jonny'}, regex=True)
player1920 = player1920.replace({'JorgeLuizFrelloFilho':'Jorginho'}, regex=True)
player1920 = player1920.replace({'LaurentKoscieln':'LaurentKoscielny'}, regex=True)
player1920 = player1920.replace({'LucasRodriguesMouradaSilva':'LucasMoura'}, regex=True)
player1920 = player1920.replace({'MathewRyan':'MatRyan'}, regex=True)
player1920 = player1920.replace({'NachoMonrea':'NachoMonreal'}, regex=True)
player1920 = player1920.replace({'PetrCec':'PetrCech'}, regex=True)
player1920 = player1920.replace({'R1104benGon1104aloSilvaNascimentoVinagre':'RúbenVinagre'}, regex=True)
player1920 = player1920.replace({'RicardoDomingosBarbosaPereira':'RicardoPereira'}, regex=True)
player1920 = player1920.replace({'RicharlisondeAndrade':'Richarlison'}, regex=True)
player1920 = player1920.replace({'RobHoldin':'RobHolding'}, regex=True)
player1920 = player1920.replace({'SeadKolasina':'SeadKolasinac'}, regex=True)
player1920 = player1920.replace({'ShkodranMustaf':'ShkodranMustafi'}, regex=True)
player1920 = player1920.replace({'SokratisPapastathopoulos':'Sokratis'}, regex=True)
player1920 = player1920.replace({'SolomonMarch':'SollyMarch'}, regex=True)
player1920 = player1920.replace({'Sung-yuengKi':'KiSung-yueng'}, regex=True)
player1920 = player1920.replace({'VVíctorCamarasa':'VíctorCamarasa'}, regex=True)
player1920 = player1920.replace({'WillianBorgesDaSilva':'Willian'}, regex=True)
player1920 = player1920.replace({'1104rjanNyland':'OrjanNyland'}, regex=True)
player1920 = player1920.replace({'AbdoulayeDoucour1104':'AbdoulayeDoucoure'}, regex=True)
player1920 = player1920.replace({'BorjaGonz1104lezTom1104s':'BorjaBastón'}, regex=True)
player1920 = player1920.replace({'BrunoAndr1104CavacoJordao':'BrunoJordão'}, regex=True)
player1920 = player1920.replace({'DanielCeballosFern1104ndez':'DaniCeballos'}, regex=True)
player1920 = player1920.replace({'DjibrilSidib1104':'DjibrilSidibe'}, regex=True)
player1920 = player1920.replace({'EmilianoBuend1104a':'EmilianoBuendia'}, regex=True)
player1920 = player1920.replace({'Fr1104d1104ricGuilbert':'FredericGuilbert'}, regex=True)
player1920 = player1920.replace({'Jes1104sVallejoL1104zaro':'JesúsVallejo'}, regex=True)
player1920 = player1920.replace({'Jo1104oPedroCavacoCancelo':'JoãoCancelo'}, regex=True)
player1920 = player1920.replace({'Jo1104oPedroJunqueiradeJesus':'JoãoPedro'}, regex=True)
player1920 = player1920.replace({'JoelintonC1104ssioApolin1104riodeLira':'Joelinton'}, regex=True)
player1920 = player1920.replace({'Jos11041104ngelEsmor1104sTasende':'Angeliño'}, regex=True)
player1920 = player1920.replace({'Jos1104IgnacioPeleteiroRomallo':'Jota'}, regex=True)
player1920 = player1920.replace({'Jos1104Reina':'PepeReina'}, regex=True)
player1920 = player1920.replace({'MuhamedBe1104i1104':'MuhamedBešić'}, regex=True)
player1920 = player1920.replace({'NicolasP1104p1104':'NicolasPepe'}, regex=True)
player1920 = player1920.replace({'OnelHern1104ndez':'Onel Hernández'}, regex=True)
player1920 = player1920.replace({'PabloMar1104':'Pablo Marí'}, regex=True)
player1920 = player1920.replace({'S1104bastienHaller':'SebastienHaller'}, regex=True)
player1920 = player1920.replace({'Isma1104laSarr':'IsmaïlaSarr'}, regex=True)
# Removing playes that played 0 mins
player1920 = player1920[player1920.minutes != 0]
#Renaming columns
player1920 = player1920.rename(columns={'full': 'name', 'team': 'Club'})


# In[23]:


player1920.head()


# ### Clean the 2020/2021 fixtures  <a class="anchor" id="Section_3_5"></a>
# - Set the game date to datetime
# - Create blank Matchweek column

# In[24]:


fixtures2021['game_date']= pd.to_datetime(fixtures2021['game_date']) 
fixtures2021['Matchweek']=''


#  ### Clean the 2020/2021 matchweek  <a class="anchor" id="Section_3_6"></a>
# - Convert months from strings to numbers
# - Create year column
# - Create match week start and end dates
# - Set correct year for 2021 dates
# - Merge with fixtures

# In[25]:


## Cleaning 2020/2021 matchweek

# Removing colons
matchweeks2021 = matchweeks2021.replace({':':''}, regex=True)

# Replacing month with number
look_up = {'January':'01','February' :'02', 'March' :'03', 'April' :'04', 'May' :'05',
            'June':'06', 'July' :'07',  'August':'08',  'September':'09','October':'10', 'November':'11', 'December':'12'}
matchweeks2021['Start_Month'] = matchweeks2021['Start_Month'].apply(lambda x: look_up[x])
matchweeks2021['End_Month'] = matchweeks2021['End_Month'].apply(lambda x: look_up[x])
# Create year column and set to 2020
matchweeks2021['Year']='2020'

#Creating matchweek start and end dates
temp1 = matchweeks2021[["Year", "Start_Month", "Start_Date"]].copy()
temp1.columns = ["year", "month", "day"]
temp2 = matchweeks2021[["Year", "End_Month", "End_Date"]].copy()
temp2.columns = ["year", "month", "day"]
matchweeks2021["Start"] = pd.to_datetime(temp1)
matchweeks2021["End"] = pd.to_datetime(temp2)
matchweeks2021 = matchweeks2021.drop(['Day','Start_Date','Start_Month','End_Date','End_Month','Year'], axis=1)

# Set year 2021 for dates jan 01 and after
matchweeks2021.End[15:] = matchweeks2021.End[15:] + pd.offsets.DateOffset(years=1)
matchweeks2021.Start[16:] = matchweeks2021.Start[16:] + pd.offsets.DateOffset(years=1)
print('Matchweeks 2019/2020 cleaned')


# In[26]:


## Merging matchweeks with fixtures
for i in range(39):
    for g in range(380):
        if fixtures2021.game_date[g]>= matchweeks2021.Start[i] and fixtures2021.game_date[g]<= matchweeks2021.End[i]:
            fixtures2021.Matchweek[g] = matchweeks2021.Matchweek[i]
       


# In[27]:


fixtures2021.head()


#  ### Clean the 2020/2021 fantasy player data  <a class="anchor" id="Section_3_7"></a>
# - Remove unnamed column form FW_data

# In[28]:


FW_data = FW_data.drop(['Unnamed: 4'],axis=1)


# In[29]:


FW_data.head()


# 

# In[ ]:





# In[ ]:





# This script will clean the players 2019/2020 data

def player1920_clean(player1920):
    player1920 = player1920.drop(['Unnamed: 0',
                            'fixture',
                          'ict_index',
                          'kickoff_time',
                          'round',
                          'selected',
                          'ppm',
                            'bps',
                            'element',
                            'transfers_in',
                            'transfers_out',
                            'value',
                            'transfers_balance'
                            
                           ], axis=1)

    player1920 = player1920.replace({'\?':'1104'}, regex=True)
    player1920 = player1920.replace({' ':''}, regex=True)
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
    player1920 = player1920[player1920.minutes != 0]
    player1920 = player1920.rename(columns={'full': 'name', 'team': 'Club'})
    print('Player 1920 cleaned')
    return player1920




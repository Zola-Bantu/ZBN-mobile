"""December 21st 2012 is the code - In the ethiopic calendar this date
corresponds to August 27 2020 in the gregorian calendar"""

import datetime

syncd = datetime.date(2020, 8, 27) # 21, 12, 2012
nytt = datetime.date(2020, 9, 11) # 1, 1, 2013
"""
365 days in a year, 12 months of 30 days, 1 month of 5 days
                                              -------------------
-------------                         pheleu  |Hapi-meshta
            |month 1 : Ausir, Aries, The Ram -|Ba, Auset
            |   The pioneer and trailblazer   |sa-Heru, Auset
            |        Lwetse - Lwetse          -------------------
            |                              poho     |Auset, sa-Heru
            |month 2 : Het-heru, Taurus, The Bull - |Nebt-hut, sa-Heru
   Selemo   |     The persistent provider           |Hapi-mesta, Tuamutef
            |        Mphalane - Diphalane          ---------------------
            |                           mafahla    |Qebesenef, Tuamutef
            |month 3 : Tehuti, Gemini, The Twins - |Tuamutef
            |      The versatile and vibrant       |Tuamutef, Qebesenef, Hapi
-------------       Pudungwana - Ngwanatsele       ----------------------
            |                             sekala     |Tuamutef, Hapi
            |month 4 : Nebt-hut, Libra, The Scales - |Heru
            |        The balanced beautifier         |Set
            |        Tshitwe - Sedimonthole          ---------------------
            |                           phepeng      |Heru
 lehlabula  |month 5 : Heru, Scorpio, The Scorpion - |Auset, Nebt-hut
            |        The intense and focused         |Set
            |        Pherekgong - Firikgong          ---------------------
            |                         seqha le motsu  |Heru
            |month 6 : Geb, Sagittarius, The Archer - |sa-Heru, Hapi
            |        The worldly adventurer           |Heru
-------------          Hlakola - Tlhakole        ------------------------
            |                          kankrap   |Hapi
            |month 7 : Auset, Cancer, The Crab - |Auset
            |       The natural nurturer         |Tuamutef, Qebesenef
            |       Hlakubele - Mopitlwe     ------------------------
            |                       tau      |Qebesenef
  lehwetla  |month 8 : Anpu, Leo, The Lion - |Nebt-hut
            |        The regal ruler         |Qebesenef, Tuamutef
            |        Mmesa - Moranang        -------------------
            |                         morwetsana   |Hapi-mesta, Hapi
            |month 9 : Sekmet, Virgo, The Virgin - |Heru
            |        The masterful helper          |Heru
-------------      Motsheanong - Motsheganong      ---------------------
            |                             podi     |Heru
            |month 10 : Set, Capricorn, The Goat - |Set
            |     The measured master planner      |sa-Heru, Hapi
            |        Phupjane - Seetebosigo        ---------------------
            |                           motlisi wa metsi   |Hapi
   mariha   |month 11: Ma'at, Aquarius, The Water Bearer - |Hapi-mesta
            |     The mad scientist and humanitarian       |Tuamutef, Qebesenef
            |          Phupu - Phukwi           ---------------------------
            |                         tlhapi    |Ma'at, Heru
            |month 12 : Nut, Pisces, The Fish - |Ma'at, Heru
            |      The dreamer and healer       |Ma'at, Heru
-------------         Phato - Phatwe            --------------------------------
             month 13 : Nut          -          |Ma'at, Heru, Auset
                                                ----------------------

this syncronisity it falls on day 351 of our calendar
this means the 1st of the new year is on the 11th September 2020

Ausir - bonna
Nebt-hut - Pono
"""
# moon cycle 29.5 days

dikgwedi1 = {
    1: ("Ausir",
        "mmoetepele o sebete, malekele o sa tsabe tswelopele.",
        ["lema boitsebo", "lema", "tswara lefu", "kgopola batho ba feteleng",
         "tsoso dinhla tse o di emisetse"],
        ["Lwetse - Lwetse", "pheleu", "selemo", "asir.png"]),
    2: ("Hut-heru",
        "moboloki o motsitsitse.",
        ["bino, ho jeka le ho thaba", "rata", "nyala",
         "keteka bontle, bomme, bosadi le bofumahadi",
         "hlahloba lehodimo"],
        ["Mphalane - Diphalane", "poho", "selemo", "../didiriso/rn_kmt/O10.png"]),
    3: ("Djehuti",
        "kgwaba la methali yohle e mofolofolo.",
        ["ithuta", "ngola", "tshwantsha", "kgabisa", "nqosa dinyewe"],
        ["Pudungwana - Ngwanatsele", "mafahla", "selemo", "../didiriso/rn_kmt/C3.png"]),
    4: ("Nebt-hut",
        "mointlafatsi o lekansang.",
        ["llela batho ba feteleng", "keteka bosiu le bontsho",
         "rutisa", "tswala", "tshireletsa", "hlweka mmele le moya",
         "boloko bafu", "nwa jwala"],
        ["Tshitwe - Sedimonthole", "sekala", "lehlabula", "../didiriso/rn_kmt/O9.png"]),
    5: ("Heru",
        "moetepele o bohale le o mofolofolo",
        ["etapele", "nahana ka bokamoso", "hlahloba lehodimo"],
        ["Pherekgong - Firikgong", "phepeng", "lehlabula", "../didiriso/rn_kmt/G5.png"]),
    6: ("Geb",
        "malekele wa lefatse.",
        ["hlokomela lefatshe","hlokomela dijalo",
         "thusa batho ba amuwa ke dikodua tsa hlaho", "tsosa matla a kahare"],
        ["Hlakola - Tlhakole", "seqha le motsu", "lehlabula", "../didiriso/rn_kmt/G39.png"]),
    7: ("Auset",
        "mohlokomedi ka thlaho.",
        ["nyala", "llela bafu","keteka bomme", "keteka borena",
         "tshireletsa setjhaba", "ithuta", "hlahloba lehodimo"],
        ["Hlakubele - Mopitlwe", "kankrap", "lehwtla", "ast.png"]),
    8: ("Anpu",
        "morena o tswanetseng.",
        ["tswara lefu", "kgopola batho ba feteleng",
         "kgabisa mabitla", "fa dineo ho batho ba feteleng"],
        ["Mmesa - Moranang", "tau", "lehwtla", "../didiriso/rn_kmt/C6.png"]),
    9: ("Sekmet",
        "mothusi o molimo.",
        ["lwa ntwa", "fodisa", "tshireletsa ya barena"],
        ["Motsheanong - Motsheganong", "morwetsana", "lehwtla", "skmt.png"]),
    10: ("Set",
         "morena wa leqheka.",
         ["hlophela bokamoso", "ela hloko dibe tse etsuwang", "bula dinyewe"],
         ["Phupjane - Seetebosigo", "podi", "mariha", "../didiriso/rn_kmt/C7.png"]),
    11: ("Ma'at",
         "tsebanyane e kgolo ka pelo e ntle.",
         ["pahamisa nnete le toka", "ithuta", "hlahloba dinaledi",
          "pahamisa boitshwaro sinhle", "matlafatsa dikgokahanyo",
          "aha kutlwano", "ela hloko nako ya selemo",
          "hlokomela boitshwari ba hao", "nqosa dinyewe"],
         ["Phupu - Phukwi", "motlisi wa metsi", "mariha", "../didiriso/rn_kmt/C10.png"]),
    12: ("Nut",
         "moyela hloko wa bokamoso le mofodisi.",
         ["hlahloba lehodimo", "hlahloba dinaledi", "keteka bomme",
          "ithuta ka lehodimo", "rutisa ka lehodimo"],
         ["Phato - Phatwe", "tlhapi", "mariha", "nut.png"]),
    13: ("Nut",
         "moyela hloko wa bokamoso le mofodisi.",
         ["hlahloba lehodimo", "hlahloba dinaledi", "keteka bomme",
          "ithuta ka lehodimo", "rutisa ka lehodimo",
          "itokisetse selemo se ntsha"],
         ["", "tlhapi", "", "nut.png"])
    }


matsatsi_shume0 = {
    1: ("Hapi-mesta",
        ["matlafatsa kgokahanyo le dipudueho tsa hao",
         "sebedisa maikutlo a hao ho susumetsa diketso tsa hao"]),
    2: ("Ba, Auset",
        ["hlokomela boistebo"]),
    3: ("sa-Heru, Auset",
        ["hlokomela kgokahanyo le dipudueho tsa hao",
         "sebedisa maikutlo a hao ho susumetsa diketso tsa hao",
         "hlokomela ho ela bokamoso hloko",
         "hlokomela ho tshireletsa tswelopele ya hao"]),
    4: ("Auset, sa-Heru",
        ["hlokomela kgokahanyo le dipudueho tsa hao",
         "sebedisa maikutlo a hao ho susumetsa diketso tsa hao",
         "hlokomela ho ela bokamoso hloko",
         "hlokomela ho tshireletsa tswelopele ya hao"]),
    5: ("Nebt-hut, sa-Heru",
        ["sebedisa pono le maikutlo a hao ho susumetsa diketso tsa hao",
         "ela bokamoso hloko",
         "sebedisa pono ho tshireletsa tswelopele ya hao"]),
    6: ("Hapi-mesta, Tuamutef",
        ["matlafatsa kgokahanyo le dipudueho tsa hao",
         "sebedisa maikutlo a hao ho susumetsa diketso tsa hao",
         "tshireletsa tswelopele ya hao"]),
    7: ("Qebesenef, Tuamutef",
        ["ela bokamoso hloko",
         "tshireletsa tswelopele ya hao"]),
    8: ("Tuamutef",
        ["tshireletsa tswelopele ya hao"]),
    9: ("Tuamutef, Qebesenef, Hapi",
        ["ela bokamoso ba temo hloko",
         "tswela pele ho lema",
         "tshireletsa tswelopele ya temo"]),
    10: ("Tuamutef, Hapi",
         ["tswela pele ho lema",
          "tshireletsa tswelopele ya temo"]),
    11: ("Heru",
         ["eta pele ka bohale le mofolofolo"]),
    12: ("Set",
         ["hlopha"]),
    13: ("Heru",
         ["eta pele ka bohale le mofolofolo"]),
    14: ("Auset, Nebt-hut",
         ["hlokomela ho sebedisa pono"]),
    15: ("Set",
         ["hlopha"]),
    16: ("Heru",
         ["eta pele ka bohale le mofolofolo"]),
    17: ("sa-Heru, Hapi",
         ["sebedisa maikutlo a hao ho susumetsa diketso tsa hao",
          "ela bokamoso ba temo hloko",
          "tswela pele ho lema",
          "tshireletsa tswelopele ya temo"]),
    18: ("Heru",
         ["eta pele ka bohale le mofolofolo"]),
    19: ("Hapi",
         ["tswela pele ho lema"]),
    20: ("Auset",
         ["hlokomela bopelo"]),
    21: ("Tuamutef, Qebesenef",
         ["ela bokamoso hloko",
         "tshireletsa tswelopele ya hao"]),
    22: ("Qebesenef",
         ["ela bokamoso hloko"]),
    23: ("Nebt-hut",
         ["ela bokamoso hloko"]),
    24: ("Qebesenef, Tuamutef",
         ["ela bokamoso hloko",
         "tshireletsa tswelopele ya hao"]),
    25: ("Hapi-mesta, Hapi",
         ["sebedisa maikutlo a hao ho susumetsa diketso tsa hao",
          "tswela pele ho lema"]),
    26: ("Heru",
         ["eta pele ka bohale le mofolofolo"]),
    27: ("Heru",
         ["eta pele ka bohale le mofolofolo"]),
    28: ("Heru",
         ["eta pele ka bohale le mofolofolo"]),
    29: ("Set",
         ["hlopha"]),
    30: ("sa-Heru, Hapi",
         ["sebedisa maikutlo a hao ho susumetsa diketso tsa hao",
          "ela bokamoso ba temo hloko",
          "tswela pele ho lema",
          "tshireletsa tswelopele ya temo"]),
    31: ("Hapi",
         ["tswela pele ho lema"]),
    32: ("Hapi-mesta",
         ["sebedisa maikutlo a hao ho susumetsa diketso tsa hao"]),
    33: ("Tuamutef, Qebesenef",
         ["ela bokamoso hloko",
          "tshireletsa tswelopele ya hao"]),
    34: ("Ma'at, Heru",
         ["etsa ntho engwe le engwe ka bohlale le pelo enhle",
          "eta pele ka bohale le mofolofolo"]),
    35: ("Ma'at, Heru",
         ["etsa ntho engwe le engwe ka bohlale le pelo enhle",
          "eta pele ka bohale le mofolofolo"]),
    36: ("Ma'at, Heru",
         ["etsa ntho engwe le engwe ka bohlale le pelo enhle",
          "eta pele ka bohale le mofolofolo"]),
    37: ("Ma'at, Heru, Auset",
         ["etsa ntho engwe le engwe ka bohlale le pelo enhle",
          "eta pele ka hlokomelo, bohale le mofolofolo"])
    }


ints = range(0,370)

class almanaka1:

    def __init__(self):
        self.syncdg = datetime.date(2020, 8, 27) # 351
        self.syncd = 350 + 365 * 2011
        self.dayone = datetime.date(2020, 8, 27) - datetime.timedelta(self.syncd)#2013

    def mapping(self, date):
        # Here we input a datetime object and it returns
        # the year and date in a native calendar 
        try :
            days_passed = (date - self.dayone).days
            year = int(days_passed/365+1) + 4239 #converted from 4236
            doy = days_passed%365+1
            return year, doy
        
        except Exception as e:
            print(e)    

    def thlaloso(self, day):
        try:
            botelele = len(str(day))
            if botelele == 2: # fix issue of length
                letsatsi = int(str(day)[1])
                #print(day/30 in ints)
                if day/30 not in ints: # fix issue of multiples of 10
                    if letsatsi == 0:
                        return dikgwedi1[int(day/30)+1], matsatsi_shume0[int(day/10)]
                    else:
                        return dikgwedi1[int(day/30+1)], matsatsi_shume0[int(day/10+1)]
                else: # fix issue of multples of 30
                    if letsatsi == 0:
                        return dikgwedi1[int(day/30)], matsatsi_shume0[int(day/10)]
                    else:
                        return dikgwedi1[int(day/30+1)], matsatsi_shume0[int(day/10+1)]
            elif botelele == 1:
                letsatsi = day
                if letsatsi == 0:
                        return dikgwedi1[int(day/30)+1], matsatsi_shume0[int(day/10)]
                else:
                        return dikgwedi1[int(day/30+1)], matsatsi_shume0[int(day/10+1)]
            else:
                letsatsi = int(str(day)[2])
                #print(day/30 in ints)
                if day/30 not in ints: # fix issue of multiples of 10
                    if letsatsi == 0:
                        return dikgwedi1[int(day/30)+1], matsatsi_shume0[int(day/10)]
                    else:
                        return dikgwedi1[int(day/30+1)], matsatsi_shume0[int(day/10+1)]
                else: # fix issue of multples of 30
                    if letsatsi == 0:
                        return dikgwedi1[int(day/30)], matsatsi_shume0[int(day/10)]
                    else:
                        return dikgwedi1[int(day/30+1)], matsatsi_shume0[int(day/10+1)]
        except Exception as e:
            print(e)

    def letsatsi(self, day):
        try:
            botelele = len(str(day))
            if botelele == 2: # fix issue of length
                beke = int(str(day)[0])
                letsatsi = int(str(day)[1])
                if day/30 not in ints: # fix issue of multiples of 10
                    if letsatsi == 0:
                        return beke%3, 10
                    else:
                        return beke%3 + 1, letsatsi
                else: # fix issue of multples of 30
                    if letsatsi == 0:
                        return beke%3 + 3, 10
                    else:
                        return beke%3 + 1, letsatsi
            elif botelele == 1:
                beke = 1
                letsatsi = day
                return beke%3, letsatsi
            else:
                beke = int(str(day)[0:2])
                letsatsi = int(str(day)[2])
                if day/30 not in ints: # fix issue of multiples of 10
                    if letsatsi == 0:
                        return beke%3, 10
                    else:
                        return beke%3 + 1, letsatsi
                else: # fix issue of multples of 30
                    if letsatsi == 0:
                        return beke%3 + 3, 10
                    else:
                        return beke%3 + 1, letsatsi
            
        except Exception as e:
            print(e)
        
if __name__=="__main__":
    almanaka = almanaka1()
##    dt = datetime.timedelta(1)
##    for i in range(50):
    year, day = almanaka.mapping(datetime.date.today())#+i*dt +290*dt)
    print(year,"|", day)
    kgwedi, letsatsi_shume = almanaka.thlaloso(day)
    beke, letsatsi = almanaka.letsatsi(day)
    print(kgwedi[0:2], "|", letsatsi_shume[0], "|", beke, letsatsi)

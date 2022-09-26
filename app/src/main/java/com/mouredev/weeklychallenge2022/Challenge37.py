import datetime as dt

def zelda(zelda1,zelda2):
    date1=dt.datetime.strptime(zeldaReleaseDates[zelda1], "%d/%m/%Y")
    date2=dt.datetime.strptime(zeldaReleaseDates[zelda2], "%d/%m/%Y")
    interval=int(str(abs(date1-date2)).split(" ")[0])
    msg="Cantidad de dias entre los dos lanzamientos: {}".format(interval)
    return msg


zeldaReleaseDates={
"THE_LEGEND_OF_ZELDA" :"21/02/1986",
"THE_ADVENTURE_OF_LINK" :"14/01/1987",
"A_LINK_TO_THE_PAST" :"21/11/1991",
"LINKS_AWAKENING" :"06/06/1993",
"OCARINA_OF_TIME" :"21/11/1998",
"MAJORAS_MASK" :"27/04/2000",
"ORACLE_OF_SEASONS" :"27/02/2001" ,
"ORACLE_OF_AGES" :"27/02/2001",
"FOUR_SWORDS" :"03/12/2002",
"THE_WIND_WAKER" :"13/12/2002",
"FOUR_SWORDS_ADVENTURES" :"18/03/2004",
"THE_MINISH_CUP" :"04/11/2004",
"TWILIGHT_PRINCES" :"19/11/2006",
"PHANTHOM_HOURGLASS" :"23/06/2007",
"SPIRIT_TRACKS" :"07/12/2009",
"SKYWARD_SWORD" :"18/11/2011",
"A_LINK_BETWEEN_WORLDS" :"23/11/2013",
"TRI_FORCE_HEROES" :"11/10/2015",
"BREATH_OF_THE_WILD" :"03/03/2017",
"TEARS_OF_THE_KINGDOM" :"12/05/2023"}


zelda("BREATH_OF_THE_WILD","TEARS_OF_THE_KINGDOM")

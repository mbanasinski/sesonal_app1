import data_managment_functions as data_managment
import Probability_sesonal_pattern as probanility
import Cumulative_Sesonal_pattern as cumulative
import pandas as pd


score = []
with open("listadniwroku.txt", "r") as f:
    for line in f:
        score.append(line.strip())
lista_dni_w_roku = score

def list_of_opportunities_20(data):
    list_of_opportunities = []
    d = lista_dni_w_roku.index(data)
    for key in data_managment.dic_of_tickers:
        #print(key)
        df = data_managment.open_df_probability_20(key)
        #print(df)
        try:
            probanility_today = df['%_PROBABILITY'][d]
            #print(probanility_today)
            if probanility_today > 79:
                print(data, key, probanility_today)
                list_of_opportunities.append(key)
        except:
            print('nie pobrano', key)
    return list_of_opportunities

def print_opportunities_20(data):
    d = lista_dni_w_roku.index(data)
    for key in data_managment.dic_of_tickers:
        df = data_managment.open_df_probability_20(key)
        #print(df)
        try:
            probanility_today = df['%_PROBABILITY'][d]
            #print(probanility_today)
            if probanility_today > 79:
                print(data, key, probanility_today, '[LONG]')
            elif probanility_today < 21:
                print(data, key, probanility_today, '[SHORT]')
        except:
            pass







import yfinance as yf
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import plotly.express as px
from datetime import date
#import pandas_datareader.data as web
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input

#####################################################################
# PARAMETRY DO PROGRAMU
#####################################################################

''' 
dni_w_pozycji = 20
ticker =  "ZW=F"
start_date = "2003-01-01"
'''
############################################################



def wykres_probability_Yahoo(ticker, start_date, days_in_position):
    today = str(date.today()).split("-", 1)[1].replace("-",".")
    actual_Year = int(str(date.today()).split("-", 1)[0])
    def Donwland_Data_Fron_Yahoo_probability(ticker, start_date):
        df_of_prices = yf.download(ticker, start=start_date)
        return df_of_prices

    btc_price = Donwland_Data_Fron_Yahoo_probability(ticker, start_date)

    def List_Of_returnes_probability(df_of_prices, days_in_position):
        List_Of_returnes = []
        i = 0
        for index, row in df_of_prices.iterrows():
            #print(index)
            zwrot = (btc_price['Close'][i + (days_in_position - 1)] - df_of_prices['Open'][i]) / df_of_prices['Open'][i]
            List_Of_returnes.append(zwrot)
            i = i +1
            if i == (len(df_of_prices.index) - days_in_position ):
                break
        return List_Of_returnes

    zwrory = List_Of_returnes_probability(btc_price, days_in_position)

    def cut_df_to_shape_of_returnes_probability(df_of_prices, days_in_position):
        for i in range(days_in_position):
            df_of_prices =  df_of_prices.drop(df_of_prices.index[len(df_of_prices)-1])
        return df_of_prices

    btc_price = cut_df_to_shape_of_returnes_probability(btc_price, days_in_position)

    def Add_List_of_returnes_to_df_probability(df_of_prices, List_Of_returnes):
        df_of_prices['returnes'] = List_Of_returnes

    Add_List_of_returnes_to_df_probability(btc_price, zwrory)

    def list_of_days_probability(df_of_prices):
        dzien_roku = []
        lista_dni_w_roku_b = []
        for index, row in df_of_prices.iterrows():
            data = str(index)
            data.count('0')
            data = data.replace(' 00:00:00', '')
            data = data.split("-", 1)[1]
            data = float(data.replace('-', '.'))
            dzien_roku.append(data)
            lista_dni_w_roku_b.append(data)
        return dzien_roku

    dzien_roku = list_of_days_probability(btc_price)

    def list_of_days_in_year_probability(df_of_prices):
        lista_dni_w_roku_b = []
        for index, row in df_of_prices.iterrows():
            data = str(index)
            data.count('0')
            data = data.replace(' 00:00:00', '')
            data = data.split("-", 1)[1]
            data = float(data.replace('-', '.'))
            lista_dni_w_roku_b.append(data)
        lista_dni_w_roku = []
        for x in lista_dni_w_roku_b:
            if x not in lista_dni_w_roku:
                lista_dni_w_roku.append(x)
        lista_dni_w_roku.sort()
        return lista_dni_w_roku

    lista_dni_w_roku =  list_of_days_in_year_probability(btc_price)

    def addig_dates_of_days_to_df_probability(df_of_prices, list_of_days):
        df_of_prices['dzien_roku'] = list_of_days
        return df_of_prices

    btc_price = addig_dates_of_days_to_df_probability(btc_price, dzien_roku)

    def dictionary_of_dares_probability(lista_dni_w_roku):
        dict_list_dni = {}
        for d in lista_dni_w_roku:
            dl = []
            dict_list_dni.update({d: dl})
        return dict_list_dni

    dict_list_dni = dictionary_of_dares_probability(lista_dni_w_roku)

    def Tworzenie_wykresu_probability(dict_list_dni, btc_price, lista_dni_w_roku):
        małylicznik = 0
        for item in dict_list_dni:
            licznik = 0
            for index, row in btc_price.iterrows():
                #print(zwrory[licznik])
                if dzien_roku[licznik] == item:
                    dict_list_dni[item].append(zwrory[licznik])
                else:
                    pass
                licznik = licznik + 1





        dict_list_dni_binarnie = dict_list_dni
        lll = 0
        for lista in dict_list_dni_binarnie:
            lll = lll + 1
            licznik_listy = 0
            licznik_listy = int(licznik_listy)
            for el in dict_list_dni_binarnie[lista]:
                if el > 0.0:
                    dict_list_dni_binarnie[lista][licznik_listy] = 1
                else:
                    dict_list_dni_binarnie[lista][licznik_listy] = 0
                licznik_listy = licznik_listy + 1

        dict_list_dni_procentowo = dict_list_dni_binarnie

        for lista in dict_list_dni_procentowo:
            procent = round( (sum(dict_list_dni_procentowo[lista]) / len(dict_list_dni_procentowo[lista])) * 100, 2)
            dict_list_dni_procentowo[lista] = procent

        dict_list_dni_procentowo_string = {}

        for qqq in dict_list_dni_procentowo:
            a = str(qqq)
            ab = a.replace('.', '-')
            aaa = dict_list_dni_procentowo[qqq]
            dict_list_dni_procentowo_string.update({ab: aaa})

        dict_list_dni_procentowo_string2 = {}
        for i in lista_dni_w_roku:
            e = str(i)
            if len(str(i)) < 4:
                e = str(i) + '0'
            a = e.split('.')

            a = e.split('.')
            if len(a[1]) == 1:
                a[1] = a[1] + "0"
            a[0] = a[0].replace('12','Dec')
            a[0] = a[0].replace('11','Nov')
            a[0] = a[0].replace('10','Oct')
            a[0] = a[0].replace('9','Sep')
            a[0] = a[0].replace('8','Aug')
            a[0] = a[0].replace('7','Jul')
            a[0] = a[0].replace('6','Jun')
            a[0] = a[0].replace('5','May')
            a[0] = a[0].replace('4','Apr')
            a[0] = a[0].replace('3','Mar')
            a[0] = a[0].replace('2','Feb')
            a[0] = a[0].replace('1','Jan')
            ''' 
            a[0] = a[0].replace('12','Grudzień')
            a[0] = a[0].replace('11','Listopad')
            a[0] = a[0].replace('10','Pażdziernik')
            a[0] = a[0].replace('9','Wrzesień')
            a[0] = a[0].replace('8','Sierpień')
            a[0] = a[0].replace('7','Lipiec')
            a[0] = a[0].replace('6','Czerwiec')
            a[0] = a[0].replace('5','Maj')
            a[0] = a[0].replace('4','Kwiecień')
            a[0] = a[0].replace('3','Marzec')
            a[0] = a[0].replace('2','Luty')
            a[0] = a[0].replace('1','Styczeń')
            '''
            dict_list_dni_procentowo_string2.update({a[1]+'-'+a[0]:dict_list_dni_procentowo_string[str(i).replace('.','-')]})

        tabela_procentowa = pd.DataFrame(dict_list_dni_procentowo_string2.items(), columns=['Date', '%_PROBABILITY'])

        #fig = px.line(tabela_procentowa, x='Date', y='DateValue' ,title='SESONAL PATTERN PROBABILITY'+' '+ticker)
        return tabela_procentowa

    aaa = Tworzenie_wykresu_probability(dict_list_dni, btc_price, lista_dni_w_roku)
    return aaa

def wykres_probability_Stooq(ticker, start_date, days_in_position):
    today = str(date.today()).split("-", 1)[1].replace("-",".")
    actual_Year = int(str(date.today()).split("-", 1)[0])
    def Donwland_Data_Fron_Yahoo_probability(ticker, start_date):
        df_of_prices = web.DataReader(ticker, 'stooq', start=start_date)
        xs = [000] * len(df_of_prices)
        df_of_prices['xs'] = xs
        df_of_prices = df_of_prices.sort_values(by=['Date'])
        #df_of_prices = yf.download(ticker, start=start_date)
        return df_of_prices

    btc_price = Donwland_Data_Fron_Yahoo_probability(ticker, start_date)

    def List_Of_returnes_probability(df_of_prices, days_in_position):
        List_Of_returnes = []
        i = 0
        for index, row in df_of_prices.iterrows():
            #print(index)
            zwrot = (btc_price['Close'][i + (days_in_position - 1)] - df_of_prices['Open'][i]) / df_of_prices['Open'][i]
            List_Of_returnes.append(zwrot)
            i = i +1
            if i == (len(df_of_prices.index) - days_in_position ):
                break
        return List_Of_returnes

    zwrory = List_Of_returnes_probability(btc_price, days_in_position)

    def cut_df_to_shape_of_returnes_probability(df_of_prices, days_in_position):
        for i in range(days_in_position):
            df_of_prices =  df_of_prices.drop(df_of_prices.index[len(df_of_prices)-1])
        return df_of_prices

    btc_price = cut_df_to_shape_of_returnes_probability(btc_price, days_in_position)

    def Add_List_of_returnes_to_df_probability(df_of_prices, List_Of_returnes):
        df_of_prices['returnes'] = List_Of_returnes

    Add_List_of_returnes_to_df_probability(btc_price, zwrory)

    def list_of_days_probability(df_of_prices):
        dzien_roku = []
        lista_dni_w_roku_b = []
        for index, row in df_of_prices.iterrows():
            data = str(index)
            data.count('0')
            data = data.replace(' 00:00:00', '')
            data = data.split("-", 1)[1]
            data = float(data.replace('-', '.'))
            dzien_roku.append(data)
            lista_dni_w_roku_b.append(data)
        return dzien_roku

    dzien_roku = list_of_days_probability(btc_price)

    def list_of_days_in_year_probability(df_of_prices):
        lista_dni_w_roku_b = []
        for index, row in df_of_prices.iterrows():
            data = str(index)
            data.count('0')
            data = data.replace(' 00:00:00', '')
            data = data.split("-", 1)[1]
            data = float(data.replace('-', '.'))
            lista_dni_w_roku_b.append(data)
        lista_dni_w_roku = []
        for x in lista_dni_w_roku_b:
            if x not in lista_dni_w_roku:
                lista_dni_w_roku.append(x)
        lista_dni_w_roku.sort()
        return lista_dni_w_roku

    lista_dni_w_roku =  list_of_days_in_year_probability(btc_price)

    def addig_dates_of_days_to_df_probability(df_of_prices, list_of_days):
        df_of_prices['dzien_roku'] = list_of_days
        return df_of_prices

    btc_price = addig_dates_of_days_to_df_probability(btc_price, dzien_roku)

    def dictionary_of_dares_probability(lista_dni_w_roku):
        dict_list_dni = {}
        for d in lista_dni_w_roku:
            dl = []
            dict_list_dni.update({d: dl})
        return dict_list_dni

    dict_list_dni = dictionary_of_dares_probability(lista_dni_w_roku)

    def Tworzenie_wykresu_probability(dict_list_dni, btc_price, lista_dni_w_roku):
        małylicznik = 0
        for item in dict_list_dni:
            licznik = 0
            for index, row in btc_price.iterrows():
                #print(zwrory[licznik])
                if dzien_roku[licznik] == item:
                    dict_list_dni[item].append(zwrory[licznik])
                else:
                    pass
                licznik = licznik + 1





        dict_list_dni_binarnie = dict_list_dni
        lll = 0
        for lista in dict_list_dni_binarnie:
            lll = lll + 1
            licznik_listy = 0
            licznik_listy = int(licznik_listy)
            for el in dict_list_dni_binarnie[lista]:
                if el > 0.0:
                    dict_list_dni_binarnie[lista][licznik_listy] = 1
                else:
                    dict_list_dni_binarnie[lista][licznik_listy] = 0
                licznik_listy = licznik_listy + 1

        dict_list_dni_procentowo = dict_list_dni_binarnie

        for lista in dict_list_dni_procentowo:
            procent = round( (sum(dict_list_dni_procentowo[lista]) / len(dict_list_dni_procentowo[lista])) * 100, 2)
            dict_list_dni_procentowo[lista] = procent

        dict_list_dni_procentowo_string = {}

        for qqq in dict_list_dni_procentowo:
            a = str(qqq)
            ab = a.replace('.', '-')
            aaa = dict_list_dni_procentowo[qqq]
            dict_list_dni_procentowo_string.update({ab: aaa})

        dict_list_dni_procentowo_string2 = {}
        for i in lista_dni_w_roku:
            e = str(i)
            if len(str(i)) < 4 or len(str(i)) == 4 :
                e = str(i) + '0'
            a = e.split('.')
            a[0] = a[0].replace('12','Grudzień')
            a[0] = a[0].replace('11','Listopad')
            a[0] = a[0].replace('10','Pażdziernik')
            a[0] = a[0].replace('9','Wrzesień')
            a[0] = a[0].replace('8','Sierpień')
            a[0] = a[0].replace('7','Lipiec')
            a[0] = a[0].replace('6','Czerwiec')
            a[0] = a[0].replace('5','Maj')
            a[0] = a[0].replace('4','Kwiecień')
            a[0] = a[0].replace('3','Marzec')
            a[0] = a[0].replace('2','Luty')
            a[0] = a[0].replace('1','Styczeń')
            dict_list_dni_procentowo_string2.update({a[1]+'-'+a[0]:dict_list_dni_procentowo_string[str(i).replace('.','-')]})

        tabela_procentowa = pd.DataFrame(dict_list_dni_procentowo_string2.items(), columns=['Date', 'DateValue'])
        fig = px.line(tabela_procentowa, x='Date', y='DateValue' ,title='SESONAL PATTERN PROBABILITY'+' '+ticker)
        return fig

    aaa = Tworzenie_wykresu_probability(dict_list_dni, btc_price, lista_dni_w_roku)
    return aaa


#aaa = wykres_probability_Yahoo(ticker, start_date, dni_w_pozycji)
#aaa.show()


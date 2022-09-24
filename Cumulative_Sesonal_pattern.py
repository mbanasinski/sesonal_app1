import yfinance as yf
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from datetime import date
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input


#####################################################################
#              PARAMETRY DO PROGRAMU
#####################################################################
today = str(date.today()).split("-", 1)[1].replace("-",".")
actual_Year = int(str(date.today()).split("-", 1)[0])
'''' 
dni_w_pozycji = 20
ticker =  "ZW=F"
start_date = "2003-01-01"
'''
plotting_turrent_year = False
rok_do_porownania = actual_Year


############################################################


def wykres_cumulatice_sesonal_pattern_Yachoo(ticker, start_date, nazwa_instrumentu):
    def Donwland_Data_Fron_Yahoo(ticker, start_date):
        df_of_prices = yf.download(ticker, start=start_date)
        return df_of_prices

    btc_price = Donwland_Data_Fron_Yahoo(ticker, start_date)

    def list_of_days(df_of_prices):
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

    dzien_roku = list_of_days(btc_price)

    def list_of_days_in_year(df_of_prices):
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

    lista_dni_w_roku =  list_of_days_in_year(btc_price)


    def addig_dates_of_days_to_df(df_of_prices, list_of_days):
        df_of_prices['dzien_roku'] = list_of_days
        return df_of_prices

    btc_price = addig_dates_of_days_to_df(btc_price, dzien_roku)

    def dictionary_of_dares(lista_dni_w_roku):
        dict_list_dni = {}
        for d in lista_dni_w_roku:
            dl = []
            dict_list_dni.update({d: dl})
        return dict_list_dni

    dict_list_dni = dictionary_of_dares(lista_dni_w_roku)

    ###################################################################
    #  TU ZACZYNA SIĘ CEŚĆ SPECYFICZNA
    ####################################################################

    lista_lat_b = []
    for index, row in btc_price.iterrows():
        rok = str(index)
        rok = rok.replace(' 00:00:00', '')
        rok = rok.split("-")[0]
        lista_lat_b.append(int(rok))

    lista_lat = []

    for r in lista_lat_b:
        if r not in lista_lat:
            lista_lat.append(r)
    btc_price['rok'] = lista_lat_b
    dic_rok = {}

    for nazwa in lista_lat:
        dic_rok.update({nazwa : {}})
    #print(btc_price)
    lista_lat
    #print(lista_lat)
    for rok in dic_rok:
        for index, row in btc_price.iterrows():
            if int(row[7]) == rok:
                dic_rok[rok].update({row[6] : row[3]})


    for lato in lista_lat:
        if lista_dni_w_roku[0] not in dic_rok[lato]:
            if lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[1] in dic_rok[lato]:
                dic_rok[lato].update( {lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[1]] } )
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[2] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[2]]})
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[3] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[3]]})
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[4] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[4]]})
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[5] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[5]]})
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[5] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[6]]})
            else:
                pass
        else:
            pass



    for lato in lista_lat:
        if lato in dic_rok:
            if lista_dni_w_roku[0] in dic_rok[lato]:
                pierwszy = dic_rok[lato][lista_dni_w_roku[0]]
                for dzien in lista_dni_w_roku:
                    if dzien in dic_rok[lato]:
                        dic_rok[lato][dzien] = ((dic_rok[lato][dzien] / pierwszy) - 1)*100
                    else:
                        pass
        pass







    dict_sredia_cum = {}
    for dzien in lista_dni_w_roku:
        lista = []
        for lato in lista_lat:
            if  lato in  dic_rok and dzien in dic_rok[lato]:
                lista.append(dic_rok[lato][dzien])
            else:
                pass
        srednia = sum(lista) / len(lista)

        dict_sredia_cum.update({ dzien: srednia})


    dict_sredia_cum_string = {}

    for qqq in dict_sredia_cum:
        a = str(qqq)
        ab = a.replace('.', '-')
        aaa = dict_sredia_cum[qqq]
        dict_sredia_cum_string.update({ab: aaa})

    dict_sredia_cum_string_ma10 = {}
    i = 0
    for ee in dict_sredia_cum_string:
        if i < 10:
            a = str(ee)
            aaa = dict_sredia_cum_string[ee]
            dict_sredia_cum_string_ma10.update({ a: aaa})
        elif i > 10 or i == 10:
            w = i
            a = str(ee)
            lllll = []
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 1]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 2]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 3]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 4]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 5]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 6]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 7]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 8]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 9]).replace(".","-")])
            aaa = sum(lllll)/len(lllll)
            dict_sredia_cum_string_ma10.update({ a: aaa})
        else:
            pass
        i = i +1

    lista_bierzącego_roku = []
    rrrr = rok_do_porownania
    for dzien in lista_dni_w_roku:

        if True:

           if dzien in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien]
                swiadectwo_prawdy = True
           elif dzien not in dic_rok[rrrr] and dzien == lista_dni_w_roku[0] :
                dzien1 = dic_rok[rrrr][dzien + 0]
           elif dzien not in dic_rok[rrrr] and (dzien +1 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +1 ]
           elif dzien not in dic_rok[rrrr] and (dzien +2 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +2 ]
           elif dzien not in dic_rok[rrrr] and (dzien +3 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +3 ]
           elif dzien not in dic_rok[rrrr] and (dzien +4 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +4 ]
           elif dzien not in dic_rok[rrrr] and (dzien +5 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +5 ]
           lista_bierzącego_roku.append(dzien1)




    dict_sredia_cum_string_ma10_p = {}

    for dzien in lista_dni_w_roku:
        e = str(dzien)

        if len(str(dzien)) < 4:
            e = str(dzien) + '0'
        #print(e)
        #print(dict_sredia_cum_string_ma10[str(round(dzien, 3)).replace('.','-')])
        #print((dzien))
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
        #print(a[1]+'-'+a[0])
        dict_sredia_cum_string_ma10_p.update({a[1]+'-'+a[0]: dict_sredia_cum_string_ma10[str(dzien).replace('.','-')] } )



    tabela_procentowa = pd.DataFrame(dict_sredia_cum_string_ma10_p.items(), columns=['Date', 'Sesonal Patern'])
    #print(len(lista_bierzącego_roku))

    tabela_procentowa['rok'] = lista_bierzącego_roku
    '''   

    tabela_procentowa.plot(x ='Date', y='Sesonal Patern', kind = 'line')
    if plotting_turrent_year:
        plt.plot(lista_bierzącego_roku)
    #print(tabela_procentowa)
    fig = px.line(tabela_procentowa, x='Date', y='Sesonal Patern' ,title='SESONAL PATTERN'+' '+ticker)
    '''
    return tabela_procentowa

def wykres_cumulatice_sesonal_pattern_Stooq(ticker, start_date):
    def Donwland_Data_Fron_Yahoo(ticker, start_date):
        df_of_prices = web.DataReader(ticker, 'stooq', start=start_date)
        #df_of_prices = yf.download(ticker, start=start_date)
        xs = [000] * len(df_of_prices)
        df_of_prices['xs'] = xs
        df_of_prices = df_of_prices.sort_values(by=['Date'])
        return df_of_prices

    btc_price = Donwland_Data_Fron_Yahoo(ticker, start_date)
    #print("to są dane z Yachoo")
    #print(btc_price.loc['2000-07-17',5])
    #print(btc_price)



    def list_of_days(df_of_prices):
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

    dzien_roku = list_of_days(btc_price)

    def list_of_days_in_year(df_of_prices):
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

    lista_dni_w_roku =  list_of_days_in_year(btc_price)


    def addig_dates_of_days_to_df(df_of_prices, list_of_days):
        df_of_prices['dzien_roku'] = list_of_days
        return df_of_prices

    btc_price = addig_dates_of_days_to_df(btc_price, dzien_roku)

    def dictionary_of_dares(lista_dni_w_roku):
        dict_list_dni = {}
        for d in lista_dni_w_roku:
            dl = []
            dict_list_dni.update({d: dl})
        return dict_list_dni

    dict_list_dni = dictionary_of_dares(lista_dni_w_roku)

    ###################################################################
    #  TU ZACZYNA SIĘ CEŚĆ SPECYFICZNA
    ####################################################################

    lista_lat_b = []
    for index, row in btc_price.iterrows():
        rok = str(index)
        rok = rok.replace(' 00:00:00', '')
        rok = rok.split("-")[0]
        lista_lat_b.append(int(rok))

    lista_lat = []

    for r in lista_lat_b:
        if r not in lista_lat:
            lista_lat.append(r)
    btc_price['rok'] = lista_lat_b
    dic_rok = {}

    for nazwa in lista_lat:
        dic_rok.update({nazwa : {}})
    #print(btc_price)
    lista_lat
    #print(lista_lat)
    for rok in dic_rok:
        for index, row in btc_price.iterrows():
            #print(type(rok))
            #print(type(row[6]))
            if int(row[7]) == rok:
                dic_rok[rok].update({row[6] : row[3]})


    for lato in lista_lat:
        if lista_dni_w_roku[0] not in dic_rok[lato]:
            if lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[1] in dic_rok[lato]:
                dic_rok[lato].update( {lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[1]] } )
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[2] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[2]]})
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[3] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[3]]})
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[4] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[4]]})
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[5] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[5]]})
            elif lista_dni_w_roku[0] not in dic_rok[lato] and lista_dni_w_roku[5] in dic_rok[lato]:
                dic_rok[lato].update({lista_dni_w_roku[0] : dic_rok[lato][lista_dni_w_roku[6]]})
            else:
                pass
        else:
            pass



    for lato in lista_lat:
        if lato in dic_rok:
            if lista_dni_w_roku[0] in dic_rok[lato]:
                pierwszy = dic_rok[lato][lista_dni_w_roku[0]]
                for dzien in lista_dni_w_roku:
                    if dzien in dic_rok[lato]:
                        dic_rok[lato][dzien] = ((dic_rok[lato][dzien] / pierwszy) - 1)*100
                    else:
                        pass
        pass







    dict_sredia_cum = {}
    for dzien in lista_dni_w_roku:
        lista = []
        for lato in lista_lat:
            if  lato in  dic_rok and dzien in dic_rok[lato]:
                lista.append(dic_rok[lato][dzien])
            else:
                pass
        srednia = sum(lista) / len(lista)

        dict_sredia_cum.update({ dzien: srednia})


    dict_sredia_cum_string = {}

    for qqq in dict_sredia_cum:
        a = str(qqq)
        ab = a.replace('.', '-')
        aaa = dict_sredia_cum[qqq]
        dict_sredia_cum_string.update({ab: aaa})

    dict_sredia_cum_string_ma10 = {}
    i = 0
    for ee in dict_sredia_cum_string:
        if i < 10:
            a = str(ee)
            aaa = dict_sredia_cum_string[ee]
            dict_sredia_cum_string_ma10.update({ a: aaa})
        elif i > 10 or i == 10:
            w = i
            a = str(ee)
            lllll = []
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 1]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 2]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 3]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 4]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 5]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 6]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 7]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 8]).replace(".","-")])
            lllll.append(dict_sredia_cum_string[str(lista_dni_w_roku[w - 9]).replace(".","-")])
            aaa = sum(lllll)/len(lllll)
            dict_sredia_cum_string_ma10.update({ a: aaa})
        else:
            pass
        i = i +1

    lista_bierzącego_roku = []
    rrrr = rok_do_porownania
    for dzien in lista_dni_w_roku:

        if True:

           if dzien in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien]
                swiadectwo_prawdy = True
           elif dzien not in dic_rok[rrrr] and dzien == lista_dni_w_roku[0] :
                dzien1 = dic_rok[rrrr][dzien + 0]
           elif dzien not in dic_rok[rrrr] and (dzien +1 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +1 ]
           elif dzien not in dic_rok[rrrr] and (dzien +2 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +2 ]
           elif dzien not in dic_rok[rrrr] and (dzien +3 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +3 ]
           elif dzien not in dic_rok[rrrr] and (dzien +4 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +4 ]
           elif dzien not in dic_rok[rrrr] and (dzien +5 ) in dic_rok[rrrr] :
                dzien1 = dic_rok[rrrr][dzien +5 ]
           lista_bierzącego_roku.append(dzien1)




    dict_sredia_cum_string_ma10_p = {}

    for dzien in lista_dni_w_roku:
        e = str(dzien)

        if len(str(dzien)) < 4:
            e = str(dzien) + '0'
        #print(e)
        #print(dict_sredia_cum_string_ma10[str(round(dzien, 3)).replace('.','-')])
        #print((dzien))
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
        #print(a[1]+'-'+a[0])
        dict_sredia_cum_string_ma10_p.update({a[1]+'-'+a[0]: dict_sredia_cum_string_ma10[str(dzien).replace('.','-')] } )



    tabela_procentowa = pd.DataFrame(dict_sredia_cum_string_ma10_p.items(), columns=['Date', 'Sesonal Patern'])
    #print(len(lista_bierzącego_roku))
    #print(tabela_procentowa)
    tabela_procentowa['rok'] = lista_bierzącego_roku


    #print(type(tabela_procentowa))

    #tabela_procentowa.to_pickle(nazwa_instrumentu +"_cumulative.pkl")
    tabela_procentowa.to_pickle("cumulative.pkl")

    tabela_procentowa.plot(x ='Date', y='Sesonal Patern', kind = 'line')
    if plotting_turrent_year:
        plt.plot(lista_bierzącego_roku)
    #print(tabela_procentowa)
    fig = px.line(tabela_procentowa, x='Date', y='Sesonal Patern' ,title='SESONAL PATTERN'+' '+ticker)

    return tabela_procentowa


#fig = wykres_cumulatice_sesonal_pattern_Yachoo(ticker, start_date, 'ZLOTO')
#print(type(fig))
#fig.show()



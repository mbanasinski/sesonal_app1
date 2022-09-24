import Probability_sesonal_pattern as probanility
import Cumulative_Sesonal_pattern as cumulative
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
from datetime import date
import plotly.graph_objects as go

''' 
dni_w_pozycji = 20
#ticker =  "GC=F"
start_date = "1990-01-01"
'''
dic_of_tickers = {"Gold":"GC=F","Silver":"SI=F", "Palladium":"PA=F", "Platinum":"PL=F", "Copper":"HG=F", "Aluminum":"ALI=F", "Crude Oil":"CL=F", "Heating Oil":"HO=F", "Natural Gas":"NG=F", "Gasoline":"RB=F", "Corn":"ZC=F", "Oat":"ZO=F", "Wheat":"KE=F", "Soybean":"ZS=F", "Soybean Oil":"ZL=F", "Cocoa":"CC=F", "Coffee":"KC=F", "Cotton":"CT=F", "Lumber":"LBS=F", "Sugar":"SB=F", "10-Year T-Note":"ZN=F", "S&P 500":"^GSPC", "Nikkei 225":"^N225", "Dow Jones":"^DJI", "Apple Inc":"AAPL", "Tesla":"TSLA", "Amazon":"AMZN", "American Airlines":"AAL", "Alphabet(Google)":"GOOGL", "Bitcoin USD":"BTC-USD", "EURUSD":"EURUSD=X", "USDJPY":"JPY=X", "GBPUSD":"GBPUSD=X", "AUDUSD":"AUDUSD=X", "NZDUSD":"NZDUSD=X", "EURJPY":"EURJPY=X", "GBPJPY":"GBPJPY=X", "EURGBP":"EURGBP=X", "EURCAD":"EURCAD=X", "EURSEK":"EURSEK=X", "EURCHF":"EURCHF=X", "EURHUF":"EURHUF=X", "EURJPY":"EURJPY=X", "USDHKD":"HKD=X", "USDSGD":"SGD=X", "USDINR":"INR=X", "USDRUB":"RUB=X", "EURCAD":"EURCAD=X", "CADCHF":"CADCHF=X", "CADJPY":"CADJPY=X", "CHFJPY":"CHFJPY=X", "GBPCAD":"GBPCAD=X", "GBPCHF":"GBPCHF=X", "AUDCAD":"AUDCAD=X", "AUDCHF":"AUDCHF=X", "AUDJPY":"AUDJPY=X", "AUDNZD":"AUDNZD=X", "CHFPLN":"CHFPLN=X", "EURNOK":"EURNOK=X", "EURNZD":"EURNZD=X", "EURPLN":"EURPLN=X", "EURSEK":"EURSEK=X", "GBPAUD":"GBPAUD=X", "GBPNZD":"GBPNZD=X", "GBPPLN":"GBPPLN=X", "NZDJPY":"NZDJPY=X", "USDNOK":"NOK=X", "USDPLN":"PLN=X"}




list_of_instruments = []

for key in dic_of_tickers:
    print(key)
    aaa = key
    key = {}
    key.update({"label": aaa})
    key.update({"value": aaa})
    list_of_instruments.append(key)

#a# See PyCharm help at https://www.jetbrains.com/help/pycharm/bc = probanility.wykres_probability_Yahoo(ticker, start_date, dni_w_pozycji)
#abc = probanility.wykres_probability_Stooq("GC.F", start_date, dni_w_pozycji)
#abcd = cumulative.wykres_cumulatice_sesonal_pattern_Yachoo(ticker, "1990-01-01" )
#abc = wykres_cumulatice_sesonal_pattern_Stooq("goog", start_date)


#abc.show()
#abcd.show()

def akyualizuj_cumulative_30(nazwa_instrumentu):
    tiker = dic_of_tickers[nazwa_instrumentu]
    tabela_procentowa = cumulative.wykres_cumulatice_sesonal_pattern_Yachoo(tiker, "1990-01-01", nazwa_instrumentu )
    #tabela_procentowa.to_pickle(nazwa_instrumentu +"_cumulative.pkl")
    #print(type(tabela_procentowa))
    tabela_procentowa.to_pickle(nazwa_instrumentu+"_cumulative_30.pkl")
    #print("tu zaczyna sie main")
    return

def open_df_cumulative_30(nazwa_instrumentu):
    aaa = nazwa_instrumentu + "_cumulative_30.pkl"
    tabela_procentowa =  pd.read_pickle(aaa)
    return tabela_procentowa

def fig_cumulative_30(nazwa_instrumentu):
    tabela_procentowa =  open_df_cumulative_30(nazwa_instrumentu)
    #tabela_procentowa.plot(x ='Date', y='Sesonal Patern', kind = 'line')
    fig = px.line(tabela_procentowa, x='Date', y='Sesonal Patern' ,title='SESONAL PATTERN last 30 years'+' '+nazwa_instrumentu)
    x = dzis()
    fig.add_shape(go.layout.Shape(type="line",yref="paper", xref="x"),x0=x,y0=0, x1=x, y1=1,)
    #print(tabela_procentowa)
    return fig

def akyualizuj_cumulative_10(nazwa_instrumentu):
    tiker = dic_of_tickers[nazwa_instrumentu]
    tabela_procentowa = cumulative.wykres_cumulatice_sesonal_pattern_Yachoo(tiker, "2012-01-01", nazwa_instrumentu )
    #tabela_procentowa.to_pickle(nazwa_instrumentu +"_cumulative.pkl")
    #print(type(tabela_procentowa))
    tabela_procentowa.to_pickle(nazwa_instrumentu+"_cumulative_10.pkl")
    #print("tu zaczyna sie main")
    return

def open_df_cumulative_10(nazwa_instrumentu):
    aaa = nazwa_instrumentu + "_cumulative_10.pkl"
    tabela_procentowa =  pd.read_pickle(aaa)
    return tabela_procentowa




def fig_cumulative_10(nazwa_instrumentu):
    tabela_procentowa =  open_df_cumulative_10(nazwa_instrumentu)
    x = dzis()
    #tabela_procentowa.plot(x ='Date', y='Sesonal Patern', kind = 'line')
    fig = px.line(tabela_procentowa, x='Date', y='Sesonal Patern' ,title='SESONAL PATTERN last 10 years'+' '+nazwa_instrumentu)
    fig.add_shape(go.layout.Shape(type="line",yref="paper", xref="x"),x0=x,y0=0, x1=x, y1=1,)
    #print(tabela_procentowa)
    return fig

def akyualizuj_probability_20(nazwa_instrumentu):
    ticker = dic_of_tickers[nazwa_instrumentu]
    start_date = "1990-01-01"
    abc = probanility.wykres_probability_Yahoo(ticker, start_date, 20)
    abc.to_pickle(nazwa_instrumentu+"_probability_20.pkl")

def open_df_probability_20(nazwa_instrumentu):
    aaa = nazwa_instrumentu + "_probability_20.pkl"
    tabela_procentowa =  pd.read_pickle(aaa)
    return tabela_procentowa

def fig_probability_20(nazwa_instrumentu):
    tabela_procentowa =  open_df_probability_20(nazwa_instrumentu)
    fig = px.line(tabela_procentowa, x='Date', y='%_PROBABILITY' ,title='HISTORICAL PROBABILITY OF WINNING 20 TRADING DAYS POSITION '+' '+nazwa_instrumentu)
    x = dzis()
    fig.add_shape(go.layout.Shape(type="line",yref="paper", xref="x"),x0=x,y0=0, x1=x, y1=1,)
    #print(tabela_procentowa)
    return fig

def akyualizuj_probability_60(nazwa_instrumentu):
    ticker = dic_of_tickers[nazwa_instrumentu]
    start_date = "1990-01-01"
    abc = probanility.wykres_probability_Yahoo(ticker, start_date, 60)
    abc.to_pickle(nazwa_instrumentu+"_probability_60.pkl")

def open_df_probability_60(nazwa_instrumentu):
    aaa = nazwa_instrumentu + "_probability_60.pkl"
    tabela_procentowa =  pd.read_pickle(aaa)
    return tabela_procentowa

def fig_probability_60(nazwa_instrumentu):
    tabela_procentowa =  open_df_probability_60(nazwa_instrumentu)
    fig = px.line(tabela_procentowa, x='Date', y='%_PROBABILITY' ,title='HISTORICAL PROBABILITY OF WINNING 60 TRADING DAYS POSITION '+' '+nazwa_instrumentu)
    x = dzis()
    fig.add_shape(go.layout.Shape(type="line",yref="paper", xref="x"),x0=x,y0=0, x1=x, y1=1,)
    #print(tabela_procentowa)
    return fig
'''' 
def actualize():
    i = 0
    for key in dic_of_tickers:
        if i > 40:
            print(key, 'corresponds to', dic_of_tickers[key])
            try:
                akyualizuj_cumulative_30(key)
                akyualizuj_cumulative_10(key)
                akyualizuj_probability_20(key)
                akyualizuj_probability_60(key)
                print('POBRANO TICKER')
                print(i,len(list_of_instruments), key)
                i = i + 1
            except:
                print('SPIERDOLIŁO SIĘ')
                print(i,len(list_of_instruments), key)
                i = i + 1
        else:
            i = i +1


'''

def actualize():
    i = 0
    for key in dic_of_tickers:
        print(key, 'corresponds to', dic_of_tickers[key])
        try:
            akyualizuj_cumulative_30(key)
            akyualizuj_cumulative_10(key)
            akyualizuj_probability_20(key)
            akyualizuj_probability_60(key)
            print('POBRANO TICKER')
            print(i,len(list_of_instruments), key)
            i = i + 1
        except:
            print('SPIERDOLIŁO SIĘ')
            print(i,len(list_of_instruments), key)
            i = i + 1



def dzis():
    today = date.today()
    Tlist = str(today).split('-')
    a = [Tlist[1], Tlist[2]]
    a[0] = a[0].replace('12','Dec')
    a[0] = a[0].replace('11','Nov')
    a[0] = a[0].replace('10','Oct')
    a[0] = a[0].replace('09','Sep')
    a[0] = a[0].replace('08','Aug')
    a[0] = a[0].replace('07','Jul')
    a[0] = a[0].replace('06','Jun')
    a[0] = a[0].replace('05','May')
    a[0] = a[0].replace('04','Apr')
    a[0] = a[0].replace('03','Mar')
    a[0] = a[0].replace('02','Feb')
    a[0] = a[0].replace('01','Jan')
    dzis = a[1]+'-'+a[0]
    return dzis



def fig_cumulative(nazwa_instrumentu, t):
    if t == 10:
        fig = fig_cumulative_10(nazwa_instrumentu)
    elif t == 30:
        fig = fig_cumulative_30(nazwa_instrumentu)
    return fig
#akyualizuj_cumulative_30('ZLOTO')
#aaaaaa = fig_cumulative_30('ZLOTO')
#aaaaaa.show()
#akyualizuj_probability_20('ZLOTO')
''' 
akyualizuj_probability_60('GOLD')
fig_probability_60('GOLD').show()
'''
''' 
actualize()
fig_cumulative_10('GOLD').show()
fig_probability_20('GOLD').show()
'''

#fig_cumulative_10('Gold').show()

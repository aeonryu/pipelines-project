from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

##Parte 1: Obteniendo los datos del precio de las accciones de las 5 empresas top involucradas en la investigación de cómputo cuántico

# Your key here
key = 'PUII9SGD6FZ1OTEF'
# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

# Get the data, returns a tuple

#Alphabet
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
googl_data, googl_meta_data = ts.get_daily(symbol='GOOGL')
# aapl_sma is a dict, aapl_meta_sma also a dict
googl_sma, googl_meta_sma = ti.get_sma(symbol='GOOGL')

import time
t = 60 
time.sleep(t) #60 segundos de espera, por las características de la API

#Lockheed Martin
lmt_data, lmt_meta_data = ts.get_daily(symbol='LMT')
lmt_sma, lmt_meta_sma = ti.get_sma(symbol='LMT')
time.sleep(t)

#IBM
ibm_data, ibm_meta_data = ts.get_daily(symbol='IBM')
ibm_sma, ibm_meta_sma = ti.get_sma(symbol='IBM')
time.sleep(t)

#Microsoft
msft_data, msft_meta_data = ts.get_daily(symbol='MSFT')
msft_sma, msft_meta_sma = ti.get_sma(symbol='MSFT')
time.sleep(t)

#Intel
intc_data, intc_meta_data = ts.get_daily(symbol='INTC')
intc_sma, intc_meta_sma = ti.get_sma(symbol='INTC')
time.sleep(t)

# Visualization
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
googl_data['4. close'].plot(label='Google')
lmt_data['4. close'].plot()
ibm_data['4. close'].plot()
msft_data['4. close'].plot()
intc_data['4. close'].plot()
plt.xlabel('Fechas')
plt.ylabel('Precio en dólares')
plt.legend(['Google','Lockheed Martin','IBM','Microsoft','Intel'])
plt.tight_layout()
plt.grid()
plt.show()

#20 septiembre Alphabet claims QS (IBM presenta controversia)
#23 octubre Alphabet confirms QS (continua la controversia)

##Parte 2: Obteniendo los datos de las noticias relacionadas con quantum computing en Financial Times con RSS
import feedparser #parses different versions of rss and formats
import pandas as pd

url = 'https://www.ft.com/news-feed'
fin_times = feedparser.parse(url)
df = pd.DataFrame(fin_times.entries) #Aquí creo el dataframe


import re
#Probar si existe la palabra 'quantum' en los títulos de las noticias
for i in range(len(fin_times.entries)):
    print(re.findall(r'quantum',df.title[i]))

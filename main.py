'''
Na podstawie danych w pliku messy_data.csv przygotuj interaktywny dashboard do analizy danych.

Etapy pracy domowej:

1. wstępna analiza danych i czyszczenie:

a. duplikaty

b. wartości odstające

c. spójność

d. braki w danych

e. skala wartości

f. inne

2. wizualizacja rozkładu zmiennych, zależności ceny od innych zmiennych, liczebność kategorii

3. budowa modelu regresji ceny od pozostałych zmiennych. Istotne zmienne należy wybrać eliminacją wsteczną lub selekcją postępującą.

4. wizualizacja modelu regresji

5. stworzenie dashboardu z powyższymi wizualizacjami i próbką danych w postaci tabeli. Dashboard powinien umożliwiać zmianę parametrów wykresów - np. zależność ceny od innej, wybranej przez użytkownika zmiennej

Wszystkie wizualizacje i dane powinny zostać zaprezentowane w postaci dashboardu. Etapy czyszczenia danych i budowy modelu regresji należy zawrzeć w notatniku Jupytera (.ipynb).

Deadline: 28.01.2024 (na oddanie kodu do assigmnentu)

Forma oddania: repo na githubie i oddanie na ćwiczeniach

Pracę domową wykonujemy indywidualnie.
'''

import numpy as np
import pandas as pd
from dash import Dash, html, dcc, Input, Output 
import plotly.express as px

app = Dash(__name__)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

data_  = pd.read_csv('messy_data.csv')
#print(data_)
#print(data_.loc[:,' price'].mean())
#print(data_.loc[:,'carat'].mean())
#print(np.where(pd.isnull(data_['carat'])))
#print (data_.dtypes)

#for i in data_.columns:
#    print (i)
#    print(np.where())
#print(np.where(data_==' ','0',data_))
#print(np.where(pd.isnull(data_)==True,0,data_))


data_a=(np.where(data_==' ','0',data_))
data_a=(np.where(pd.isnull(data_a)==True,0,data_a))
print(data_a)
data_a[:,0]=data_a[:,0].astype(np.float64)
data_a[:,4]=data_a[:,4].astype(np.float64)
data_a[:,5]=data_a[:,5].astype(np.float64)
data_a[:,6]=data_a[:,6].astype(np.float64)
data_a[:,7]=data_a[:,7].astype(np.float64)
data_a[:,8]=data_a[:,8].astype(np.float64)
data_a[:,9]=data_a[:,9].astype(np.float64)
print(data_a)


data_ap = pd.DataFrame(data_a,columns=['carat','clarity','color','cut','x dimension','y dimension','z dimension','depth','table','price'])

print(data_ap)
print('AAAA')
print(data_ap['price'].mean())



def Mean_Zero_Parameters( column_of_df):
    #Funckja w polach zadanej kolumny, które są równe zero (czyli byłe puste) wpisuje wartość średnią tej kolumny
    print(column_of_df.mean())
    apap=column_of_df.mean()
    for index1 in column_of_df.index:
        if column_of_df[index1]==0:
            column_of_df[index1]= apap 

    print(column_of_df.mean())



def otliersDelete( column_of_df):
    #Funckja w polach zadanej kolumny, które są równe zero (czyli byłe puste) wpisuje wartość średnią tej kolumny
    print(column_of_df.mean())
    apap=column_of_df.mean()
    for index1 in column_of_df.index:
        if column_of_df[index1]>5*apap:
            column_of_df[index1]= apap 

    print(column_of_df.mean())


def toLowerColumn( column_of_df):
    #Funckja w polach zadanej kolumny, które są równe zero (czyli byłe puste) wpisuje wartość średnią tej kolumny
    for index1 in column_of_df.index:
        column_of_df[index1]=column_of_df[index1].lower()



Mean_Zero_Parameters(data_ap.loc[:,'carat'])
Mean_Zero_Parameters(data_ap.loc[:,'x dimension'])
Mean_Zero_Parameters(data_ap.loc[:,'y dimension'])
Mean_Zero_Parameters(data_ap.loc[:,'z dimension'])
Mean_Zero_Parameters(data_ap.loc[:,'depth'])
Mean_Zero_Parameters(data_ap.loc[:,'table'])
Mean_Zero_Parameters(data_ap.loc[:,'price'])


otliersDelete(data_ap.loc[:,'carat'])
otliersDelete(data_ap.loc[:,'x dimension'])
otliersDelete(data_ap.loc[:,'y dimension'])
otliersDelete(data_ap.loc[:,'z dimension'])
otliersDelete(data_ap.loc[:,'depth'])
otliersDelete(data_ap.loc[:,'table'])
otliersDelete(data_ap.loc[:,'price'])


toLowerColumn(data_ap.loc[:,'clarity'])
toLowerColumn(data_ap.loc[:,'color'])
toLowerColumn(data_ap.loc[:,'cut'])




fig = px.scatter(data_ap, x='carat', y='price')

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div([
    html.Div(children=[
        html.Label('X axes'),
        dcc.Dropdown(['carat','clarity','color','cut','x dimension','y dimension','z dimension','depth','table','price'], 'carat',id='Ydropdown'),
        html.Label('Y axes'),
        dcc.Dropdown(['carat','clarity','color','cut','x dimension','y dimension','z dimension','depth','table','price'], 'price',id='Xdropdown'),
    ], style={'padding': 10, 'flex': 'row'}),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )

], style={'display': 'flex', 'flex-direction': 'column'})


@app.callback(
    Output('example-graph-2', 'figure'),
    Input('Ydropdown', 'value'),
    Input('Xdropdown', 'value'))
def update_figure(newY,newX):
    fig = px.scatter(data_ap, x=newX, y=newY)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
#print(data_ap.loc[:,'carat'].mean())
#apap=data_ap.loc[:,'carat'].mean()
#for index1 in data_ap.index:
#    if data_ap['carat'][index1]==0:
#       data_ap['carat'][index1]= apap 





print(data_ap.loc[:,'carat'].mean())



#print (data_ap.dtypes)
#print(data_a.price.astype(float))

#for i in data_a.columns:
#    print (i)
#    print(data_a.i.astype(float))
#data_a[" price"].apply(pd.to_numeric)#pd.to_numeric(data_a[" price"])
#print(data_a[" price",1].astype(float))
#for i in data_.columns:
#    print (i)
#    print(np.where())



#print(np.where(pd.isnull(data_.columns.)))
#import statsmodels.api as sm
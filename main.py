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
import plotly.graph_objects as go
import statsmodels.formula.api as smf

import statsmodels.api as sm

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


data_a=(np.where(data_==' ',float('nan'),data_))
data_a=(np.where(pd.isnull(data_a)==True,float('nan'),data_a))
print(data_a)
#data_a[:,0]=data_a[:,0].astype(np.float64)
#data_a[:,4]=data_a[:,4].astype(np.float64)
#data_a[:,5]=data_a[:,5].astype(np.float64)
#data_a[:,6]=data_a[:,6].astype(np.float64)
#data_a[:,7]=data_a[:,7].astype(np.float64)
#data_a[:,8]=data_a[:,8].astype(np.float64)
#data_a[:,9]=data_a[:,9].astype(np.float64)


print(data_a)

data_a
data_ap = pd.DataFrame(data_a,columns=['carat','clarity','color','cut','xdimension','ydimension','zdimension','depth','table','price'])

data_ap['carat']=pd.to_numeric(data_ap['carat'])

data_ap['xdimension']=pd.to_numeric(data_ap['xdimension'])

data_ap['ydimension']=pd.to_numeric(data_ap['ydimension'])

data_ap['zdimension']=pd.to_numeric(data_ap['zdimension'])

data_ap['depth']=pd.to_numeric(data_ap['depth'])

data_ap['table']=pd.to_numeric(data_ap['table'])

data_ap['price']=pd.to_numeric(data_ap['price'])

#s = pd.Series([1, 2, 3], dtype="Int64")
#pd.to_numeric(s, downcast="integer")

print(data_ap.info())
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
    a=column_of_df
    for index1 in column_of_df.index:
        a[index1]=column_of_df[index1].lower()        
    column_of_df=a   

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

pom = data_ap['carat']
#pom = pom.fillna(1)
#data_ap.loc['carat'] = pom
#data_ap['carat']=
#data_ap['carat']=data_ap['carat'].fillna(data_ap['carat'].mean())

Mean_Zero_Parameters(data_ap.loc[:,'carat'])
data_ap.loc[:,'carat'] = np.round(np.array(data_ap.loc[:,'carat'], dtype=np.float64), 2)

Mean_Zero_Parameters(data_ap.loc[:,'xdimension'])
data_ap.loc[:,'xdimension'] = np.round(np.array(data_ap.loc[:,'xdimension'], dtype=np.float64), 2)

Mean_Zero_Parameters(data_ap.loc[:,'ydimension'])
data_ap.loc[:,'ydimension'] = np.round(np.array(data_ap.loc[:,'ydimension'], dtype=np.float64), 2)

Mean_Zero_Parameters(data_ap.loc[:,'zdimension'])
data_ap.loc[:,'zdimension'] = np.round(np.array(data_ap.loc[:,'zdimension'], dtype=np.float64), 2)



Mean_Zero_Parameters(data_ap.loc[:,'depth'])
data_ap.loc[:,'depth'] = np.round(np.array(data_ap.loc[:,'depth'], dtype=np.float64), 2)

Mean_Zero_Parameters(data_ap.loc[:,'table'])
data_ap.loc[:,'table'] = np.round(np.array(data_ap.loc[:,'table'], dtype=np.float64), 2)

Mean_Zero_Parameters(data_ap.loc[:,'price'])
data_ap.loc[:,'price'] = np.round(np.array(data_ap.loc[:,'price'], dtype=np.float64), 2)

print(data_ap.info())
'''aabb="xdimension"
bbaa="ydimension"
ccnn=aabb+" ~ "+bbaa
model = smf.ols(formula=ccnn,data=data_ap).fit()
print(model.summary())
'''


otliersDelete(data_ap.loc[:,'carat'])
otliersDelete(data_ap.loc[:,'xdimension'])
otliersDelete(data_ap.loc[:,'ydimension'])
otliersDelete(data_ap.loc[:,'zdimension'])
otliersDelete(data_ap.loc[:,'depth'])
otliersDelete(data_ap.loc[:,'table'])
otliersDelete(data_ap.loc[:,'price'])


toLowerColumn(data_ap.loc[:,'clarity'])
toLowerColumn(data_ap.loc[:,'color'])
toLowerColumn(data_ap.loc[:,'cut'])



fig = px.scatter(data_ap, x='carat', y='price')
'''print(data_ap)
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
'''
app.layout = html.Div([
    html.Div(children=[
        html.Label('X axes'),
        dcc.Dropdown(['carat','clarity','color','cut','xdimension','ydimension','zdimension','depth','table','price'], 'carat',id='Ydropdown'),
        html.Label('Y axes'),
        dcc.Dropdown(['carat','clarity','color','cut','xdimension','ydimension','zdimension','depth','table','price'], 'price',id='Xdropdown'),
    ], style={'padding': 10, 'flex': 'row'}),

    dcc.Graph(
        id='graph',
        figure=fig
    ),

    generate_table(data_ap)

], style={'display': 'flex', 'flex-direction': 'column'})


@app.callback(
    Output('graph', 'figure'),
    Input('Ydropdown', 'value'),
    Input('Xdropdown', 'value'))
def update_figure(newX,newY):
    
    fig1 = px.scatter(data_ap, x=newX, y=newY)

    if data_ap[newX].dtypes==float and data_ap[newY].dtypes==float:
        #fig = px.scatter(data_ap, x=newX, y=newY)
        aabb=newX
        bbaa=newY
        ccnn=bbaa+" ~ "+aabb
        model = smf.ols(formula=ccnn,data=data_ap).fit()
        print(model.summary())
        data_ap['fitted']=model.fittedvalues
        print(data_ap['fitted'])
        print("adnext")
        print(data_ap[newX])
        newXValue=data_ap[newX]
        fig2 = px.scatter(x=newXValue,y=data_ap['fitted'],color_discrete_sequence=['red'])
        fig=go.Figure(data=fig1.data+fig2.data)
    else:
        fig = fig1
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
#print(data_ap.loc[:,'carat'].mean())
#apap=data_ap.loc[:,'carat'].mean()
#for index1 in data_ap.index:
#    if data_ap['carat'][index1]==0:
#       data_ap['carat'][index1]= apap 









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
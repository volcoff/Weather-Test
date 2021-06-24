#Mande a llamar la libreria pandas
from datetime import date
import pandas as pd

#Cree esta lista para poder construir un nuevo dataframe
weatherList= []
#Cre mi lista con el nombre wheder
wheader=[["1/1/20","FALSE"],["1/2/20","TRUE"],["1/3/20", "TRUE"], ["1/4/20","FALSE"],["1/5/20","FALSE"],["1/6/20","TRUE"],["1/7/20","FALSE"],["1/8/20","TRUE"],["1/9/20","TRUE"],["1/10/20","TRUE"]]
#Crear mi Data frame de pandas
df= pd.DataFrame(wheader)

#cargue la lista en un dataframe
BadWeaderDF = pd.DataFrame(wheader,columns=['Date','was_rainy'])

#Esta linea se puede comentar, realmente la puse solo para verificar que los datos eran correctos
#print(df)

for i in range(1,len(df)):
    today=df.iloc[i,1]
    yesterday=df.iloc[i-1,1]
    #me posiciono en los dias buenos, ya que quiero saber si el dia anterior llovio
    if (today=="TRUE"):
        #aqui reviso si el dia anterior llovio
        if(yesterday=="FALSE"):
            #aqui estoy generando un json para cargarlo como dataframe, si simplemento el dataframe.appent me trae todo el dataframe
            BadDate=df.iloc[i,0]
            was_rainy=df.iloc[i,1]   
            Data={'Date':BadDate,'was_rainy':was_rainy}
            weatherList.append(Data)

#Aqui solo cargue el json al dataframe nuevo para manipularlo, pero igual se puede manipular con el json
BadWeaderDF=pd.DataFrame(weatherList,columns=['Date','was_rainy'])
print(BadWeaderDF)
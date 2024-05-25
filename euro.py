#EUROPE DASHBOARD PROJECT 
#IMPORT LIBRARIES
import pandas as pd
import numpy as np
import folium
# CREATE A DATAFRAME HAVING COUNTRY COORDINATES
df2 = pd.read_excel('./country_coordinates.xlsx')
df2
#CREATE A VARIABLE CONSISTING COLUMN NAMES OF DATAFRAME DF2
column = df2.columns
column
#CREATING A VARIABLE var WHICH WILL FIRST STORE THE VALUE OF LONGITUDE AND LATITUDE AND THEN CREATE THE MAP
var = folium.Map(location=[df2.LONGTITUDE.mean(), df2.LATITUDE.mean()], 
                 zoom_start=3, control_scale=True)

#Loop through each row in the dataframe
for i,row in df2.iterrows():
    #Setup the content of the popup
    iframe = folium.IFrame('Well Name: ,' +str(row["COUNTRY"]))
    #Initialise the popup using the iframe
    popup = folium.Popup(iframe, min_width=300, max_width=300)
    
    #Add each row to the map
    folium.Marker(location=[row['LONGTITUDE'],row['LATITUDE']],
                  popup = popup, c=row['COUNTRY']).add_to(var)
    
    var.save('euro.html')

#DEFINING A FUCTION PRINMAP WHICH PLOTS POINTS ON MAP USING DF2 DATAFRAME
def printmap(m, df2):
    df1 = df2[df2['COUNTRY'].isin(m)]
    print(df1)
    
    var = folium.Map(location=[df1.LONGTITUDE.mean(), df1.LATITUDE.mean()], 
                 zoom_start=3, control_scale=True)

    #Loop through each row in the dataframe
    for i,row in df1.iterrows():
        #Setup the content of the popup
        iframe = folium.IFrame('Well Name:' + str(row["COUNTRY"]))

        #Initialise the popup using the iframe
        popup = folium.Popup(iframe, min_width=300, max_width=300)

        #Add each row to the map
        folium.Marker(location=[row['LONGTITUDE'],row['LATITUDE']],
                      popup = popup, c=row['COUNTRY']).add_to(var)
        
    var.save('euro.html')

a="19N/20D"
b="29N/30D"
c="39N/40D"
days=['a','b','c']
days
k='FRANCE'
f='DENMARK'


n19=['FRANCE','BELGIUM','NETHERLANDS','GERMANY','SWITZERLAND','CZECHIA','DENMARK']
n29=['FRANCE','BELGIUM','NETHERLANDS','GERMANY','SWITZERLAND','CZECHIA','ITALY','AUSTRIA','DENMARK']
n39=df2.COUNTRY.unique()
selection19=['BELGIUM','NETHERLANDS','GERMANY','SWITZERLAND','CZECHIA' , 'AUSTRIA']
selection29=['BELGIUM', 'LUXEMBOURG','NETHERLANDS','GERMANY','HUNGARY','SWITZERLAND','CZECHIA','ITALY','AUSTRIA',]


print("Enter the days you want to spent in europe (travelling not include )\n" ,days)

print("a=19N/20D ,b=29N/30D , c=39N/40D")


start=input("enter the days \n" )


print("\nso the starting point is FRANCE and your exit is from DENMARK\n")



if start.lower()=="a":
    
    print("\nFor the 9 nights and 10 days your countries are as \n\n",n19)
    
    print("\nso the package you have select is \n ", start)

    print("select the countries from  ", selection19)
    selection=input(" select country you want to eliminate ")


    if selection=="BELGIUM":
        print("your country are as follow ")
        m=(['NETHERLANDS', 'GERMANY', 'SWITZERLAND', 'CZECHIA', 'AUSTRIA'])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)


    elif selection=="NETHERLANDS":
        print("your country are as follow ")
        m=(['BELGIUM', 'GERMANY', 'SWITZERLAND', 'CZECHIA', 'AUSTRIA'])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)

    elif selection=="GERMANY":
        print("your country are as follow ")
        m=(['BELGIUM', 'NETHERLANDS', 'SWITZERLAND', 'CZECHIA', 'AUSTRIA'])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)

    elif selection=="SWITZERLAND":
        print("your country are as follow ")
        m=(['BELGIUM', 'NETHERLANDS', 'GERMANY', 'CZECHIA', 'AUSTRIA'])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)

    elif selection=="CZECHIA":
        print("your country are as follow ")
        m=(['BELGIUM', 'NETHERLANDS', 'GERMANY', 'SWITZERLAND', 'AUSTRIA'])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)
        
        


    elif selection=="AUSTRIA":
        print("your country are as follow ")
        m=(['BELGIUM', 'NETHERLANDS', 'GERMANY', 'SWITZERLAND', 'CZECHIA'])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)

    else:
        print("INVALID INPUT ")
        


    
    
if start.lower()=="b":
    print("\n for 29 Nights and 30 Days your countries are as \n ", n29)
    
    #for 29 nights and 30 days 

    print("select the countries from  ", selection29)
    selection=input(" select country you want to eliminate ") 

    if selection=="BELGIUM":
        print("your countries are as follows ")
        m=([ 'LUXEMBOURG','NETHERLANDS','GERMANY','HUNGARY','SWITZERLAND','CZECHIA','ITALY','AUSTRIA',])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)

    elif selection=="LUXEMBOURG":
        print("your countries are as follows ")
        m=([ 'BELGIUM','NETHERLANDS','GERMANY','HUNGARY','SWITZERLAND','CZECHIA','ITALY','AUSTRIA',])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)
        

    elif selection=="NETHERLANDS":
        print("your countries are as follows ")
        m=([ 'BELGIUM','LUXEMBOURG','GERMANY','HUNGARY','SWITZERLAND','CZECHIA','ITALY','AUSTRIA',])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)
        

    elif selection=="GERMANY":
        print("your countries are as follows ")
        m=([ 'BELGIUM','LUXEMBOURG','NETHERLANDS','HUNGARY','SWITZERLAND','CZECHIA','ITALY','AUSTRIA',])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)
        

    elif selection=="HUNGARY":
        print("your countries are as follows ")
        m=([ 'BELGIUM','LUXEMBOURG','NETHERLANDS','GERMANY','SWITZERLAND','CZECHIA','ITALY','AUSTRIA',])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)
        

    elif selection=="SWITZERLAND":
        print("your countries are as follows ")
        m=([ 'BELGIUM','LUXEMBOURG','NETHERLANDS','GERMANY','HUNGARY','CZECHIA','ITALY','AUSTRIA',])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)
        

    elif selection=="CZECHIA":
        print("your countries are as follows ")
        m=([ 'BELGIUM','LUXEMBOURG','NETHERLANDS','GERMANY','HUNGARY','SWITZERLAND','ITALY','AUSTRIA',])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)
        

    elif selection=="ITALY":
        print("your countries are as follows ")
        m=([ 'BELGIUM','LUXEMBOURG','NETHERLANDS','GERMANY','HUNGARY','SWITZERLAND','CZECHIA','AUSTRIA',])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)
        

    elif selection=="AUSTRIA":
        print("your countries are as follows ")
        m=([ 'BELGIUM','LUXEMBOURG','NETHERLANDS','GERMANY','HUNGARY','SWITZERLAND','CZECHIA','ITALY',])
        m.append(k)
        m.append(f)
        print(m)
        printmap(m, df2)
        


    else:
        print("INVALID INPUT ")

    
elif start.lower()=="c":
    print("\n for 39 Nights and 40 Days our countries are as \n ", n39 )
    #for 39 nights 40days    
    print("select the countries from  ", n39)
    m.append(k)
    m.append(f)
    m= df2.COUNTRY.unique()

    printmap(m, df2)
    
else :
    print("invalid input")
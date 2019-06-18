#cell 0
import plotly.plotly as py
import pandas as pd
import plotly


#cell 1
plotly.tools.set_credentials_file(username='qwerty03', api_key='zalzm7bui9')

#cell 2
# Africa

#cell 3
df = pd.read_csv('africa_pneumonia.csv')

data1 =  dict(
        type = 'choropleth',
        locations = df['ISO_Code'],
        z = df['Pneumonia'],
        text = df['CountryName'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        name = 'pneumonia',
        marker = dict(
            line = dict (
                color = 'rgb(220,220,0)',
                width = 1.0
            ) ),
        
      ) 

#cell 4
# Asia

#cell 5
df1 = pd.read_csv('asia_preterm.csv')

data2 =  dict(
        type = 'choropleth',
        locations = df1['ISO_Code'],
        z = df1['Preterm'],
        text = df1['CountryName'],
        colorscale = [[0,"rgb(172, 10, 5)"],[0.35,"rgb(190, 60, 40)"],[0.5,"rgb(245, 100, 70)"],\
            [0.6,"rgb(245, 120, 90)"],[0.7,"rgb(247, 137, 106)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(0,0,0)',
                width = 1.0
            ) ),
       
      ) 

#cell 6
# Europe

#cell 7
df2 = pd.read_csv('europe_congenital.csv')

data3 =  dict(
        type = 'choropleth',
        locations = df2['ISO_Code'],
        z = df2['Congenital'],
        text = df2['CountryName'],
        colorscale = [[0,"rgb(5, 172, 10)"],[0.35,"rgb(40, 190, 60)"],[0.5,"rgb(70, 245, 100)"],\
            [0.6,"rgb(90, 245, 120)"],[0.7,"rgb(106, 247, 137)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(220,0,0)',
                width = 1.0
            ) )
      ) 

#cell 8
# North America

#cell 9
df3 = pd.read_csv('north_america_preterm.csv')

data4 =  dict(
        type = 'choropleth',
        locations = df3['ISO_Code'],
        z = df3['Preterm'],
        text = df3['CountryName'],
        colorscale = [[0,"rgb(172, 10, 5)"],[0.35,"rgb(190, 60, 40)"],[0.5,"rgb(245, 100, 70)"],\
            [0.6,"rgb(245, 120, 90)"],[0.7,"rgb(247, 137, 106)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(0,0,0)',
                width = 1.0
            ) ),
        
      ) 

#cell 10
# South America

#cell 11
df4 = pd.read_csv('south_america_congenital.csv')

data5 = dict(
        type = 'choropleth',
        locations = df4['ISO_Code'],
        z = df4['Congenital'],
        text = df4['CountryName'],
        colorscale = [[0,"rgb(5, 172, 10)"],[0.35,"rgb(40, 220, 60)"],[0.5,"rgb(70, 245, 100)"],\
            [0.6,"rgb(90, 245, 120)"],[0.7,"rgb(106, 247, 137)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(220,0,0)',
                width = 1.0
            ) ),
        
      ) 

#cell 12
layout = dict(
    title = 'Overall representation of the unicef-data for under 5 death due to cause',
    geo = dict(
        showlegend=True,
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'albers'
        )
    )
)


fig = dict( data=[data1,data2,data3,data4,data5], layout=layout )


#cell 13
# Red : Preterm
# Green : Congenital
# Blue : Pneumonia

#cell 14
py.iplot( fig, validate=False, filename='d3-world-map' )


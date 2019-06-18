#cell 0
import pandas as pd
import plotly.plotly as py
import plotly
import plotly.graph_objs as go

#cell 1
plotly.tools.set_credentials_file(username='qwerty03', api_key='5aa2fn7kfo')

#cell 2
Congenital = pd.read_csv('Congenital_top30.csv')
Congenital['Congenital1'] = Congenital['Congenital ']
Congenital_formatted = Congenital[['CountryName','Congenital1']]
Congenital_formatted

#cell 3
country = list(Congenital_formatted.CountryName)
Congenital_top_30 = list(Congenital_formatted.Congenital1)

trace0 = go.Scatter(
    x = Congenital_top_30,
    y = country,
    mode = 'markers',
    name = 'Percentage values',
    marker=dict(
        color='rgb(156, 165, 196)',
        line=dict(
            color='rgba(156, 165, 196, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=10,
    )
)
'''
trace1 = go.Scatter(
    x=71.2,
    y=Macedonia,
    mode='markers',
    name='Percent of estimated registered voters',
    marker=dict(
        color='rgba(204, 204, 204, 0.95)',
        line=dict(
            color='rgba(217, 217, 217, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=16,
    )
)
'''
#data = [trace0, trace1]
data = [trace0]

layout = go.Layout(
    title="Cause of death due to Congenital in the first month of life",
    xaxis=dict(
        showgrid=True,
        showline=True,
        linecolor='rgb(102, 102, 102)',
        titlefont=dict(
            color='rgb(204, 204, 204)'
        ),
        tickfont=dict(
            color='rgb(102, 102, 102)',
        ),
        autotick=False,
        dtick=10,
        ticks='outside',
        tickcolor='rgb(102, 102, 102)',
    ),
    margin=dict(
        l=140,
        r=40,
        b=50,
        t=80
    ),
    legend=dict(
        font=dict(
            size=10,
        ),
        yanchor='middle',
        xanchor='right',
    ),
    width=810,
    height=800,
    paper_bgcolor='rgb(254, 247, 234)',
    plot_bgcolor='rgb(254, 247, 234)',
    hovermode='closest',
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Top_30_countries_Congenital')

#cell 4



#cell 0
import pandas as pd
import plotly.plotly as py
import plotly
import plotly.graph_objs as go


#cell 1
plotly.tools.set_credentials_file(username='qwerty03', api_key='5aa2fn7kfo')

#cell 2
preterm = pd.read_csv('Preterm_top30.csv')
preterm['Preterm1'] = preterm['Preterm ']
preterm_formatted = preterm[['CountryName','Preterm1']]
#preterm_formatted

#cell 3
country = list(preterm_formatted.CountryName)
preterm_top_30 = list(preterm_formatted.Preterm1)

trace0 = go.Scatter(
    x = preterm_top_30,
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
    title="Cause of death due to Preterm in the first month of life",
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
py.iplot(fig, filename='Top_30_countries_preterm')

#cell 4


#cell 5



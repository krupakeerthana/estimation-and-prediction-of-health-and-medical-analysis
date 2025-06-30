import plotly.express as px

def line_chart(df, x, y, title):
    return px.line(df, x=x, y=y, title=title)

from dash import Dash, html, dcc, callback, Output, Input

app= Dash(__name__)

app.layout = html.H1("My dash app")


my_H1= html.H1(Chiildren="My dash application")
my_H12= html.H2(Chiildren="More info ...")
my_dropdown= dcc.Dropdown(option=["Apple", "Päron", "Apelsin"], value="Päron")
app.layout= html.Div(children=[my_H1, my_H2, my_dropdown])

@callback (
Output(my_H2, component_property="children"),
Input(my_dropdown, component_property= "Vaue")

)
def update_heading2(fruit):
    return fruit.upper()
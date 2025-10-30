from dash import Dash, html, dcc
import plotly.express as px

# Crear datos y gráfico
data = {
    "Departamento": ["Antioquia", "Cundinamarca", "Valle del Cauca", "Atlántico"],
    "Muertes": [12000, 9500, 8800, 6200]
}
fig = px.bar(data, x="Departamento", y="Muertes", title="Mortalidad por departamento - 2019")

# Crear la aplicación Dash
app = Dash(__name__)

# Diseño de la app
app.layout = html.Div([
    html.H1("Análisis de Mortalidad 2019"),
    dcc.Graph(figure=fig)
])

# Ejecutar el servidor local
if __name__ == "__main__":
    app.run(debug=True)

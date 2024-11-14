from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import layout
from bokeh.models import Slider

# Créer des données initiales
x = [x * 0.1 for x in range(0, 100)]
y = [0] * len(x)
source = ColumnDataSource(data={'x': x, 'y': y})

# Créer une figure Bokeh
plot = figure(title="Application Bokeh interactive", x_axis_label="x", y_axis_label="y")
plot.line('x', 'y', source=source)

# Créer un slider pour interagir avec le graphique
slider = Slider(start=0, end=10, value=1, step=0.1, title="Facteur multiplicatif")

# Définir la fonction de callback pour mettre à jour les données
def update_data(attr, old, new):
    factor = slider.value
    new_y = [factor * val for val in x]
    source.data = {'x': x, 'y': new_y}

# Associer le callback au slider
slider.on_change('value', update_data)

# Organiser la mise en page
app_layout = layout([[plot], [slider]])

# Ajouter la mise en page au document Bokeh
curdoc().add_root(app_layout)

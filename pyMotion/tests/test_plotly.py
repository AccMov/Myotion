import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure, Scatter
import plotly
import numpy as np
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
    QWidget)
from PySide6.QtWebEngineWidgets import QWebEngineView


# Create data frame. Preprocessing done in previous steps
data = {
    "id": (["Results.GA.PP001"] * 10 + ["Results.GA.PP002"] * 10 + ["Results.GA.PP003"] * 10 +
           ["Results.GA.PP004"] * 10 + ["Results.GA.PP005"] * 10 + ["Results.GA.PP006"] * 10 +
           ["Results.GA.PP007"] * 10 + ["Results.GA.PP008"] * 10 + ["Results.GB.PP001"] * 10 +
           ["Results.GB.PP002"] * 10 + ["Results.GB.PP003"] * 10 + ["Results.GB.PP004"] * 10 +
           ["Results.GB.PP005"] * 10 + ["Results.GB.PP006"] * 10 + ["Results.GB.PP007"] * 10 +
           ["Results.GB.PP008"] * 10 + ["Results.GB.PP009"] * 10),
    "muscle": (["ES", "MF", "GMed", "BF", "LGM", "RA", "EO", "TFL", "RF", "TA"] * 17),
    "parameter": ["BPt"] * 170,
    "value": [ 4.469166e-07, 6.583348e-07, 5.740654e-08, 6.484783e-08, 5.384977e-08, 3.638348e-07, 5.754989e-09, 4.248578e-09, 2.185613e-07,
                                5.241972e-07, 2.268811e-06, 6.274575e-07, 1.086097e-07, 1.706187e-07, 5.069020e-07, 3.857862e-08, 1.890864e-08, 1.293974e-07,
                                5.689619e-07, 1.558139e-06, 9.050177e-07, 1.145185e-06, 1.266315e-07, 3.201826e-07, 1.271385e-07, 4.013045e-08, 5.738738e-08,
                                5.049442e-08, 1.074182e-06, 9.184853e-07, 8.113003e-07, 7.676527e-07, 7.010750e-08, 3.257138e-07, 3.662326e-08, 3.477464e-08,
                                7.033389e-08, 4.004842e-07, 6.933911e-07, 4.278812e-07, 9.247114e-07, 6.954120e-07, 1.459336e-07, 1.806641e-07, 5.055805e-08,
                                2.035285e-08, 4.775317e-08, 5.625635e-08, 1.383005e-06, 8.819423e-07, 2.256283e-06, 1.512067e-06, 1.108409e-06, 1.309409e-06,
                                3.981629e-08, 5.853301e-09, 3.367703e-07, 1.678200e-07, 2.064621e-06, 1.780348e-06, 9.845964e-08, 1.187423e-07, 1.517121e-07,
                                8.417073e-08, 2.703044e-07, 2.941639e-08, 4.191524e-07, 3.737571e-08, 3.812797e-07, 3.163391e-06, 6.549323e-07, 2.415388e-06,
                                1.442509e-07, 5.214906e-07, 3.849112e-08, 5.720157e-08, 2.560452e-07, 6.233906e-08, 6.474735e-07, 4.432808e-06, 2.331585e-07,
                                4.705611e-07, 1.847827e-07, 1.883050e-07, 7.537713e-08, 2.846701e-09, 4.011989e-08, 9.432575e-09, 1.137580e-07, 7.934226e-07,
                                1.434555e-06, 9.396479e-07, 6.494298e-07, 5.174247e-07, 6.272057e-07, 2.086906e-07, 7.491827e-07, 1.211449e-06, 2.010589e-06,
                                2.265188e-06, 6.334077e-07, 2.884018e-07, 1.241120e-07, 1.825970e-08, 9.313346e-08, 1.613434e-08, 5.981950e-08, 8.462454e-08,
                                7.039528e-07, 6.219591e-08, 1.694533e-06, 3.109434e-06, 1.552465e-06, 2.518240e-07, 3.267983e-07, 9.143998e-06, 1.703820e-07,
                                3.644231e-08, 1.567843e-06, 2.008024e-06, 9.522492e-07, 1.565636e-06, 5.588759e-07, 1.559126e-07, 8.743837e-07, 4.162157e-07,
                                1.178549e-07, 2.894992e-08, 1.813097e-06, 2.529496e-06, 7.946084e-07, 2.792359e-06, 6.275212e-08, 3.291227e-07, 1.423837e-06,
                                5.413372e-07, 7.589750e-07, 8.796217e-08, 1.030376e-06, 1.023613e-06, 3.846267e-06, 2.150267e-06, 8.746650e-07, 2.135793e-06,
                                1.307326e-07, 2.663247e-07, 1.709225e-07, 2.279045e-07, 7.997134e-06, 1.463845e-06, 8.111867e-07, 1.261161e-06, 3.062190e-07,
                                2.116192e-07, 2.075226e-06, 7.541255e-09, 8.439026e-09, 1.100311e-07, 7.902747e-07, 1.652975e-06, 4.047867e-07, 2.987185e-07,
                                4.296497e-07, 5.961347e-07, 2.112224e-07, 4.325762e-09, 1.402427e-07, 6.537959e-07, 4.659321e-07, 9.827920e-07],  # Replace with your values
    "group": (["GroupA"] * 80 + ["GroupB"] * 90)
}

df_draw = pd.DataFrame(data)

# Calculate the mean values
df_bar = df_draw.groupby(["group", "muscle"])["value"].mean().reset_index()

# Make GroupA values negative (for bi-direction bar plot)
df_bar.loc[df_bar["group"] == "GroupA", "value"] *= -1

### plotly code
df_bar['abs_value'] = abs(df_bar['value'])

fig = px.bar(
    df_bar,
    x="value",
    y="muscle",
    color="group",
    barmode="relative",
    title="Bar Plot of parameter BPt by Muscle",
    labels={"value": "Value", "muscle": "Muscle", "group": "Group"},
    color_discrete_sequence=['#1f77b4', '#ff7f0e'],
)

# calculate the maximum absolute value in the data, for the range of xaixs
max_abs_value = max(abs(df_bar["value"]))

# x-axis
custom_tick_values = [-2 * max_abs_value, -max_abs_value, 0, max_abs_value, 2 * max_abs_value]
custom_tick_text = [str(abs(x)) for x in custom_tick_values]

# plot layout
fig.update_layout(
    xaxis=dict(
        title="Parameter(BPt) values",  # x name
        tickvals=custom_tick_values,
        ticktext=custom_tick_text,
        range=[-2.2 * max_abs_value, 2.2 * max_abs_value],  # Extend the range to accommodate ticks
    ),
    yaxis=dict(
        title="Muscles",  # y name
    ),
    legend=dict(
        title="Group",
    ),
    plot_bgcolor="white",  # No background
    margin=dict(l=80, r=20, t=50, b=50),
    font=dict(family="Arial", size=12),  # font size (one can just zoom in if open with browser)
)

# adjust trace
fig.update_traces(
    marker=dict(
        line=dict(
            width=1,  # marker line width
        ),
    ),
)

# Adjust hover information
fig.update_traces(
    hovertemplate="%{y}: %{customdata[0]}",
    customdata=df_bar[['abs_value']].to_numpy(),
    showlegend=True,  # Show legend in the hover label
)


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()

        # we create html code of the figure
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></ html>'

        # we create an instance of QWebEngineView and set the html code
        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        # set the QWebEngineView instance as main widget
        self.setCentralWidget(plot_widget)

# run plot as html
#fig.show()
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

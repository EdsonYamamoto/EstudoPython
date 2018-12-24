
import plotly as py
import plotly.graph_objs as go
import numpy as np

class TestPlotly:

    def PlotlyPrinc(self):
        print("[0] Plotly Test 1")
        teste = input()
        if teste is "0":
            TestPlotly.PlotlyTeste(object)

    def PlotlyTeste(self):
        print("Executando teste")

        # Create random data with numpy

        N = 1000
        random_x = np.random.randn(N)
        random_y = np.random.randn(N)

        # Create a trace
        trace = go.Scatter(
            x = random_x,
            y = random_y,
            mode = 'markers'
        )

        data = [trace]

        # Plot and embed in ipython notebook!
        py.plot(data, filename='basic-scatter')

        # or plot with: plot_url = py.plot(data, filename='basic-line')
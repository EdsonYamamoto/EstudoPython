from Person import Person
from Controller import Controller
from MachineLearning import MachineLearning
from TestesModulos.testPlotly import TestPlotly
from TestesModulos.testMatPlotLib import TestMatPlotLib
from TestesModulos.testPandas import TestPandas
from TestesModulos.testSeaborn import TestSeaborn
from TestesModulos.testOpenCV import TestOpenCV

class main:
    print("Starting")
    print("__name__ value: ", __name__)

    if __name__ == '__main__':

        print("[0] Teste com classe")
        print("[1] Invocando metodo")
        print("[2] machine learning")
        print("[3] matplotlib")
        print("[4] plotly")
        print("[5] pandas")
        print("[6] seaborn")
        print("[7] Open CV")

        print("Comando ")
        operacao = input()

        if operacao is '0':
            Controller.mainMet1(object)

        if operacao is '1':
            p1 = Person("John", 36)
            print(p1.name)
            print(p1.age)

        if operacao is '2':
            MachineLearning.DataSet(object)

        if operacao is '3':
            TestMatPlotLib.MatPlotLibPrinc(object)

        if operacao is '4':
            TestPlotly.PlotlyPrinc(object)

        if operacao is '5':
            TestPandas.PandasPrinc(object)

        if operacao is '6':
            TestSeaborn.SeabornPrinc(object)

        if operacao is '7':
            TestOpenCV.OpenCVPrinc(object)


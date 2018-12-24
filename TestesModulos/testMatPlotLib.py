import matplotlib.pyplot as plt
import numpy as np

class TestMatPlotLib:

    def MatPlotLibPrinc(self):
        print('Mat plot lib')
        print("[1] grafico simples")
        print("[2] grafico duplo")
        print("[3] grafico dentro doutro")

        teste = input()
        if teste is '1':
            TestMatPlotLib.Teste1(object)
        if teste is '2':
            TestMatPlotLib.Teste2(object)
        if teste is '3':
            TestMatPlotLib.Teste3(object)

    def Teste1(self):
        print("Executando")

        x = np.linspace(0,5,11)
        y = x *x
        plt.subplot(1,2,1)
        plt.plot(x,y, 'r--')
        plt.show()

    def Teste2(self):
        print("Executando")

        x = np.linspace(0,5,11)
        y = x *x

        plt.subplot(1,2,1)
        plt.plot(x,y, 'r--')

        plt.xlabel('Eixo1 X')
        plt.ylabel('Eixo1 Y')

        plt.subplot(1,2,2)
        plt.plot(y,x, 'g*-')

        plt.xlabel('Eixo2 X')
        plt.ylabel('Eixo2 Y')
        plt.show()

    def Teste3(self):
        print("Executando")

        x = np.linspace(0,5,11)

        y = x *x

        plt.subplot(1,2,1)
        plt.plot(x,y, 'r--')

        plt.subplot(1,2,2)
        plt.plot(y, x, 'g*-')

        fig = plt.figure()
        axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
        axes2 = fig.add_axes([0.2,0.5,0.3,0.3])
        axes1.set_xlabel('Eixo X')
        axes1.set_title('Titulo')

        axes1.plot(x,y)
        axes2.plot(y,x)

        fig.show()

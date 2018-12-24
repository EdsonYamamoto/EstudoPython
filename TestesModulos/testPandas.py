
import pandas as pd
import numpy as np

class TestPandas:
    def PandasPrinc(self):
        print('[0] Pandas Test')
        teste = input()

        if teste is '0':
            TestPandas.Teste1(object)

    def Teste1(self):
        print("Executando teste")
        labels = ['a','b','c']

        minha_lista = [10,20,30]
        arr = np.array([10,20,30])
        d = {'a':10, 'b':20, 'c':30}

        resp = pd.Series(minha_lista, labels)

        print(resp)

        resp = pd.Series(arr,labels)

        print(resp)

        ser = pd.Series([1,2,3,4], index=['EUA','Alemanha','URSS','Japao'])
        print (ser)
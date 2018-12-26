from sinesp_client import SinespClient

class TestSinesp:
    def SinespPrinc(self):
        print('[0] sinesp Test')
        teste = input()

        if teste is '0':
            TestSinesp.Teste1(object)

    def Teste1(self):
        print("Digite placa do carro")
        placa = input()
        sc = SinespClient()
        result = sc.search(placa)
        print(result)
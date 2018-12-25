from sinesp_client import SinespClient

class TestSinesp:
    def SinespPrinc(self):
        print('[0] sinesp Test')
        teste = input()

        if teste is '0':
            TestSinesp.Teste1(object)

    def Teste1(self):
        sc = SinespClient()
        result = sc.search('EYB2903')
        print(result)
from pymongo import MongoClient

class TestPymongo:

    def PymongoTest(self):
        print("[0]Inputar dados")
        teste = input()
        if teste is '0':
            TestPymongo.InputarDados(object)

    def InputarDados(self):
        stringConnection = 'mongodb://mongodb-stitch-asd-fchmh:Facens081368!@' \
                           'edsontestemongodb-shard-00-00-4bp1k.mongodb.net:27017,' \
                           'edsontestemongodb-shard-00-01-4bp1k.mongodb.net:27017,' \
                           'edsontestemongodb-shard-00-02-4bp1k.mongodb.net:27017/' \
                           'test?ssl=true&replicaSet=EdsonTesteMongoDB-shard-0&authSource=admin&retryWrites=true'
        Client = MongoClient(stringConnection)
        db = Client['CameraSeguranca']
        collection = db['Carros']
        carro = {'for':1}

        x = collection.insert(carro)

        print(x)
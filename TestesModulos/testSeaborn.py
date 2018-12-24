import seaborn as sns
import matplotlib.pyplot as plt

class TestSeaborn:

    def SeabornPrinc(self):
        print("Test Seaborn 1")
        print('[0] teste')
        teste = input()
        if teste is '0':
            TestSeaborn.Teste1(object)

    def Teste1(self):
        print("Executando")

        tips = sns.load_dataset('tips')
        tips.head()

        sns.distplot(tips['total_bill'], kde=False, bins=50)
        plt.show()

        sns.jointplot(x='total_bill', y='tip', data = tips, kind='reg')
        plt.show()

        sns.jointplot(x='total_bill', y='tip', data = tips, kind='hex')
        plt.show()

        sns.pairplot(tips)
        plt.show()

        sns.pairplot(tips, hue="sex")
        plt.show()


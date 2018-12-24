from sklearn import datasets
from sklearn import svm
import pickle


class MachineLearning:

    def DataSet(self):
        print('data')
        iris = datasets.load_iris()
        digits = datasets.load_digits()

        #print(iris)
        #print(digits)

        clf = svm.SVC(gamma=0.001, C=100.)


        print(clf)

        clf.fit(digits.data[:-1], digits.target[:-1])

        clf.predict(digits.data[-1:])

        s = pickle.dumps(clf)
        clf2 = pickle.loads(s)
        clf2.predict(X[0:1])
        y[0]


    def __init__(self):
        print("Executando load dataset")

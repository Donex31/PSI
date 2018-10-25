import numpy

class Perceptron(object):

    '''siec perceptronu'''
    def __init__(self, input_size, learning_rate = 1, epochs = 3):
        self.Weights = numpy.zeros(input_size+1)
        self.epochs = epochs
        self.learning_rate = learning_rate

    '''funkcja aktywacyjna'''
    def activation(self, x):
        return 1 if x>=0 else 0

    '''wyliczanie wyniku'''
    def predict(self, x):
        x = numpy.insert(x, 0, 1)
        z = self.Weights.T.dot(x)
        a = self.activation(z)
        return a

    '''uczenie perceptronu'''
    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = numpy.insert(X[i], 0, 1)
                e = d[i] - self.predict(X[i])
                #print(e)
                self.Weights= self.Weights+self.learning_rate * e * x


if __name__ == '__main__':

    '''Dane uczace'''
    X = numpy.array([[0,0], [0,1], [1,0], [1,1]])
    d = numpy.array([0, 1, 1, 1])

    #X = numpy.array([[0, 0], [0, 1], [1, 0]])
    #d = numpy.array([0, 1, 1])

    #X = numpy.array([[0, 0], [0, 1]])
    #d = numpy.array([0, 1])

    #X = numpy.array([[0, 0]])
    #d = numpy.array([0])

    #X = numpy.array([[0,1], [0,0], [1,1], [1,0], [0,0], [0,1]])
    #d = numpy.array([1, 0, 1, 1, 0, 1])

    '''Dane Testowe'''
    Y = numpy.array([[0,0], [0,1], [1,0], [1,1]])
    #Y = numpy.array([[0,1]])
    #Y = numpy.array([[0,1], [0,0]])
    #Y = numpy.array([[0,1], [0,0], [1,1], [1,0], [0,0], [0,1], [1,1]])

    perceptron = Perceptron(input_size=2)
    perceptron.fit(X, d)
    #print(perceptron.Weights)# wyswietlenie wag

    for i in range(Y.shape[0]):
        print (perceptron.predict(Y[i]))#wyświetlanie wyników
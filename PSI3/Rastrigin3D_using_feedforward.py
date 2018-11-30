import neurolab as nl
import Rastrigin3D as R3D
import pylab as pl

if __name__ == '__main__':
    '''Tworzenie sieci'''
    min, max, xrange = [-2, 2, 500]
    # X,Y = R3D.np.asarray(R3D.make_data(min,max,xrange))

    val = R3D.np.linspace(min, max, xrange)
    target = [0] * xrange
    for a in range(0,xrange):
        target[a]=[R3D.rastrigin(val[a])]

    input = [0] * xrange
    for a in range(0,xrange):
        input[a]=[val[a]]

    # input=[xrange*[0]]*xrange
    # for a in range(0, xrange):
    # for b in range(0, xrange):
    #    input[a] = [X[a][b],Y[a][b]]
    # input = R3D.np.asarray(input)
    # target = [0]*xrange
    # for a in range(0,xrange):
    # target[a]=[R3D.rastrigin(input[a][0],input[a][1])]

    net = nl.net.newff([[min, max]] ,[20,20, 1])
    net.trainf = nl.train.train_gdm
    error = net.train(input, target, epochs=2000, show = 100, lr=0.0001,mc = 0.1)
    out = net.sim(input)

    print(out)

    pl.plot(out)
    pl.xlabel('Epoch number')
    pl.ylabel('Train error')
    pl.grid()
    pl.show()


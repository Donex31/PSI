import neurolab as nl
import pylab as pl
import Data

'''Tworzenie sieci'''
net = nl.net.newp(Data.GetStart(),1)

'''Uczenie sieci'''
error = net.train(Data.GetInput(),Data.GetTarget(),epochs=500,show = 100, lr=0.001)

'''Testowanie seci'''
out = net.sim(Data.test['A'])
print(out[0][0])
if out[0][0]==0:
    print('Mala litera')
else:
    print('Wielka litera')


'''Tworznie wykresy'''
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('Train error')
pl.grid()
pl.show()


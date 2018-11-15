import neurolab as nl
import pylab as pl
import Data

'''Tworzenie sieci'''
size = [1]
net = nl.net.newff(Data.GetStart(),size)

'''Uczenie sieci'''
net.trainf = nl.train.train_gd
error = net.train(Data.GetInput(),Data.GetTarget(),epochs=500,show = 100, lr=0.1)

'''Testowanie seci'''
out = net.sim(Data.test['A'])
print(out[0][0])
if round(out[0][0])==0:
    print('Mala litera')
else:
    print('Wielka litera')

print()
'''Tworznie wykresy'''
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel('Train error')
pl.grid()
pl.show()


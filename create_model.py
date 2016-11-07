import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten, Dropout, Activation, Convolution2D, Reshape
from keras.layers.advanced_activations import ELU

from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import random
import sys

#wave = open('wavnp31.txt').read()
#print(len(wave))

#Due to time constraints, we only trained on one model to get a proof of concept going.
with open('wavnp31.txt') as f:
    wave = [tuple(map(float, i.split(' '))) for i in f]

print("corpus length of tuples:",len(wave))

#Parameters
wavlen = len(wave)
maxlen = 100
step = 15

sequences = []
next_sample = []

seq_index =  dict((c,i) for i, c in enumerate(wave))
op_seq_index = dict((i,c) for i, c in enumerate(wave))

#Separated the music/wave frequenies into cuts of sequences
for i in range(0, len(wave) - maxlen,step):
	sequences.append(wave[i:i+maxlen])
	next_sample.append(wave[i+maxlen])
	
print(len(sequences))

#X = nth of the sequence
#Y = n+1th of the sequence
X = np.zeros((len(sequences), maxlen, len(wave)), dtype=np.bool)
y = np.zeros((len(sequences), len(wave)), dtype=np.bool)

#create vectors
for i, sequences in enumerate(sequences):
	for j, wave in enumerate(sequences):
		X[i, j, seq_index[wave]] = 1
	y[i, seq_index[next_sample[i]]] = 1


#Model essentially - Training on what's next of the sequence
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, wavlen)))
model.add(Dense(wavlen))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


#Due to time constraints, we were never able to get the prediction fully working 10/24;
#however the model did seem to learn but would've worked better if we trained on mono
#sound instead of stereo
for iteration in range(1,2):
	print("Iteration:",iteration)
	model.fit(X,y,batch_size=128,nb_epoch=1)
	start_index = random.randint(0, wavlen - maxlen -1)	
#	for diversity in [0.2,0.5,1.0,1.2]:
	x_predict = np.zeros(1, maxlen, wavlen)
	for t, wave in enumerate(sequences):
		x_predict[0,t, seq_index[wave]] = 1
	pred = model.predict(x_predict, verbose=0)[0]
	print(pred)

#		next_ind = sample(pred, diversity)
#		next_val = op_seq_index[next_ind]

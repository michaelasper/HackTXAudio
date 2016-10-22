import numpy
from keras.models import Sequential 
from keras.layers import Dense , Dropout, Flatten
from keras.layers import LSTM
from keras.utils import np_utils
from keras.layers.convolutional import Convolution2D, MaxPooling2D


#read data for x
datagen =  ImageDataGenerator(rescale = 1./255)
image_from_dir = datagen.flow_from_directory('train', target_size = (512,512))

#split data for testing and training 
#[samples, time steps, feautres]
#normalize x  

model = Sequential()


model.add(Convolution2D(128,5,5, border_mode='same', input_shape=(3,512,512)))

#model.add(Flatten())
model.add(Dense())
model.add(Dropout(0.3))
#model.add(Permute())
model.add(LSTM(32, return_sequences=True))
model.fit_generator(image_from_dir, sample_per_epoch=10, nb_epoch=50) 
#return sequences set to true 


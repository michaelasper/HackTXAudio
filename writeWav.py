import scipy.io.wavfile;

#Preprocessing the data
#We have all the wavFiles to numpy arrays for us to
#preprocess on multiple computers while we trained
#on the much faster computer at the time

def convertNumpyToWavFile(filename, rate, data):
    wavfile.write(filename, rate, data);

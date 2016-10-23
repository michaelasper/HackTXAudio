import scipy.io.wavfile;

def convertNumpyToWavFile(filename, rate, data):
    wavfile.write(filename, rate, data);
from pydub import AudioSegment
import stft
import scipy.io.wavfile as wav
import numpy as np
from numpy.lib import stride_tricks
np.set_printoptions(threshold=np.inf)

#
# def stft(sig, frameSize, overlapFac=0.5, window=np.hanning):
#     win = window(frameSize)
#     hopSize = int(frameSize - np.floor(overlapFac * frameSize))
#
#     # zeros at beginning (thus center of 1st window should be for sample nr. 0)
#     samples = np.append(np.zeros(np.floor(frameSize/2.0)), sig)
#     # cols for windowing
#     cols = np.ceil( (len(samples) - frameSize) / float(hopSize)) + 1
#     # zeros at end (thus samples can be fully covered by frames)
#     samples = np.append(samples, np.zeros(frameSize))
#
#     frames = stride_tricks.as_strided(samples, shape=(cols, frameSize), strides=(samples.strides[0]*hopSize, samples.strides[0])).copy()
#     frames *= win
#     #print(np.fft.rfft(frames))
#     return np.fft.rfft(frames)


sound = AudioSegment.from_mp3("Monkey_Warhol_-_01_-_Everything_Starts_with_an_E.mp3")
sound.export("song1.wav", format="wav")
f, audio = wav.read("song1.wav")
specgram = stft.spectrogram(audio)
# s, audio = wav.read("song1.wav")
# spectrogram = stft(audio, 1024)
spectram = open("specinfo.txt", "w+")
spectram.write(str(specgram))
spectram.close()

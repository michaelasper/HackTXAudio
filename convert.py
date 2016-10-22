from pydub import AudioSegment
import stft
import scipy.io.wavfile as wav

sound = AudioSegment.from_mp3("Monkey_Warhol_-_01_-_Everything_Starts_with_an_E.mp3")
sound.export("song1.wav", format="wav")

fs,audio = wav.read('song1.wav')

specgram = stft.spectrogram(audio)

print(specgram)
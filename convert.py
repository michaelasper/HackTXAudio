from pydub import AudioSegment
sound = AudioSegment.from_mp3("Monkey_Warhol_-_01_-_Everything_Starts_with_an_E.mp3")
sound.export("song1", format="wav")
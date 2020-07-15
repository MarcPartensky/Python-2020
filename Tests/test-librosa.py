import librosa
y, sr = librosa.load("you're a dumb mother fucker", sr=16000) # y is a numpy array of the wav file, sr = sample rate
y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=4) # shifted by 4 half steps



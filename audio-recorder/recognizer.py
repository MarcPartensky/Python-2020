import speech_recognition as sr
r = sr.Recognizer()

test = sr.AudioFile('test.wav')
with test as source:
    audio = r.record(source)

result = r.recognize_google(audio)

print(result)

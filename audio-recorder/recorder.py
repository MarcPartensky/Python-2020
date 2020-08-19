import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)


def record():
    with mic as source:
        audio = r.listen(source)
    return r.recognize_google(audio, language='fr-FR')

result = record()
print(result)


if result.startswith('quels sont mes micros'):
    print(sr.Microphone.list_microphone_names())

if result.startswith('website'):
    import os
    os.system('code /Users/marcpartensky/programs/website')


print(os.listdir())

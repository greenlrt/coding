import speech_recognition as sr

r = sr.Recognizer()

stream = sr.AudioFile('stream.wav')

with stream as source:
        r.adjust_for_ambient_noise(source)
	audio = r.record(source)

text = r.recognize_google(audio)

print(text)

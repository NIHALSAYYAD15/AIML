import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic)
    recognizer.dynamic_energy_threshold = True
    print("Listening...")
    audio = recognizer.listen(mic)        
    print("Recording stopped")
    try:
        print("Audio is converting to text Please wait...")
        text = recognizer.recognize_google(audio, language='us-in').lower()
        print("Recognised text -> " + text)
    except Exception as e:
        print(e)
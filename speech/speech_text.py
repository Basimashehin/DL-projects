import speech_recognition as sr
def speech_recog():
    r=sr.Recognizer()
    mic=sr.Microphone()
    while True:
        with mic as source:
            print("speak.................")
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                print("You said ....",text)
            except sr.UnknownValueError:
                print("Didn't hear Anything please repeat.............")


speech_recog()

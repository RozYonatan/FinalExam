import speech_recognition as sr

class STT:

    def __init__(self,audio_data):
        self.recognizer = sr.Recognizer()
        self.audio_data = audio_data
        self.text = ""

    def extract_text(self):
        try:
            self.text = self.recognizer.recognize_google(self.audio_data)
            print(self.text)
            return self.text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"


    def get_text(self):
        return self.text

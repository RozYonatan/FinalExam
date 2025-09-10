from faster_whisper import WhisperModel
import io
class STT:

    model = WhisperModel("base")


    @staticmethod
    def extract_text(audio_file):
       segments, info = STT.model.transcribe(io.BytesIO(audio_file))
       result = ".".join([segment.text for segment in segments])
       print(result)
       return result





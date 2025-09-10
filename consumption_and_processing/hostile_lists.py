import base64
import io

class HostileLists:

    def __init__(self,encoded_hostile = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ"
                 ,encoded_very_hostile="R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT" ):
        self.encoded_hostile = encoded_hostile
        self.encoded_very_hostile = encoded_very_hostile


    def get_decryption_list(self,encoded_string):
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        decoded_string = decoded_string.lower()
        decrypted_list = decoded_string.split(",")
        return decrypted_list

    def get_hostile_list(self):
        return self.get_decryption_list(self.encoded_hostile)

    def get_very_hostile_list(self):
        return self.get_decryption_list(self.encoded_very_hostile)






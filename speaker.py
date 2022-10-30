#Code written for IBM Call for code 2K22 (SwachBin)
from playsound import playsound
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('w9BnLVJn7bNkplaRmatr8qps1RxMbozXN1N68KuS-Pcz')
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/45faaf38-33db-49b9-85a2-37a1a6cac7ae')

var="Thank you for using Swach Bin. "

with open('Voice.wav', 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(var,voice='en-US_AllisonV3Voice',accept='audio/wav').get_result().content)

playsound('/home/pi/CFC/model2/Voice.wav',block=False)
print('playing Voice using speaker')

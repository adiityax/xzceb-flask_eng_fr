import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('el0GCeoL439LCwa-7u-bZ4Tsbn85YN2TJU-TBZ1dBYaR')
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url('https://api.kr-seo.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    translation = language_translator.translate(
        text = english_text,
        model_id = 'en-fr').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    list1 = translation.get('translations')
    french_text = list1[0]['translation']
    return french_text

def french_to_english(french_text):
    translation = language_translator.translate(
        text = french_text,
        model_id = 'fr-en').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    list1 = translation.get('translations')
    english_text = list1[0]['translation']
    return english_text


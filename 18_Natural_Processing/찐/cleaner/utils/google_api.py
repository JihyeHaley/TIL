import requests
import json
import html

URL_GOOGLE_TRANSLATE = 'https://www.googleapis.com/language/translate/v2'
URL_GOOGLE_DETECT = 'https://translation.googleapis.com/language/translate/v2/detect'
GOOGLE_API_KEY = 'AIzaSyAy8QmfwewfLHbt5Ua1L5gGqjdGGZd_7ro'

# logger = Logger.__call__('GConNLP').get_logger()


def google_detect(text_to_detect):
    query_params = {}
    query_params['key'] = GOOGLE_API_KEY
    query_params['q'] = text_to_detect
    google_result = None
    detected_lang = ''
    try:
        google_result = requests.post(URL_GOOGLE_DETECT, data=json.loads(json.dumps(query_params)))
    except Exception as e:
        print(e)
        # logger.info('cannot get result from google error: {}', e)

    if google_result:
        detected_lang = json.loads(google_result.text)['data']['detections'][0][0]['language']
        detected_lang = html.unescape(detected_lang)
    return detected_lang


def google_translate(text_to_translate, source_language_code, target_language_code):
    # logger.info('Start Google Translate ...')
    print('Start Google Translate ...')
    text_list = text_to_translate.split('\n')
    query_params = {'key': GOOGLE_API_KEY, 'source': source_language_code, 'target': target_language_code, 'q': text_list,
                    'model': 'nmt'}
    print(query_params)
    google_result = None
    google_translated = dict.fromkeys(text_list, "")

    try:
        google_result = requests.post(URL_GOOGLE_TRANSLATE, data=json.loads(json.dumps(query_params)))
    except Exception as e:
        print(e)
        # logger.info('cannot get result from google error: {}', e)

    if google_result:
        del google_translated
        google_translated = dict(zip(text_list, [html.unescape(text['translatedText']) for text in
                                                 json.loads(google_result.text)['data']['translations']]))

    print(google_result)
    print(google_translated)

    # logger.info('... Google Translate done')
    return google_translated


if __name__ == "__main__":
    google_translate(
        'The target value is also able to be specified as one of agreed requirements by acquirers and suppliers to specify quality requirements or to examine conformance for acquisition.\nA requirements specification is usually changed and revised during development and affects the quality measures based on it',
        'en', 'ko')

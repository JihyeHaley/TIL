import requests
import json
import html

URL_GOOGLE_TRANSLATE = 'https://www.googleapis.com/language/translate/v2'
URL_GOOGLE_DETECT = 'https://translation.googleapis.com/language/translate/v2/detect'
GOOGLE_API_KEY = 'AIzaSyAy8QmfwewfLHbt5Ua1L5gGqjdGGZd_7ro'

# logger = Logger.__call__('GConNLP').get_logger()

URL_PARSE = 'https://parser.gconstudio.com'
URL_GCON_PARSE = URL_PARSE + '/parse'


def parse_file(file, source_language_code):
    print('Parsing a file ...')
    headers = {'Authorization': 'GPl+nafzlHDTYW7hdI4yZ5ew18JH4JW90'}

    fin = open(file, 'rb')
    files = {'document': fin}
    values = {'source_language_code': source_language_code}
    result = requests.post(URL_GCON_PARSE, data=json.loads(json.dumps(values)), files=files,
                           headers=headers)
    output = json.loads(result.text)
    return output['data']


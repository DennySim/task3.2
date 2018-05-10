from pprint import pprint

import requests
import os.path


def translate_it(text, in_lang, out_lang):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    # key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    key = 'trnsl.1.1.20180508T175323Z.83fa959898aa274d.1cfaf858cffdc77bd24df269b386d4e7845c32e0'


    # Use this for autodetection original language
    #url_lang_detect = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
    #
    # params_post = {
    #     'key': key,
    #     'text': text,
    # }
    #
    # in_lang = requests.post(url_lang_detect, params=params_post).json()
    # lang_list = [in_lang['lang'], out_lang]

    lang_list = [in_lang, out_lang]
    trans = '-'.join(lang_list)

    params = {
        'key': key,
        'lang': trans,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def input_data():
    print('Enter path to a file (ex. c:/1/de.txt)')
    file_path_in = input()
    print('Enter original language (ex. de)')
    in_lang = input()

    return file_path_in, in_lang


def output_data():

    print('Enter path to save a file (ex. c:/1/ru.txt)')
    file_path_out = input()
    print('Enter language to translate to (ex. ru)')
    out_lang = input()
    if out_lang:
        pass
    else:
        out_lang = 'ru'

    return os.path.normcase(file_path_out), out_lang


def translated_text():
    input_data_set = input_data()
    with open(input_data_set[0], encoding='utf-8') as f:
        output_data_set = output_data()
        with open(output_data_set[0], 'w', encoding='utf-8') as ff:
            ff.write(translate_it(f.read(), input_data_set[1], output_data_set[1]))


translated_text()
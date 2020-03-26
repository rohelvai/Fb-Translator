#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: controller.py
# Created: Wednesday, 25th March 2020 4:19:57 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Thursday, 26th March 2020 6:43:30 pm
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

import requests as rq
from googletrans import Translator

# Temp File Based DB
"""
Wish to replace it with sqlite or some other database
The Practice should be avoided
"""
f1 = open('user.txt', 'r')
f2 = open('src.txt', 'r')
f3 = open('dest.txt', 'r')
user = f1.read().split()
src = f2.read().split()
dest = f3.read().split()
f1.close()
f2.close()
f3.close()

# Supported Language List
# Formatted Like a dictionary
lang_list = {
    'Auto': 'auto',
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Arabic': 'ar',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Chinese (Simplified)': 'zh',
    'Chinese (Traditional)': 'zh-TW',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian': 'Creole ht',
    'Hebrew': 'iw',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Khmer': 'km',
    'Korean': 'ko',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Macedonian': 'mk',
    'Malay': 'ms',
    'Maltese': 'mt',
    'Marathi': 'mr',
    'Norwegian': 'no',
    'Persian': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Serbian': 'sr',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Spanish': 'es',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Yiddish': 'yi'
}

# Modifies Files
# Till now I don't know how it works
def filing():
    """
    Should fix this and replace with DB Calls
    """
    f1 = open('user.txt', 'w')
    f2 = open('src.txt', 'w')
    f3 = open('dest.txt', 'w')
    for item in user:
        f1.write("%s\n" % item)
    for item in src:
        f2.write("%s\n" % item)
    for item in dest:
        f3.write("%s\n" % item)
    f1.close()
    f2.close()
    f3.close()

# Maybe Text Encoder
def encode(text):
    """
    Should Fix this
    """
    text = text.title()
    if text == 'Bangla':
        return 'bn'
    for name, code in lang_list.items():
        if name == text:
            return code
    else:
        return 'wrong'

# Text Decoder (Maybe)
def decode(text):
    if text == 'auto':
        return 'Any (Auto Detect)'
    for name, code in lang_list.items():
        if code == text:
            return name

# Welcome Message
def welcome(user_id, name):
    user_id = str(user_id)
    message = 'Hi, {name}. 😉😉😉 \n\nWelcome to TranslatorBot.\n\n' \
                  'Send any sentence to translate.\n\n' \
                  'Send /admin to chat with admin.\n' \
                  'Send /help to get help.\n'.format(name=name)

    if user_id not in user:
        user.append(user_id)
        src.append('auto')
        dest.append('en')
        filing()

    return message + '\n\n\nCurrent translation: \n\n' + 'From: %s\nTo: %s' \
           % (decode(src[user.index(str(user_id))]), decode(dest[user.index(str(user_id))]))

# Gets Current Language
def current_language(user_id):
    if str(user_id) not in user:
        return 'Sorry. 😔😔😔\n\n Please try sending /start once more.'
    return 'Current translation: \n\n' + 'From: %s\nTo: %s' \
           % (decode(src[user.index(str(user_id))]), decode(dest[user.index(str(user_id))]))

# Make Changes to Current Language Choice
def language_change(user_id, message):
    if user_id in user:
        try:
            message = message.split('-')
            print(message)

            if encode(message[0]) != 'wrong' and encode(message[1]) != 'auto' and encode(message[1]) != 'wrong':
                src[user.index(str(user_id))] = encode(message[0])
                dest[user.index(str(user_id))] = encode(message[1])
                text = "Success! 😍😍😍"
                filing()
            else:
                text = 'Sorry. 😔😔😔 Check format and supported languages.' \
                       '(Auto detect can\'t be destination language)'
            return text + '\n\nCurrent translation: \n\n' + 'From: %s\nTo: %s' \
                % (decode(src[user.index(str(user_id))]), decode(dest[user.index(str(user_id))]))
        except Exception as e:
            print(e)
            return "Sorry. 😔😔😔 Something wrong happened.\n" \
                   "Try sending /start once more or " \
                   "check format and supported languages."
    else:
        return 'Sorry. 😔😔😔\nTry sending /start once more.'

# Swaps between Currently Selected Language Choices
def swap_language(user_id):
    if str(user_id) not in user:
        return 'Sorry. 😔😔😔\n\n Please try sending /start once more.'
    try:
        if src[user.index(str(user_id))] == 'auto':
            return 'Sorry. Language swap not possible. Auto detect can\'t be selected as destination language.'
        temp = src[user.index(str(user_id))]
        src[user.index(str(user_id))] = dest[user.index(str(user_id))]
        dest[user.index(str(user_id))] = temp
        filing()
        return 'Success! 😍😍😍\n\nCurrent translation: \n\n' \
               'From: %s\nTo: %s' % (decode(src[user.index(str(user_id))]),
                                     decode(dest[user.index(str(user_id))]))
    except:
        return 'Sorry. 😔😔😔 Something isn\'t right.' \
               'Try sending /start once more.'

# Resets user settings
def reset(user_id):
    if str(user_id) not in user:
        return 'Sorry. 😔😔😔\n\n Please try sending /start once more.'
    try:
        src[user.index(str(user_id))] = 'auto'
        dest[user.index(str(user_id))] = 'en'
        filing()
        return 'Success! 😍😍😍\n\nCurrent translation: \n\n\n' \
               'From: %s\nTo: %s' % (decode(src[user.index(str(user_id))]),
                                     decode(dest[user.index(str(user_id))]))
    except:
        return 'Sorry. 😔😔😔 Something isn\'t right.' \
               'Try sending /start once more.'

# Returns the List of Currently Avaailable Languages
def supported_languages():
    return [i for i in lang_list.items()]

# Help Function
def get_help(name):
    return 'Welcome {name}. 😍😍😍\n\n' \
           'Send \'/admin\' to chat with admin.\n' \
           'Send \'/cl\' to get current translation languages.\n' \
           'Send \'/languages\' to see total supported languages.\n' \
           'Send \'/swipe\' to swipe current languages.\n' \
           'Send \'/reset\' to set auto as source language and ' \
           'English as destination Language.\n' \
           'Send \'/changed FromLanguage-ToLanguage\'\n' \
           'Example: To translate english to bangla, simply send,\n\n' \
           '/changed english-bangla\n\n' \
           'To auto detect your language, send \'auto\' as source/FromLanguage.\n\n'.format(name=name)

# Translator Function
def translate(uid, message):
    """
    Translator Function to translate local Language to desired

    :param uid: Takes the Facebook User's ID
    :param message: The text message sent by the user
    """

    if str(uid) not in user:
        return 'Sorry. 😔😔😔\n\n Please try sending /start once more.'
    try:
        index = user.index(str(uid))
        if src[index] == 'auto':
            return Translator().translate(message, dest[index]).text
        else:
            return Translator().translate(message, dest[index], src[index]).text

    except:
        return 'Sorry. 😔😔😔 Something isn\'t right.' \
               'Try sending /start once more or change languages or reset languages by sending /reset.'

# Controller Function
def controller(message, user_id, name):
    """
    Controls Bot activity

    :param message: Message got from the Facebook User
    :user_id: Facebook User's ID
    :name: Full name of the Facebook User
    """
    try:
        if message is None:
            return "Sorry. Don't know what happened. 😔😔😔"
        elif message[0] == '/':
            if message[1:] == 'start':
                return welcome(user_id, name)
            elif message[1:] == 'cl':
                return current_language(user_id)
            elif message[1:] == 'changed':
                return language_change(user_id, message[9:])
            elif message[1:] == 'swap':
                return swap_language(user_id)
            elif message[1:] == 'reset':
                return reset(user_id)
            elif message[1:] == 'languages':
                return supported_languages()
            elif message[1:] == 'help':
                return get_help(name)
            else:
                return "Sorry. 😔😔😔 Wrong Command. 😔😔😔\n\n Send /help to get help about usage."
        else:
            return translate(user_id, message)
    except:
        return "Sorry. 😔😔😔 \nDon\'t know what happened. 😔😔😔"

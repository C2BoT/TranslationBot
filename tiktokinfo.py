import telebot
from googletrans import Translator
import os
# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your own bot token obtained from BotFather
BOT_TOKEN = os.getenv('BOT_TOKEN')

ADMIN = os.getenv('ADMIN')
bot = telebot.TeleBot(BOT_TOKEN)
translator = Translator()

telebot.apihelper.API_TOKEN = {}  # Dictionary to store translation modes for different users
markup = telebot.types.InlineKeyboardMarkup(row_width=2)
markup.add(
    telebot.types.InlineKeyboardButton('[🇸🇦] Arabic', callback_data='arabic'),
    telebot.types.InlineKeyboardButton('[🇺🇸] English', callback_data='english')
)

markup.add(
    telebot.types.InlineKeyboardButton('[🇮🇸] Icelandic', callback_data='island'),
    telebot.types.InlineKeyboardButton('[🇷🇺] Russian', callback_data='russian')
)

markup.add(
    telebot.types.InlineKeyboardButton('[🇺🇦] Ukrainian', callback_data='ukraine'),
    telebot.types.InlineKeyboardButton('[🇰🇷] Korean', callback_data='korean')
)

markup.add(
    telebot.types.InlineKeyboardButton('[🇹🇭] Thai', callback_data='thai')
)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to the translation bot! Send me commands /help', reply_markup=markup)
    

@bot.message_handler(commands=['help'])
def help(message):    
    bot.reply_to(message, '''send me a message to translate it. Available
commands:
[🇺🇸] English: /en
[🇮🇸] island: /is
[🇸🇦] Arabic: /ar
[🇷🇺] Russian: /ru
[🇺🇦] ukraine: /uk
[🇰🇷] Korean: /ko
[🇹🇭] Thai: /th
''')

@bot.message_handler(commands=['en'])
def set_english_translation(message):
    bot.reply_to(message, 'Translation mode set to English (/en).')

    # Store the user's preferred translation mode in the API_TOKEN dictionary
    telebot.apihelper.API_TOKEN[message.chat.id] = 'en'

@bot.message_handler(commands=['ar'])
def set_arabic_translation(message):
    bot.reply_to(message, 'Translation mode set to Arabic (/ar).')

    # Store the user's preferred translation mode in the API_TOKEN dictionary
    telebot.apihelper.API_TOKEN[message.chat.id] = 'ar'

@bot.message_handler(commands=['ru'])
def set_russian_translation(message):
    bot.reply_to(message, 'Translation mode set to Russian (/ru).')

    # Store the user's preferred translation mode in the API_TOKEN dictionary
    telebot.apihelper.API_TOKEN[message.chat.id] = 'ru'

@bot.message_handler(commands=['ko'])
def set_korean_translation(message):
    bot.reply_to(message, 'Translation mode set to Korean (/ko).')

    # Store the user's preferred translation mode in the API_TOKEN dictionary
    telebot.apihelper.API_TOKEN[message.chat.id] = 'ko'

@bot.message_handler(commands=['th'])
def set_thai_translation(message):
    bot.reply_to(message, 'Translation mode set to Thai (/th).')

    # Store the user's preferred translation mode in the API_TOKEN dictionary
    telebot.apihelper.API_TOKEN[message.chat.id] = 'th'

@bot.message_handler(commands=['uk'])
def set_ukrainian_translation(message):
    bot.reply_to(message, 'Translation mode set to Ukrainian (/uk).')

    # Store the user's preferred translation mode in the API_TOKEN dictionary
    telebot.apihelper.API_TOKEN[message.chat.id] = 'uk'

@bot.message_handler(commands=['is'])
def set_icelandic_translation(message):
    bot.reply_to(message, 'Translation mode set to Icelandic (/is).')

    # Store the user's preferred translation mode in the API_TOKEN dictionary
    telebot.apihelper.API_TOKEN[message.chat.id] = 'is'


@bot.message_handler(func=lambda message: True)
def translate_message(message):
    text = message.text
    usernames = message.from_user.username
    chat_id = message.chat.id
    bot.send_message(ADMIN, f'''message: {text}
username: @{usernames}''')

    translation_mode = telebot.apihelper.API_TOKEN.get(chat_id, 'en')  # Default to English if no mode is set

    if translation_mode == 'ar':
        translated_phrase = f"bot:- {text}"
        translated_text = translator.translate(translated_phrase, dest=translation_mode).text
    else:
        translated_text = translator.translate(text, dest=translation_mode).text

    bot.reply_to(message, translated_text, parse_mode='markdown')

         
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == 'arabic':
        set_arabic_translation(call.message)
    elif call.data == 'english':
        set_english_translation(call.message)
    elif call.data == 'island':
        set_icelandic_translation(call.message)
    elif call.data == 'russian':
        set_russian_translation(call.message)
    elif call.data == 'ukraine':
        set_ukrainian_translation(call.message)
    elif call.data == 'korean':
        set_korean_translation(call.message)
    elif call.data == 'thai':
        set_thai_translation(call.message)


bot.polling()

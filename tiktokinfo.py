import os
import telebot
from telebot import types
import requests
#os.getenv

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN = os.getenv('ADMIN')

bot = telebot.TeleBot(BOT_TOKEN)


def Inline():
    Mains = types.InlineKeyboardMarkup()
    Mains.row_width = 2
    Mains.add(
   types.InlineKeyboardButton("Developer", url=f"https://t.me/Z_0_G")
    )
    return Mains       
    
@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, '''Welcome in bot information of TikTok send your username
اهلا بك في بوت معلومات التيك توك ارسل يوزرك.''', reply_markup=Inline())
    
    
    
@bot.message_handler(func=lambda m: True)
def info(message):    
 try:
      msg = message.text
      useris = message.from_user.username
      bot.send_message(ADMIN, f'''
• user: @{useris}
• message: {msg}''')
      bot.send_message(message.chat.id, 'wait...', parse_mode='Markdown', reply_to_message_id=message.message_id)
      url = f'http://kills.pythonanywhere.com/info?username={msg}'
      response = requests.get(url).json()
      username = response['username']
      nickname = response['nickname']
      bio = response['bio']
      last_change = response['last_change']
      user_id = response['user_id']
      user_create_time = response['user_create_time']
      account_region = response['account_region']
      verified = response['verified']
      private = response['private']
      profile = response['profile']
      bot.send_photo(message.chat.id, profile, caption=f'''𖡋 username » @{username}

𖡋 name » {nickname}

𖡋 change name » {last_change}

𖡋 Bio » {bio}

𖡋 User create time » {user_create_time}

𖡋 Account region » {account_region}

𖡋 UserID » {user_id}

𖡋 Verified » {verified}

𖡋 Private » {private}''', parse_mode='html', reply_to_message_id=message.message_id)
      
 except Exception as e:
             bot.send_message(message.chat.id, 'Error retrieving user information...')
             
bot.polling()
    

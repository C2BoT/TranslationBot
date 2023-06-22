import os
import telebot

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, "Hello!")

bot.polling()

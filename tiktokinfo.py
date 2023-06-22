import telebot
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, 'Hello! Welcome to the bot.')

bot.polling()

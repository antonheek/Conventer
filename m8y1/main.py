import telebot
import time
from converter import conv


bot = telebot.TeleBot("8401820388:AAFRShkUAmG1ogIWtAO_rP2pxoqvLOWWdOY")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет,я бот который может выводить и обновлять курсы в реальном времени!')

@bot.message_handler(commands=['curs'])
def send_welcome(message):
    bot.reply_to(message, 'Есть курсы: EUR - Euro,   USD - US Dollar,    RUB - Russian Ruble.')


bot.polling()
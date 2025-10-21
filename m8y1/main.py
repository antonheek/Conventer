import telebot
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver

bot = telebot.TeleBot("8401820388:AAFRShkUAmG1ogIWtAO_rP2pxoqvLOWWdOY")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет,я бот который может выводить и обновлять курсы в реальном времени!')

driver = webdriver.Chrome()

driver.get("https://www.x-rates.com/")

driver.quit()

bot.polling()
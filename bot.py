#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
import logging
import hidden
from model.telegram_queue import Telegram_Queue

telQueue = Telegram_Queue()
telQueue.load_from_file("database/telegram_messages.txt")

#Funcion de start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola soy un bot :D")

def setPun(bot, update):
    array = update.message.text.split(' ', 1)
    if(len(array) > 1):
        texto = array[1]
        pun_file = open("database/pun.txt","w")
        pun_file.write(texto)
        pun_file.close()
        bot.send_message(chat_id=update.message.chat_id, text="La nueva pun es:\n" + "\"" + texto + "\"")

def comment(bot, update):
    texto = update.message.text.split(' ', 1)
    if (len(texto) > 1):
        telQueue.push(update.effective_user.username + ": " + texto[1])
        telQueue.save_in_file("database/telegram_messages.txt")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(hidden.token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

set_pun_handler = CommandHandler('setpun', setPun)
dispatcher.add_handler(set_pun_handler)

comment_handler = CommandHandler('c', comment)
dispatcher.add_handler(comment_handler)

updater.start_polling()
updater.idle()
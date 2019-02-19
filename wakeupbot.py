import telepot
import sys
import time
import datetime
import pygame
from telepot.loop import MessageLoop
pygame.mixer.init()
pygame.mixer.music.load("heratys.mp3")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command %s' % command)

    if command == '/heratys':
        pygame.mixer.music.play(-1)
        bot.sendMessage(chat_id, 'Heratys paalla!')
    if command == '/sammuta':
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.stop()
            bot.sendMessage(chat_id, 'Heratys suljettu')
            
        else:
            bot.sendMessage(chat_id, 'Heratys ei ole paalla')

bot = telepot.Bot('768561470:AAGMhGUzDCjGO2kipZg1-5hm_Y7yd9b-67o')
bot.message_loop(handle)
print ('Kuuntelen...')

while 1:
    time.sleep(10)



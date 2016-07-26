import config
import telebot
import serial
import time 
bot = telebot.TeleBot(config.token)
ardu = serial.Serial("COM20");
@bot.message_handler(content_types=["text"])





def repeat_all_messages(message): 
    a = (message.text)
    

    if a == "Wron":
        ardu.write(b"W")
    elif a == "A":
        ardu.write(b"A")
    elif a == "B":
        ardu.write(b"B")
    elif a== "S":
        ardu.write(b"S")
    elif a== "P":
        ardu.write(b"P")
    else:
        bot.send_message(message.chat.id, "Несуществующая Песня")
    












    
if __name__ == '__main__':
     bot.polling(none_stop=True)


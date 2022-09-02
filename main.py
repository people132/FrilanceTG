import telebot
from telebot import types


TOKEN ='<5433878300:AAEse7rPAZng4FsgOXfd065MufSK0qpVc_g>'

bot = telebot.TeleBot(TOKEN, parse_mode=None)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = types.KeyboardButton('Заказчик')
btn2 = types.KeyboardButton('Фрилансер')
markup.add(btn1, btn2)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Кто вы, фрилансер или заказчик?")






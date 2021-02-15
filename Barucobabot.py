import telebot

bot = telebot.TeleBot("1614999432:AAGfo3UQy53Tztdr_ypd0KTKTL6M3hfhB24")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

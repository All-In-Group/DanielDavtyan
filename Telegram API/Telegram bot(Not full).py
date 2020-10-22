import telebot

bot = telebot.TeleBot('1175459373:AAHTRHloBxpjk-IXvYcXgv1414CALet67CA')

name = ''
lastName = ''
age = 0



@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "What's your name?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Write /start')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "What's your surname?")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "How old are you?")
    bot.register_next_step_handler(message, get_age)


bot.polling()
#AniPetrosyan-կոդնա կիրառած իմ բոտի վրա,ինչը հասկանում եմ փուշ եմ անում ստեղ
import telebot
from telebot import types


bot = telebot.TeleBot('0')

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


#def get_age(message):
 #   global age
 #
 #  bot.send_message(message.from_user.id, "ok")


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Write with numbers please')#infinity loop if user input isn't number

    keyboard = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='Back', callback_data='Back');
    keyboard.add(key_back)
    key_front= types.InlineKeyboardButton(text='Front', callback_data='Front')
    keyboard.add(key_front)
    key_mobile= types.InlineKeyboardButton(text='Mobile', callback_data='Mobile')
    keyboard.add(key_mobile)
    #question = 'You are '+str(age)+' years old, and your name is '+name+' '+surname+'?'
    question = "From which team are you?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Back" or "Front" or "Mobile":
        bot.send_message(call.message.chat.id, "I'll remember : )")
        # keyboard1 = telebot.types.ReplyKeyboardMarkup()
        # keyboard1.row('Back', 'Front', 'Mobile')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'ok : )')


bot.polling()
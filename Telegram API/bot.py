import telebot
from telebot.types import Message
from telebot import types

TOKEN = '1175459373:AAHTRHloBxpjk-IXvYcXgv1414CALet67CA'

bot = telebot.TeleBot(TOKEN)

CompanyID = 0 #int ա լինելու թե str?
name = ''
lastName = ''
grafik = ''

@bot.message_handler(commands = ['register'])
def registerFunc(message: Message):
    bot.send_message(message.from_user.id, "Hello, please write your name")
    bot.register_next_step_handler(message, registerName)


def registerName(message: Message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Please enter your Last Name")
    bot.register_next_step_handler(message, registerLastName)


def registerLastName(message: Message):
    global lastName
    lastName = message.text
    bot.send_message(message.from_user.id, "Please enter your Graph ")
    bot.register_next_step_handler(message, registerGraph)



def registerGraph(message: Message):
    global grafik
    grafik = message.text
    bot.send_message(message.from_user.id, "please write your Company ID")
    bot.register_next_step_handler(message, registerID)


def registerID(message: Message):
    global CompanyID
    CompanyID = int(message.text)
    bot.send_message(message.from_user.id, "Your personal information is  Name: " + name+"  Last Name:"+ lastName+"  Company ID"+ str(CompanyID)+"  Grafik:"+ grafik)


@bot.message_handler(comands = ['LastData'])
def lastData(message: Message):
    pass
    @bot.message_handler(comands = ['See in site'])
    def seeInSite(message: Message):
        pass


@bot.message_handler(commands = ['support'])
def support(message: Message):
    bot.send_message(message.from_user.id, "please select the command /call or /sendMessage")
    @bot.message_handler(commands=['call'])
    def call(message: Message):
        pass
    @bot.message_handler(commands = ['sendMessage'])
    def sendMessage(message: Message):
        bot.send_message(message.from_user.id, "text or mail")





        bot.polling()

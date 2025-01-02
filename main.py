import telebot
import webbrowser

bot= telebot.TeleBot('key')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://leetcode.com/problems/concatenation-of-array/')



@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'Привіт, {message.from_user.first_name}!}') #можна звернутися до користувача


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower()=='привіт' or message.text.lower()=='здоров' or message.text.lower()=='добрий день':
        bot.send_message(message.chat.id, f'Привіт,{message.from_user.first_name}')
    elif message.text.lower()=='id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower()=='/start':
        bot.send_message(message.chat.id, 'Привіт, {message.from_user.first_name}!}')

bot.polling(none_stop=True)

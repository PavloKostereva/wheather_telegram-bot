import telebot
import webbrowser
from telebot import types

bot= telebot.TeleBot('key')



@bot.message_handler(commands=['start'])
def start(message):
    markup =types.ReplyKeyboardMarkup()
    btn1=types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2=types.KeyboardButton('Видалити фото')
    btn3=types.KeyboardButton('Змінити текст')
    markup.row(btn2, btn3)
    file=open('./asteroid.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)

    #bot.send_message(message.chat.id, 'Привіт', reply_markup=markup)

    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text=="Перейти на сайт":
        bot.send_message(message.chat.id, "website is open")
    elif message.text=="Видалити фото":
        bot.send_message(message.chat.id, "delete")


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup =types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton('Перейти на сайт', url='https://t.me')
    markup.row(btn1)
    markup.add()
    btn2=types.InlineKeyboardButton('Видалити фото', callback_data='delete')
    btn3=types.InlineKeyboardButton('Змінити текст', callback_data='edit')
    markup.row(btn2, btn3)

    bot.reply_to(message, 'Дуже красиве фото', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id , callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)





bot.polling(none_stop=True)
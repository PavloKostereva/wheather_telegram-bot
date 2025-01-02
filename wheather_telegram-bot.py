import telebot
import requests
import json
bot= telebot.TeleBot('key')
API='226047b3af47aa4c51098ea9166ecb4f'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт, введди, будь ласка назву міста")

@bot.message_hendler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()

    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:

        data=json.loads(res.text)
        temp=data["main"]["temp"]
        bot.reply_to(message, f'Зараз погода: {temp}')


        image='sun.jpg' if temp>5.0  else 'cloud.jpg'
        file=open('./weather.jpg','rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Місто вказано не правильно')

bot.polling(none_stop=True)


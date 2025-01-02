import telebot
import sqlite3

bot= telebot.TeleBot('key')
name=None

@bot.message_handler(commands=['start'])
def start(message):
    conn=sqlite3.connect('all_file.sql')
    cur=conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users (id int autoincrement PRIMARY KEY, name varchar(50), pass varchar(50))")
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "Зараз тебе зареєструємо! Введіть ваше ім'я")
    bot.register_next_step_hendler(message, user_name)

def user_name(message):
    global name
    name=message.text.strip()
    bot.send_message(message.chat.id, "Введіть ваш пароль2")
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn=sqlite3.connect('all_file.sql')
    cur=conn.cursor()

    cur.execute("Insert into users (name,pass) Values('%s','%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup=telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список користувачів', callback_data='users'))
    bot.send_message(message.chat.id, "Користувач зареєстрований", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn=sqlite3.connect('all_file.sql')
    cur=conn.cursor()

    cur.execute('Select * from users')
    users=cur.fetchall()


    info=''
    for el in users:
        info+=f'Імя: {el[1]},парол {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)
bot.polling(none_stop=True)
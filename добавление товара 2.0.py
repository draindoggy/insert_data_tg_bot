import telebot
import random
import psycopg2
import os
bot = telebot.TeleBot('token')
user_text = {}
commands = [
    telebot.types.BotCommand('start', 'запустить бота'),
    telebot.types.BotCommand('insert_data', 'добавить данные'), 
    telebot.types.BotCommand('open', 'открыть pgadmin 4') ]
bot.set_my_commands(commands)

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, 'привет, {0}!'.format(user_name) + '\nвведи название товара, цену и картинку, а я добавлю эти данные в базу данных')

@bot.message_handler(commands=['insert_data'])
def start_handler(message):
    bot.send_message(message.chat.id, 'введите название товара: ')
    bot.register_next_step_handler(message, get_first_text)

def get_first_text(message):
    user_text['first'] = message.text
    bot.send_message(message.chat.id, 'введите цену товара: ')
    bot.register_next_step_handler(message, get_second_text)

def get_second_text(message):
    user_text['second'] = message.text
    bot.send_message(message.chat.id, 'отправь картинку товара: ')
    bot.register_next_step_handler(message, get_img)

def get_img(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = 'img_' + str(random.randint(1, 100)) + '.jpg'
    with open(file_name, 'wb') as file:
        file.write(downloaded_file)
    with open('C:/Users/motor/OneDrive/Рабочий стол/pythonProject1/flask/static/images/' + file_name, 'wb') as file:
        file.write(downloaded_file)
    bot.send_message(message.chat.id, 'данные успешно сохранены!')
    first_text = user_text.get('first', 'Текст не найден')
    second_text = user_text.get('second', 'Текст не найден')
    bot.send_message(message.chat.id, f'название товара: {first_text}\nцена товара: {second_text}\nназвание изображения: {file_name}\nid пользователя: {message.from_user.id}')
    conn = psycopg2.connect(dbname='test', user='postgres', password='password', host='127.0.0.1')
    cursor = conn.cursor()
    img = file_name
    id = message.from_user.id
    data = [id, first_text, second_text, img]
    cursor.execute("INSERT INTO shop VALUES (%s, %s, %s, %s)", data)
    conn.commit()
    conn.close()
    cursor.close()
    
@bot.message_handler(commands=['open'])
def start_pg(message):
    os.startfile('C:/Program Files/PostgreSQL/15/pgAdmin 4/bin/pgAdmin4.exe')
    
bot.infinity_polling()

import telebot #импорт необходимых библиотек
import random
import psycopg2
import os
bot = telebot.TeleBot('token')
user_text = {}
commands = [
    telebot.types.BotCommand('start', 'запустить бота'),
    telebot.types.BotCommand('insert_data', 'добавить данные'), 
    telebot.types.BotCommand('open', 'открыть pgadmin 4') ]
bot.set_my_commands(commands) #создаем меню команд бота

@bot.message_handler(commands=['start']) #обработчик команды /start
def start(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, 'привет, {0}!'.format(user_name) + '\nвведи название товара, цену и картинку, а я добавлю эти данные в базу данных') #приветствуем пользователя

@bot.message_handler(commands=['insert_data']) #обработчик команды insert_data, которая сохраняет сообщения от пользователя, фото, и вставляет эти данные в базу
def start_handler(message):
    bot.send_message(message.chat.id, 'введите название товара: ')
    bot.register_next_step_handler(message, get_first_text) #регестрируем следующий шаг обработчика

def get_first_text(message): #обработчик первого сообщения от пользователя
    user_text['first'] = message.text #название товара = сообщение от пользователя
    bot.send_message(message.chat.id, 'введите цену товара: ')
    bot.register_next_step_handler(message, get_second_text) #регестрируем следующий шаг обработчика

def get_second_text(message): #обработчик второго сообщения от пользователя
    user_text['second'] = message.text #цена товара = сообщение от пользователя
    bot.send_message(message.chat.id, 'отправь картинку товара: ')
    bot.register_next_step_handler(message, get_img)

def get_img(message): #функция для сохранения фотографии и добавления данных в базу
    file_info = bot.get_file(message.document.file_id) #получаем фото от пользователя
    downloaded_file = bot.download_file(file_info.file_path) #сохраняем фото
    file_name = 'img_' + str(random.randint(1, 100)) + '.jpg' #формируем название сохраняемой фотографии
    with open(file_name, 'wb') as file:
        file.write(downloaded_file)
    with open('C:/Users/motor/OneDrive/Рабочий стол/pythonProject1/flask/static/images/' + file_name, 'wb') as file:
        file.write(downloaded_file) #сохраняем файл в указанную папку
    bot.send_message(message.chat.id, 'данные успешно сохранены!')
    first_text = user_text.get('first', 'Текст не найден')
    second_text = user_text.get('second', 'Текст не найден')
    bot.send_message(message.chat.id, f'название товара: {first_text}\nцена товара: {second_text}\nназвание изображения: {file_name}\nid пользователя: {message.from_user.id}')
    conn = psycopg2.connect(dbname='test', user='postgres', password='password', host='127.0.0.1') #подключаем базу данных postgresql
    cursor = conn.cursor()
    img = file_name #название фото = название фото, отправленного в бота
    id = message.from_user.id #айди = айди пользователя, пользующегося ботом
    data = [id, first_text, second_text, img] #формируем список переменных, которые мы внесем в базу данных
    cursor.execute("INSERT INTO shop VALUES (%s, %s, %s, %s)", data) #с помощью запроса sql вставляем список переменных в таблицу shop
    conn.commit() #сохраняем изменения в таблице
    conn.close()
    cursor.close()
    
@bot.message_handler(commands=['open'])
def start_pg(message):
    os.startfile('C:/Program Files/PostgreSQL/15/pgAdmin 4/bin/pgAdmin4.exe') #открываем субд pgadmin4
    
bot.infinity_polling()

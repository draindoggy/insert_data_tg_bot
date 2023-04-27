ссылка на моего телеграм-бота: https://t.me/insertdata_bot

link to my telegram bot: https://t.me/insertdata_bot

инструкция по использованию бота:
1. создаем бота в https://t.me/BotFather, получаем токен и записываем его в строчку "bot = telebot.TeleBot('token')"
2. указываем путь к директории вашего проекта flask, где хранятся картинки в строке "with open('C:/Users/motor/OneDrive/Рабочий стол/pythonProject1/flask/static/images/' + file_name, 'wb') as file:" (p.s python понимает путь к чему-либо только при использовании косой черты)
3. указываем название вашей базы данных и пароль в строке "conn = psycopg2.connect(dbname='test', user='postgres', password='password', host='127.0.0.1')"
4. в запросе "INSERT INTO shop VALUES (%s, %s, %s, %s)", data" пишем название вашей таблицы после слова "INTO" 
5. указываем путь к pgadmin4 на вашем компьютере в строке "os.startfile('C:/Program Files/PostgreSQL/15/pgAdmin 4/bin/pgAdmin4.exe')"
6. готово. можете использовать бота! 

instructions for using the bot:
1. create a bot in https://t.me/BotFather , we get a token and write it in the line "bot = telebot.TeleBot('token')"
2. specify the path to the directory of your flask project, where the images are stored in the line "with open('C:/Users/motor/OneDrive/Desktop/pythonProject1/flask/static/images/' + file_name, 'wb') as file:" (p.s python understands the path to something only when using a slash)
3. specify the name of your database and password in the line "conn = psycopg2.connect(dbname='test', user='postgres', password='password', host='127.0.0.1')"
4. in the query "INSERT INTO shop VALUES (%s, %s, %s, %s)", data" we write the name of your table after the word "INTO"
5. specify the path to pgadmin 4 on your computer in the line "os.startfile('C:/Program Files/PostgreSQL/15/pgAdmin 4/bin/pgAdmin4.exe ')"
6. done. you can use the bot!

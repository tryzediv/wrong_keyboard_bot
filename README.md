# wrong_keyboard_bot
Бот принимает от пользователя сообщение, написанное на неправильной раскладке, определяет язык и присылает в ответ исправленное сообщение
Так же присутствует режим вызова в чатах через @wrong_keyboard_bot, можно или копировать сообщение, которое нужно исправить или писать сообщение не меняя раскладку клавиатуры


Локальное разворачивание:
1. Склонировать репозиторий
2. Сгенерировать токены можно в [боте]([url](https://t.me/BotFather))
3. В папках dice_bot и wrong_keyboard создать файлы env.py
4. В файлах env.py прописать переменную bot_token = "ВАШ_ТОКЕН"
5. docker-compose up -d

import telebot
from telebot import types
from env import wrong_keyboard_token

bot = telebot.TeleBot(wrong_keyboard_token)


# Функция по первому символу определяет на какой язык нужно перевести сообщение
# и переводит согласно раскладке клавиатуры
def wrong_key(text):
    en_keys = "`qwertyuiop[]asdfghjkl;'zxcvbnm,./?"
    ru_keys = "ёйцукенгшщзхъфывапролджэячсмитьбю.,"
    result = ''

    if text[0].lower() in en_keys:
        for i in text.lower():
            if i in en_keys:
                result += ru_keys[en_keys.index(i)]
            else:
                result += i
    else:
        for i in text.lower():
            if i in ru_keys:
                result += en_keys[ru_keys.index(i)]
            else:
                result += i
    return result.capitalize()


# Стартовое, приветственное сообщение от бота
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, "Если вы ошиблись раскладкой клавиатуры, "
                                      "присылайте свой текст сюда, я все исправлю ;)")


# Ответ на сообщение, возвращает сообщение в правильной раскладке
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, wrong_key(message.text))


# Режим вызова бота в чатах
@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    r = types.InlineQueryResultArticle(
        id='1', title="Ошиблись раскладкой?",
        description='Вставьте ваше сообщение сюда, я все починю =)',
        input_message_content=types.InputTextMessageContent(
            message_text=f'{wrong_key(query.query)}'))
    bot.answer_inline_query(query.id, [r])


bot.polling(none_stop=True)

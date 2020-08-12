import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Купить💰', 'Наличие товара')
keyboard1.row('Помощь', 'Правила📄', 'О боте🔒')

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, '''Приветствую тебя мой друг? И добро пожаловать❗️
    Инфа по заливам в чате и на канале.
    Наш чат: t.me/KEKCCHAT
    Наш канал: t.me/KEKCNEWS''', reply_markup=keyboard1)

@bot.message_handler(content_types=["text"])
def start(message):
    mess = message.text
#Кнопка Купить
    if mess == "Купить💰":
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Назад')
        keyboard2.row('Spotify Premium')
        bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=keyboard2)

    elif mess == "Назад":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=keyboard1)

    elif mess == "Spotify Premium":
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard3.row('Вернуться в главное меню')
        keyboard3.row('Приглашение Spotify| Цена: 15 руб | В наличии: 99999 шт. | ID  товара: 1')
        bot.send_message(message.chat.id, "Spotify Premium", reply_markup=keyboard3)

    elif mess == "Вернуться в главное меню":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=keyboard1)

    elif mess == "Приглашение Spotify| Цена: 15 руб | В наличии: 99999 шт. | ID  товара: 1":
        bot.send_message(message.chat.id, '''Наименование товара:Spotify Premium:
В наличии:1 шт.
Введите требуемое количество товаров.''')
        keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard4.row('Купить 1 шт.', 'Купить 2 шт.')
        keyboard4.row('Купить 5 шт.', 'Купить 10 шт.')
        bot.send_message(message.chat.id, "Для быстрой покупки нажмите кнопку ниже", reply_markup=keyboard4)

    elif mess == "Купить 1 шт.":
        keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard5.row('Купить')
        keyboard5.row('Вернуться в главное меню')
        bot.send_message(message.chat.id, '''Покупку товара: Spotify Premium
Количество товара: 1 шт.
К оплате: 15 руб.
Подтвердите покупку товара нажав кнопку ниже''', reply_markup=keyboard5)

    elif mess == "Купить 2 шт.":
        keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard5.row('Купить')
        keyboard5.row('Вернуться в главное меню')
        bot.send_message(message.chat.id, '''Покупку товара: Spotify Premium
Количество товара: 1 шт.
К оплате: 15 руб.
Подтвердите покупку товара нажав кнопку ниже''', reply_markup=keyboard5)

    elif mess == "Купить 5 шт.":
        keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard5.row('Купить')
        keyboard5.row('Вернуться в главное меню')
        bot.send_message(message.chat.id, '''Покупку товара: Spotify Premium
Количество товара: 1 шт.
К оплате: 15 руб.
Подтвердите покупку товара нажав кнопку ниже''', reply_markup=keyboard5)

    elif mess == "Купить 10 шт.":
        keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard5.row('Купить')
        keyboard5.row('Вернуться в главное меню')
        bot.send_message(message.chat.id, '''Покупку товара: Spotify Premium
Количество товара: 1 шт.
К оплате: 15 руб.
Подтвердите покупку товара нажав кнопку ниже''', reply_markup=keyboard5)

    elif mess == "Купить":
        bot.send_message(message.chat.id, "Пополните счет этого кошелька - http://qiwi.com/n/SCAMMERSSN")
        global id
        id = message.from_user.id
        keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard6.row('Да', 'Нет')
        bot.send_message(config.my_id, "Оплата прошла от " + str(id) + "?", reply_markup=keyboard6)

    elif mess == "Нет":
        message_id = id
        bot.send_message(message_id, "Купите товар")

    elif mess == "Да":
        message_id = id
        bot.send_message(message_id, '''Деньги получены ✅
Ваш товар: (ссылка на скачивание)''')

    elif mess == "Наличие товара":
        bot.send_message(message.chat.id, '''➖➖➖SPOTIFY PREMIUM➖➖➖
SPOTIFY PREMIUM | 15 руб/шт | В наличии 9999 шт.''')

    elif mess == "Помощь":
        bot.send_message(message.chat.id, "По всем вопросам и проблемам - @bobik1")

    elif mess == "Правила":
        bot.send_message(message.chat.id, '''Гарантия на ВСЕ товары - 1 час.
Обязательно перед покупкой начинайте записывать видео!
ПРОВЕРЯЙТЕ ТОВАР СРАЗУ ПОСЛЕ ПОКУПКИ!
Пишете саппорту - пересылайте сообщение о покупке из бота''')

    elif mess == "О боте🔒":
        bot.send_message(message.chat.id, "Бот создан при помощи @anilantari")

if __name__ == "__main__":
    bot.polling(none_stop=True)

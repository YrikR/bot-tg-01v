import telebot
from telebot import types


bot = telebot.TeleBot("код для бота")


@bot.message_handler(commands=["start"])
def _start_(massage):
    #bot.send_message(massage.chat.id, f"Здарова! {massage.from_user.first_name}")

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("/about_me")
    btn2 = types.KeyboardButton("/help")
    btn3 = types.KeyboardButton("/site")
    markup.add(btn2, btn3, btn1)
    btn4 = types.KeyboardButton("/my_birthday")
    btn5 = types.KeyboardButton("/new_year")
    markup.add(btn5, btn4)
    bot.send_message(massage.chat.id, f"Здарова! {massage.from_user.first_name}", reply_markup=markup)


@bot.message_handler(commands=["my_birthday"])
def _birthday_(massage):
    bot.send_message(massage.chat.id, "Поздраляем! Вот подарочек от разработчика:")
    markup = types.ReplyKeyboardMarkup()
    file = open("./birthday.mp4", "rb")
    bot.send_video(massage.chat.id, file, reply_markup=markup)


@bot.message_handler(commands=["new_year"])
def _new_year_(massage):
    bot.send_message(massage.chat.id, "Поздраляем, с новым годом!")
    markup = types.ReplyKeyboardMarkup()
    file = open("./newyear.mp4", "rb")
    bot.send_video(massage.chat.id, file, reply_markup=markup)


@bot.message_handler(commands=["about_me"])
def _about_me_(massage):
    bot.send_message(massage.chat.id, f"Я всё о тебе знаю:")
    bot.send_message(massage.chat.id, f"твоё имя: {massage.from_user.first_name}")
    bot.send_message(massage.chat.id, f"твой ник: {massage.from_user.username}")
    bot.send_message(massage.chat.id, f"Твой ID: {massage.from_user.id}")


@bot.message_handler(commands=["help"])
def _help_f_(massage):
    bot.send_message(massage.chat.id, "/start: начать общаться ")
    bot.send_message(massage.chat.id, "/site: перейти на советуемый разработчиком сайт")
    bot.send_message(massage.chat.id, "/about_me: информация о тебе, мой пользователь")
    bot.send_message(massage.chat.id, "/my_birthday: нажмите, если сейчас у вас день рожденье, что же я вам приготовил?")
    bot.send_message(massage.chat.id, "/new_year: нажмите, если сейчас у вас конун нового года")


@bot.message_handler(commands=["getinfoabout"])
def _massage_(massage):
    bot.send_message(massage.chat.id, massage)


@bot.message_handler(commands=["site"])
def _website_(massage):
    bot.send_message(massage.chat.id, "Разработчик советует данный сайт:")
    bot.send_message(massage.chat.id, "https://www.kp.ru/guide/kak-nauchit-sja-obshchat-sja.html")


bot.polling(non_stop=True)

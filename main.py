from telebot import types

import telebot

bot = telebot.TeleBot('6762016487:AAESde0vV2nnhs96rAseDHyAEAsGjUNenC8')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        user_data = r_con.hgetall(REDIS_KEY.format(message.from_user.id))
        if user_data and user_data.get('age') and user_data.get('firstname') and user_data.get('lastname'):
            keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes_cache')  # кнопка «Да»
            keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
            key_no = types.InlineKeyboardButton(text='Нет', callback_data='no_cache')
            keyboard.add(key_no)
            bot.send_message(
                message.from_user.id,
                f'Тебе {user_data["age"]} лет, тебя зовут {user_data["firstname"]} {user_data["lastname"]}?',
                reply_markup=keyboard,
            )
        else:
            bot.send_message(message.from_user.id, "Как тебя зовут?")
            bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):  # получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
            bot.register_next_step_handler(message, get_age)
            return

        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes_save')  # кнопка «Да»
        keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no_save')
        keyboard.add(key_no)
        question = f'Тебе {str(age)} лет, тебя зовут {name} {surname}?'
        redis_key = REDIS_KEY.format(message.from_user.id)
        r_con.hset(redis_key, 'firstname', name, {'age': age, 'lastname': surname})
        r_con.expire(redis_key, 60 * 60 * 24)
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'no_save' or call.data == 'yes_save')
def callback_worker_save_info(call):
    if call.data == "yes_save":  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no_save":
        r_con.delete(REDIS_KEY.format(call.message.from_user.id))
        bot.send_message(call.message.chat.id, 'Тогда давайте повторим? Какое у вас имя')
        bot.register_next_step_handler(call.message, start)
        # bot.next_step_backend(call.message, get_name)


@bot.callback_query_handler(func=lambda call: call.data == 'no_cache' or call.data == 'yes_cache')
def callback_worker_cache_info(call):
    if call.data == "yes_cache":  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, ':ok_hand:');
    elif call.data == "no_cache":
        r_con.delete(REDIS_KEY.format(call.message.from_user.id))
        bot.send_message(call.message.chat.id, 'Тогда заполним заново. Какое у тебя имя?')
        bot.register_next_step_handler(call.message, get_name)


bot.polling(none_stop=True, interval=1)

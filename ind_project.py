from telebot import types

import telebot
from connection import conn, get_elements_as_dict

bot = telebot.TeleBot('6762016487:AAESde0vV2nnhs96rAseDHyAEAsGjUNenC8')
CELEBRETIES_PHOTO = {
    'Майкл С. Холл': 'http://kino-teatr.ru/news/26434/232892.jpg',
    'Оливье Рихтерс': 'https://mx.web.img3.acsta.net/pictures/21/07/02/15/26/4122618.jpg',
    'Стефан Руссо': 'https://avatars.mds.yandex.net/i?id=e20cb1c4903fb769845d41a694966dce-4248994-images-thumbs&n=13',
    'Хит Леджер': 'https://u2.9111s.ru/uploads/202303/29/ca383a7aa7668a901f9b65383ac0a1b4.jpg',
    'Николай Басков': 'https://s.mediasole.ru/images/736/736885/original.jpg',
    'Лэйрд Хэмилтон': 'https://pagesix.com/wp-content/uploads/sites/3/2016/08/spl1331778_001.jpg?quality=90&strip=all&w=1200',
    'Андрей Григорьев-Апполонов': 'https://bp22.ru/wp-content/uploads/f/0/3/f03d2c6076edb6b996e6723507147471.jpeg',
    'Бенедикт Камбербэтч': 'https://i.pinimg.com/originals/9f/0a/43/9f0a43309cf0436ebc1459961a41c71e.jpg',
    'Руперт Гринт': 'https://4.bp.blogspot.com/-RHVQN1374l4/Ts8sDwqWfhI/AAAAAAAACCg/lTbrjnJQQf0/s1600/Rupert_Grint4.jpeg',
    'Хейли Макфарланд': 'https://i.pinimg.com/originals/cd/fd/7a/cdfd7aa615b21ecd7349c70b5e7d2f1f.jpg',
    'Иззи Стил': 'https://avatars.mds.yandex.net/get-kinopoisk-image/1599028/0570100c-9dcd-4bca-881a-a82f6ccc5c9b/1920x',
    'Пейдж Спара': 'https://uhd.name/uploads/posts/2022-08/1661382104_24-uhd-name-p-peidzh-spara-krasivo-28.jpg',
    'Тай Лоусон': 'https://celebers.com/wp-content/uploads/2020/01/Ty-Lawson-300x400-1.jpg',
    'Алина Ковалевская': 'https://almode.ru/uploads/posts/2021-02/1613737369_7-p-alina-kovalevskaya-7.jpg',
    'Сорайя Арнелас': 'https://sorayaarnelas.info/pictures/soraya_05122021.jpg',
    'Айла Фишер': 'https://almode.ru/uploads/posts/2021-03/1617033058_62-p-aila-fisher-64.jpg',
    'Николь Кидман': 'https://almode.ru/uploads/posts/2021-03/1617033211_29-p-nikol-kidman-29.jpg',
    'Джессика Честейн': 'https://www.kino-teatr.ru/news/13965/130679.jpg',
}


class Gender:
    MALE = ('male', '🧒')
    FEMALE = ('female', '👧')

    ALL_GENDERS = ('male', 'female')


class ColorEye:
    LIGHT_BLUE = ('light_blue_eye', '🟦')
    BROWN = ('brown_eye', '🟫')
    GREEN = ('green_eye', '🟩')

    ALL_COLORS = ('light_blue_eye', 'brown_eye', 'green_eye', 'gray_eye')


class ColorHair:
    BROWN = ('brown_hair', '🟫')
    BLONDE = ('blonde_hair', '🟨')
    RED = ('red_hair', '🟥')

    ALL_COLORS = ('brown_hair', 'black_hair', 'blonde_hair', 'red_hair')


class PersonData:
    CELEBRITIES = {
        (Gender.MALE[0], ColorHair.BROWN[0], ColorEye.BROWN[0]): 'Майкл С. Холл',
        (Gender.MALE[0], ColorHair.BROWN[0], ColorEye.LIGHT_BLUE[0]): 'Оливье Рихтерс',
        (Gender.MALE[0], ColorHair.BROWN[0], ColorEye.GREEN[0]): 'Стефан Руссо',
        (Gender.MALE[0], ColorHair.BLONDE[0], ColorEye.BROWN[0]): 'Хит Леджер',
        (Gender.MALE[0], ColorHair.BLONDE[0], ColorEye.LIGHT_BLUE[0]): 'Николай Басков',
        (Gender.MALE[0], ColorHair.BLONDE[0], ColorEye.GREEN[0]): 'Лэйрд Хэмилтон',
        (Gender.MALE[0], ColorHair.RED[0], ColorEye.BROWN[0]): 'Андрей Григорьев-Апполонов',
        (Gender.MALE[0], ColorHair.RED[0], ColorEye.LIGHT_BLUE[0]): 'Бенедикт Камбербэтч',
        (Gender.MALE[0], ColorHair.RED[0], ColorEye.GREEN[0]): 'Руперт Гринт',
        (Gender.FEMALE[0], ColorHair.BROWN[0], ColorEye.BROWN[0]): 'Хейли Макфарланд',
        (Gender.FEMALE[0], ColorHair.BROWN[0], ColorEye.LIGHT_BLUE[0]): 'Иззи Стил',
        (Gender.FEMALE[0], ColorHair.BROWN[0], ColorEye.GREEN[0]): 'Пейдж Спара',
        (Gender.FEMALE[0], ColorHair.BLONDE[0], ColorEye.BROWN[0]): 'Тай Лоусон',
        (Gender.FEMALE[0], ColorHair.BLONDE[0], ColorEye.LIGHT_BLUE[0]): 'Алина Ковалевская',
        (Gender.FEMALE[0], ColorHair.BLONDE[0], ColorEye.GREEN[0]): 'Сорайя Арнелас',
        (Gender.FEMALE[0], ColorHair.RED[0], ColorEye.BROWN[0]): 'Айла Фишер',
        (Gender.FEMALE[0], ColorHair.RED[0], ColorEye.LIGHT_BLUE[0]): 'Николь Кидман',
        (Gender.FEMALE[0], ColorHair.RED[0], ColorEye.GREEN[0]): 'Джессика Честейн',
    }

    def __init__(self, gender, color_eye, color_hair):
        self.gender = gender
        self.color_eye = color_eye
        self.color_hair = color_hair

    def get_celebrity(self):
        return self.CELEBRITIES[(self.gender, self.color_hair, self.color_eye)]


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        cursor = conn.cursor()
        cursor.execute(f'select * from users where chat_id = {message.from_user.id}')
        user_data = get_elements_as_dict(cursor)
        if user_data and user_data[0].get('celebrity_id'):
            cursor.execute(f'select * from users join celebrities on users.celebrity_id = celebrities.id')
            user_data = get_elements_as_dict(cursor)
            message_text = f'По вашим прошлым данным вы -- {user_data[0]["name"]}.'

            keyboard = types.InlineKeyboardMarkup()
            key_yes = types.InlineKeyboardButton(text='Пройти ещё раз', callback_data='again')
            keyboard.add(key_yes)

            bot.send_photo(
                message.from_user.id,
                user_data[0]['url_photo'],
                caption=message_text,
                reply_markup=keyboard,
            )
            return

        if not user_data:
            cursor.execute(f'insert into users (chat_id) values ({message.from_user.id})')
            conn.commit()

        message_text = 'Приступим. Какой у вас пол?'

        keyboard = types.InlineKeyboardMarkup()
        key_male = types.InlineKeyboardButton(text=Gender.MALE[1], callback_data=Gender.MALE[0])
        keyboard.add(key_male)
        key_female = types.InlineKeyboardButton(text=Gender.FEMALE[1], callback_data=Gender.FEMALE[0])
        keyboard.add(key_female)

        bot.send_message(message.from_user.id, message_text, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Напишите /start.')


@bot.callback_query_handler(func=lambda call: call.data in Gender.ALL_GENDERS)
def callback_worker_save_gender(call):
    cursor = conn.cursor()
    cursor.execute(f'update users set gender = \'{call.data}\' where chat_id = {call.from_user.id}')
    conn.commit()
    message_text = 'Хорошо. Какой у вас цвет волос?'
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_brown = types.InlineKeyboardButton(text=ColorHair.BROWN[1], callback_data=ColorHair.BROWN[0])
    keyboard.add(key_brown)
    key_red = types.InlineKeyboardButton(text=ColorHair.RED[1], callback_data=ColorHair.RED[0])
    keyboard.add(key_red)
    key_blonde = types.InlineKeyboardButton(text=ColorHair.BLONDE[1], callback_data=ColorHair.BLONDE[0])
    keyboard.add(key_blonde)
    bot.send_message(call.from_user.id, message_text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in ColorHair.ALL_COLORS)
def callback_worker_save_color_hair(call):
    cursor = conn.cursor()
    cursor.execute(f'update users set hair = \'{call.data}\' where chat_id = {call.from_user.id}')
    conn.commit()
    # r_con.hset(REDIS_KEY.format(call.from_user.id), 'hair', call.data)
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_brown = types.InlineKeyboardButton(text=ColorEye.BROWN[1], callback_data=ColorEye.BROWN[0])
    keyboard.add(key_brown)
    key_green = types.InlineKeyboardButton(text=ColorEye.GREEN[1], callback_data=ColorEye.GREEN[0])
    keyboard.add(key_green)
    key_light_blue = types.InlineKeyboardButton(text=ColorEye.LIGHT_BLUE[1], callback_data=ColorEye.LIGHT_BLUE[0])
    keyboard.add(key_light_blue)
    bot.send_message(call.from_user.id, 'Отлично! Какой у вас цвет глаз?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in ColorEye.ALL_COLORS)
def callback_worker_save_color_eye(call):
    cursor = conn.cursor()
    cursor.execute(f'update users set eye = \'{call.data}\' where chat_id = {call.from_user.id}')
    conn.commit()
    cursor.execute(f'select * from users where chat_id = {call.from_user.id}')
    user_data = get_elements_as_dict(cursor)[0]
    person = PersonData(user_data['gender'], user_data['eye'], user_data['hair'])
    celebrity = person.get_celebrity()
    cursor.execute(f'select * from celebrities where name = \'{celebrity}\'')
    celebrity_data = get_elements_as_dict(cursor)[0]
    cursor.execute(f'update users set celebrity_id = {celebrity_data["id"]} where chat_id = {call.from_user.id}')
    conn.commit()
    message_text = f'Прекрасно! По предоставленным данным вы -- {celebrity}.'
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Пройти ещё раз', callback_data='again')
    keyboard.add(key_yes)
    bot.send_photo(
        call.from_user.id,
        celebrity_data['url_photo'],
        caption=message_text,
        reply_markup=keyboard,
    )


@bot.callback_query_handler(func=lambda call: call.data == 'again')
def callback_worker_remove_result(call):
    cursor = conn.cursor()
    try:
        cursor.execute(f'delete from users where chat_id = {call.from_user.id}')
    except Exception:
        bot.send_message(call.from_user.id, 'Вы уже очистили свою историю. Напишите /start.')

    conn.commit()
    bot.send_message(call.from_user.id, 'Готово. Напишите /start ещё раз.')


bot.polling(none_stop=True, interval=1)

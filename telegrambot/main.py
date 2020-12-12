import telebot


bot = telebot.TeleBot('1417561064:AAElcSDCcwsL791l3wiJlqUTJVk4MwF7Rrc')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет! Я помогу тебе найти необходимую информацию о поступлении.\n' \
                                     '\n' \
                                     'Чтобы узнать больше, нажми /info')

@bot.message_handler(commands=['info'])
def info_message(message):
    key = telebot.types.InlineKeyboardMarkup()
    key.add(telebot.types.InlineKeyboardButton(text='Проходные баллы прошлых лет', callback_data=1))
    key.add(telebot.types.InlineKeyboardButton(text='Перейти в личный кабинет абитуриента', url='https://lk.mai.ru/login'))
    key.add(telebot.types.InlineKeyboardButton(text='Список документов для поступления в магистратуру', callback_data=2))
    bot.send_message(message.chat.id, text="Нажми на одну из кнопок, чтобы получить интересующую информацию", reply_markup=key)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    answer = ''
    if call.data == '1':
        answer = 'Отправь мне номер направления, чтобы узнать проходные баллы:\n' \
                 '\n' \
                 '01.04.02 — Прикладная математика и информатика\n' \
                 '09.04.01 — Информатика и вычислительная техника\n' \
                 '22.04.01 — Материаловедение и технологии материалов\n' \
                 '24.04.04 — Авиастроение'
    elif call.data == '2':
        answer = 'Для поступления в магистратуру МАИ тебе необходимо предоставить в приёмную комиссию следующие документы:\n' \
                 '\n' \
                 '✔ Заявление и согласие на обработку персональных данных\n' \
                 '\n' \
                 '✔ Паспорт (документ, удостоверяющий личность и гражданство)\n' \
                 '\n' \
                 '✔ Копия паспорта\n' \
                 '\n' \
                 '✔ Диплом о высшем образовании (оригинал или ксерокопия документа гособразца об образовании)\n' \
                 '\n' \
                 '✔ 4 цветных фото размером 3х4\n' \
                 '\n' \
                 '✔ Документы, подтверждающие индивидуальные достижения и/или особые права'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "01.04.02":
        bot.send_message(message.from_user.id, "Проходной балл за 2019 год: 79\n"
                                               "Проходной балл за 2020 год: 81")
    elif message.text == "09.04.01":
        bot.send_message(message.from_user.id, "Проходной балл за 2019 год: 83\n"
                                               "Проходной балл за 2020 год: 85")

    elif message.text == "22.04.01":
        bot.send_message(message.from_user.id, "Проходной балл за 2019 год: 68\n"
                                               "Проходной балл за 2020 год: 70")

    elif message.text == "24.04.04":
        bot.send_message(message.from_user.id, "Проходной балл за 2019 год: 77\n"
                                               "Проходной балл за 2020 год: 80")
    else :
        bot.send_message(message.from_user.id, "Я тебя не понимаю.\n"
                                               "Чтобы узнать проходные баллы, пожалуйста, напиши мне еще раз.")


if __name__ == '__main__':
     bot.infinity_polling()
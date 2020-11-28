import telebot


bot = telebot.TeleBot('1417561064:AAElcSDCcwsL791l3wiJlqUTJVk4MwF7Rrc')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет! Я помогу тебе узнать необходимую информацию о поступлении\n' \
                                     '\n' \
                                     'Чтобы узнать больше, нажми /info')

@bot.message_handler(commands=['info'])
def info_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Проходные баллы прошлых лет', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Перейти в личный кабинет абитуриента', url='https://lk.mai.ru/login'))
    markup.add(telebot.types.InlineKeyboardButton(text='Список документов для поступления в магистратуру', callback_data=3))
    bot.send_message(message.chat.id, text="Нажми на одну из кнопок, чтобы получить интересующую информацию", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    answer = ''
    if call.data == '1':
        answer = '333'

    elif call.data == '3':
        answer = '✔ Заявление и согласие на обработку персональных данных\n' \
                 '\n' \
                 '✔ Паспорт (документ, удостоверяющий личность и гражданство)\n' \
                 '\n' \
                 '✔ Копия паспорта\n' \
                 '\n' \
                 '✔Диплом о высшем образовании (оригинал или ксерокопия документа гособразца об образовании)\n' \
                 '\n' \
                 '✔ 4 цветных фото размером 3х4\n' \
                 '\n' \
                 '✔ Документы, подтверждающие индивидуальные достижения и/или особые права'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

if __name__ == '__main__':
     bot.infinity_polling()
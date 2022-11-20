import telebot
import os

bot = telebot.TeleBot('5924752296:AAFNjfGDbqI7PfMjUIN1cEcd9Px9i9D3DFs')

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('ДА', 'НЕТ')

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('начать')

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('100', '500', '1000')
keyboard.row('2500', '5000', 'получить')
keyboard.row('получить исходник', 'выключить компьютер', 'назад')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Бот запущен</b>', parse_mode='html')
    bot.send_message(message.chat.id, '<b>Связь успешно установленна</b>', parse_mode='html', reply_markup = keyboard1)



@bot.message_handler()
def get_user_txt(message):
    if message.text == 'начать':
        bot.send_message(message.chat.id, '<b>Укажите радиус</b>', parse_mode='html', reply_markup = keyboard)
    if message.text == 'назад':
        bot.send_message(message.chat.id, 'Для продолжения нажмите "начать"', parse_mode='html', reply_markup = keyboard1)
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'ок', parse_mode='html', reply_markup = keyboard1)
        os.system('shutdown /p /f')
    if message.text == 'НЕТ':
        bot.send_message(message.chat.id, 'Для продолжения нажмите "начать"', parse_mode='html', reply_markup = keyboard1)
    if message.text == 'выключить компьютер':
        bot.send_message(message.chat.id, 'Точно?', parse_mode='html', reply_markup = keyboard2)
#    if message.text == 'получить исходник':
#        bot.send_message(message.chat.id, 'Точно?', parse_mode='html')
    if message.text == 'получить':
        try:
            with open("text.txt", mode='rt', encoding="UTF-8") as f:
                for row in f:
                    bot.send_message(message.chat.id, row, parse_mode='html')

            # text_st = open('text.txt', 'r')
            # text_st = text_st.readlines()
            # #text_st = [i.split(';;') for i in text_st.readlines()]
            # print(text_st)
            # for row in text_st:
            #     bot.send_message(message.chat.id, row, parse_mode='html')
        except:
            bot.send_message(message.chat.id, '<b>нет данных</b>', parse_mode='html')



bot.polling(none_stop = True)
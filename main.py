#!/usr/bin/env python
import telebot
import constants
import sys
import os
import json
from botanio import botan
botan_key = "5c68ded3-3a98-4523-bdcf-b553454037ba"
uid='message.from_user'
message_dict='message.to_dict()'
event_name='update.message.text'
print (botan.track(botan_key, uid, event_name))
TRACK_URL = 'https://api.botan.io/track'
from telebot import types
bot = telebot.TeleBot(constants.token)
def make_json(message):
    data = {}
    data['message_id'] = message.message_id
    data['from'] = {}
    data['from']['id'] = message.from_user.id
    if message.from_user.username is not None:
        data['from']['username'] = message.from_user.username
    data['chat'] = {}
    # Chat.Id используется в обоих типах чатов
    data['chat']['id'] = message.chat.id
    return data
def track(token, uid, message, name='Message'):
    try:
        r = requests.post(
            TRACK_URL,
            params={"token": token, "uid": uid, "name": name},
            data=make_json(message),
            headers={'Content-type': 'application/json'},
        )
        return r.json()
    except requests.exceptions.Timeout:
        # set up for a retry, or continue in a retry loop
        return False
    except (requests.exceptions.RequestException, ValueError) as e:
        # catastrophic error
        print(e)
        return False
bot.remove_webhook()
#   bot.send_message(97111096, "test")

#   upd = bot.get_updates()
#   print(upd)

#   last_upd = upd[-1]
#   message_from_user = last_upd.message
#   print(message_from_user)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Кафель', 'Сантехника')
    user_markup.row('Аксессуар', 'Смеситель')
    user_markup.row('Ванна', 'Контакты')
    bot.send_message(message.from_user.id, 'Выберите раздел', reply_markup=user_markup)
    botan.track(botan_key, uid, event_name, 'start')

@bot.message_handler(func=lambda message: message.text=="Кафель")
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Назад')
    user_markup.row('Provence', 'Inside')
    user_markup.row('Celebration', 'Deja Vu')
    user_markup.row('Vintage', 'Pera')
    bot.send_message(message.from_user.id, 'Выберите коллекцию', reply_markup=user_markup)
    botan.track(botan_key, uid, event_name, 'Кафель')

@bot.message_handler(func=lambda message: message.text=="Сантехника")
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Назад')
    user_markup.row('Раковина', 'Унитаз')
    user_markup.row('Биде')
    bot.send_message(message.from_user.id, 'Выберите коллекцию', reply_markup=user_markup)
    botan.track(botan_key, uid, event_name, 'Сантехника')

@bot.message_handler(func=lambda message: message.text=="Аксессуар")
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Назад')
    user_markup.row('Istanbul', 'Matrix')
    user_markup.row('Somnia', 'Nest Trendy')
    user_markup.row('Juno Swarovski')
    bot.send_message(message.from_user.id, 'Выберите коллекцию', reply_markup=user_markup)
    botan.track(botan_key, uid, event_name, 'Аксессуар')

@bot.message_handler(func=lambda message: message.text=="Смеситель")
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Назад')
    user_markup.row('Istаnbul', 'Q-Line')
    user_markup.row('Style-X', 'T4')
    user_markup.row('Juno', 'Z-Line')
    bot.send_message(message.from_user.id, 'Выберите коллекцию', reply_markup=user_markup)
    botan.track(botan_key, uid, event_name, 'Смеситель')

@bot.message_handler(func=lambda message: message.text=="Ванна")
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Назад')
    user_markup.row('Т4', 'Silence')
    user_markup.row('Neon', 'Balance')
    user_markup.row('Comfort', 'Combo')
    bot.send_message(message.from_user.id, 'Выберите коллекцию', reply_markup=user_markup)
    botan.track(botan_key, uid, event_name, 'Ванна')

@bot.message_handler(func=lambda message: message.text=="Контакты")
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Назад')
    user_markup.row('Кoнтакты', 'Локация', 'VitrA')
    bot.send_message(message.from_user.id, 'Выберите подраздел', reply_markup=user_markup)
    botan.track(botan_key, uid, event_name, 'Контакты')

@bot.message_handler(func=lambda message: message.text=="Назад")
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Кафель', 'Сантехника')
    user_markup.row('Аксессуар', 'Смеситель')
    user_markup.row('Ванна', 'Контакты')
    bot.send_message(message.from_user.id, 'Выберите раздел', reply_markup=user_markup)
    botan.track(botan_key, uid, event_name, 'Назад')



@bot.message_handler(content_types=['text'])
def handle_text(message):
        if message.text == 'Deja Vu':
            directory = 'D:/Telebot/tiles/Deja Vu'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на кафели", url="http://vitra.uz/category/плитка/керамогранит")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о кафеле.", reply_markup=keyboard)
        if message.text == 'Vintage':
            directory = 'D:/Telebot/tiles/Vintage'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на кафели", url="http://vitra.uz/category/плитка/керамогранит")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о кафеле.", reply_markup=keyboard)
        if message.text == 'Pera':
            directory = 'D:/Telebot/tiles/Pera'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на кафели", url="http://vitra.uz/category/плитка/керамогранит")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о кафеле.", reply_markup=keyboard)
        if message.text == 'Inside':
            directory = 'D:/Telebot/tiles/Inside'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на кафели", url="http://vitra.uz/category/плитка/керамогранит")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о кафеле.", reply_markup=keyboard)
        if message.text == 'Celebration':
            directory = 'D:/Telebot/tiles/Celebration'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на кафели", url="http://vitra.uz/category/плитка/керамогранит")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о кафеле.", reply_markup=keyboard)
        if message.text == 'Provence':
            directory = 'D:/Telebot/tiles/Provence'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на кафели", url="http://vitra.uz/category/плитка/керамогранит")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о кафеле.", reply_markup=keyboard)
        if message.text == 'Раковина':
            directory = 'D:/Telebot/tiles/Раковина'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел раковин", url="http://vitra.uz/category/санитарная-керамика/раковины")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о сантехике.", reply_markup=keyboard)
        if message.text == 'Биде':
            directory = 'D:/Telebot/tiles/Биде'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел биде", url="http://vitra.uz/category/санитарная-керамика/биде")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о сантехике.", reply_markup=keyboard)
        if message.text == 'Унитаз':
            directory = 'D:/Telebot/tiles/Унитаз'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел унитаз", url="http://vitra.uz/category/санитарная-керамика/унитаз")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о сантехике.", reply_markup=keyboard)
        if message.text == 'Juno Swarovski':
            directory = 'D:/Telebot/tiles/Juno Swarovski'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел аксессуаров", url="http://vitra.uz/category/смесители-и-душевые-системы/аксессуары")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация об аксессуаре.", reply_markup=keyboard)
        if message.text == 'Somnia':
            directory = 'D:/Telebot/tiles/Somnia'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел аксессуаров", url="http://vitra.uz/category/смесители-и-душевые-системы/аксессуары")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация об аксессуаре.", reply_markup=keyboard)
        if message.text == 'Nest Trendy':
            directory = 'D:/Telebot/tiles/Nest Trendy'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел аксессуаров", url="http://vitra.uz/category/смесители-и-душевые-системы/аксессуары")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация об аксессуаре.", reply_markup=keyboard)
        if message.text == 'Istanbul':
            directory = 'D:/Telebot/tiles/Istanbul'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел аксессуаров", url="http://vitra.uz/category/смесители-и-душевые-системы/аксессуары")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация об аксессуаре.", reply_markup=keyboard)
        if message.text == 'Matrix':
            directory = 'D:/Telebot/tiles/Matrix'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел аксессуаров", url="http://vitra.uz/category/смесители-и-душевые-системы/аксессуары")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация об аксессуаре.", reply_markup=keyboard)
        if message.text == 'Istаnbul':
            directory = 'D:/Telebot/tiles/Istаnbul'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел смесителей", url="http://vitra.uz/category/смесители-и-душевые-системы/смеситель")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о смесителе.", reply_markup=keyboard)
        if message.text == 'Style-X':
            directory = 'D:/Telebot/tiles/Style-X'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел смесителей", url="http://vitra.uz/category/смесители-и-душевые-системы/смеситель")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о смесителе.", reply_markup=keyboard)
        if message.text == 'Q-Line':
            directory = 'D:/Telebot/tiles/Q-Line'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел смесителей", url="http://vitra.uz/category/смесители-и-душевые-системы/смеситель")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о смесителе.", reply_markup=keyboard)
        if message.text == 'T4':
            directory = 'D:/Telebot/tiles/T4'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел смесителей", url="http://vitra.uz/category/смесители-и-душевые-системы/смеситель")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о смесителе.", reply_markup=keyboard)
        if message.text == 'Juno':
            directory = 'D:/Telebot/tiles/Juno'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел смесителей", url="http://vitra.uz/category/смесители-и-душевые-системы/смеситель")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о смесителе.", reply_markup=keyboard)
        if message.text == 'Z-Line':
            directory = 'D:/Telebot/tiles/Z-line'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел смесителей", url="http://vitra.uz/category/смесители-и-душевые-системы/смеситель")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о смесителе.", reply_markup=keyboard)
        if message.text == 'Silence':
            directory = 'D:/Telebot/tiles/Silence'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел ванн", url="http://vitra.uz/category/vanna/")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о ваннах.", reply_markup=keyboard)
        if message.text == 'Т4':
            directory = 'D:/Telebot/tiles/Т4'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел ванн", url="http://vitra.uz/category/vanna/")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о ваннах.", reply_markup=keyboard)
        if message.text == 'Combo':
            directory = 'D:/Telebot/tiles/Combo'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел ванн", url="http://vitra.uz/category/vanna/")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о ваннах.", reply_markup=keyboard)
        if message.text == 'Balance':
            directory = 'D:/Telebot/tiles/Balance'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел ванн", url="http://vitra.uz/category/vanna/")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о ваннах.", reply_markup=keyboard)
        if message.text == 'Neon':
            directory = 'D:/Telebot/tiles/Neon'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел ванн", url="http://vitra.uz/category/vanna/")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о ваннах.", reply_markup=keyboard)
        if message.text == 'Comfort':
            directory = 'D:/Telebot/tiles/Comfort'
            all_files_in_directory = os.listdir(directory)
            print(all_files_in_directory)
            for file in all_files_in_directory:
                img = open(directory + '/' + file, 'rb')
                bot.send_chat_action(message.from_user.id, 'upload_photo')
                bot.send_photo(message.chat.id, img)
                img.close()
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на раздел ванн", url="http://vitra.uz/category/vanna/")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Более подробная информация о ваннах.", reply_markup=keyboard)
        if message.text == 'Кoнтакты':
            bot.send_message(message.from_user.id, "Tel.: +99871252-75-00")
            bot.send_message(message.from_user.id, "Tel.: +99871252-76-00")
            bot.send_message(message.from_user.id, "e-mail:   info@vitra.uz")
        if message.text == 'Локация':
            bot.send_chat_action(message.from_user.id, 'find_location')
            bot.send_location(message.from_user.id, 41.3031089, 69.2677359)
        if message.text == 'VitrA':
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти на сайт", url="http://vitra.uz")
            keyboard.add(url_button)
            url_button = types.InlineKeyboardButton(text="Перейти на Facebook", url="https://www.facebook.com/vitrauzbekistan/")
            keyboard.add(url_button)
            url_button = types.InlineKeyboardButton(text="Перейти на Instagram", url="https://www.instagram.com/vitra_uzbekistan/")
            keyboard.add(url_button)
            url_button = types.InlineKeyboardButton(text="Перейти на YouTube", url="https://www.youtube.com/channel/UCeJAH_adnkwSo6Le8ldamAg")
            keyboard.add(url_button)
            url_button = types.InlineKeyboardButton(text="Присоеденится на канал", url="https://telegram.me/vitrauzbekistan")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Ссылки на Социальные сети.", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)
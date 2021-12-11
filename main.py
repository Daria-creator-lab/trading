import pandas as pd
# import numpy as np
# import csv
# import os
import re

import_file = pd.read_csv(r'/Users/dary/Desktop/stocks_c.csv', sep=';', engine='python', encoding='utf-8-sig',
                          error_bad_lines=False)
headers = pd.read_csv(r'/Users/dary/Desktop/stocks_c.csv', nrows=0).columns.tolist()
columns_t = ['Ticker']
columns_p = ['Price']

tickers_t = pd.read_csv(r'/Users/dary/Desktop/stocks_c.csv', usecols=columns_t, sep=';')
# print(type(tickers_t))
list_of_tickers = []
for row in tickers_t.itertuples():
    list_of_tickers.append(row)

tickers_p = pd.read_csv(r'/Users/dary/Desktop/stocks_c.csv', usecols=columns_p, sep=';')
# print(type(tickers_p))
list_of_price = []
for row in tickers_p.itertuples():
    list_of_price.append(row)

print(list_of_tickers)
# print(list_of_price)
# print(tickers_p.loc[0])
print(str(tickers_p.loc[0]).split('\n')[0])


import telebot

token = r"2074679904:AAEkoTRdfSitln0Htnx-v0DbNTPJndpVWrY"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Этот бот поможет найти информацию об акциях S&P500")
        bot.send_message(message.from_user.id, "Введите тикер акции ")
        bot.register_next_step_handler(message, main_function)
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Этот бот поможет найти информацию об акциях S&P500")
        bot.send_message(message.from_user.id, "Введите тикер акции ")
        bot.register_next_step_handler(message, main_function)
    elif re.match(r'[A-Z]{1,5}', message.text) is not None:
        bot.register_next_step_handler(message, main_function)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")




def main_function(message):
    global stock_ticker
    stock_ticker = message.text
    match_found = False
    for i in range(454):
        if stock_ticker in list_of_tickers[i]:
            ticker_price = str(tickers_p.loc[0]).split('\n')[0]
            print(ticker_price)
            bot.send_message(message.from_user.id, stock_ticker + '\n' + ticker_price)
            print("in process")
            match_found = True
            break
    if match_found == False:
        bot.send_message(message.from_user.id, "Такой тикер не найден, проверьте правильность ввода")


# bot.polling(none_stop=True, interval=0)
# while True:
#     try:
#         bot.polling(none_stop=True)
#
#     except Exception as e:
#         logger.error(e)  # или просто print(e) если у вас логгера нет,
#         # или import traceback; traceback.print_exc() для печати полной инфы
#         time.sleep(15)

# # создание таблицы
# import httplib2
# # import apiclient.discovery
# from googleapiclient.discovery import build
# from oauth2client.service_account import ServiceAccountCredentials
# CREDENTIALS_FILE = r'stock-329411-201f237c77cd.json'  # Имя файла с закрытым ключом, вы должны подставить свое
#
# # Читаем ключи из файла
# credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, [r'https://www.googleapis.com/auth/spreadsheets', r'https://www.googleapis.com/auth/drive'])
# httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
# # service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API
# service = build('sheets', 'v4', http = httpAuth)
# spreadsheet = service.spreadsheets().create(body = {
#     'properties': {'title': 'Первый тестовый документ', 'locale': 'ru_RU'},
#     'sheets': [{'properties': {'sheetType': 'GRID',
#                                'sheetId': 0,
#                                'title': 'Лист номер один',
#                                'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
# }).execute()
# spreadsheetId = spreadsheet['spreadsheetId'] # сохраняем идентификатор файла
# print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)
#
# # разрешаем доступ к таблице
# # driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
# driveService = build('drive', 'v3', http = httpAuth)
# access = driveService.permissions().create(
#     fileId = spreadsheetId,
#     body = {'type': 'user', 'role': 'writer', 'emailAddress': 'dasha.me07@gmail.com'},  # Открываем доступ на редактирование
#     fields = 'id'
# ).execute()
# # Получаем список листов, их Id и название
# spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
# sheetList = spreadsheet.get('sheets')
# for sheet in sheetList:
#     print(sheet['properties']['sheetId'], sheet['properties']['title'])
#
# sheetId = sheetList[0]['properties']['sheetId']
#
# print('Мы будем использовать лист с Id = ', sheetId)
#
# # results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
# #     "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
# #     "data": [
# #         {"range": "Лист номер один!B1:C1",
# #          "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
# #          "values": [
# #                     ["1", "2"], # Заполняем первую строку
# #                    ]}
# #     ]
# # }).execute()
#
# # чтение данных из таблицы
# ranges = ["Лист номер один!A1:A100"]#454
#
# results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
#                                                    ranges=ranges,
#                                                    valueRenderOption='FORMATTED_VALUE',
#                                                    dateTimeRenderOption='FORMATTED_STRING').execute()
# # columns = results['values'][0]
# # data = results['values'][1]
# # df = pd.DataFrame(data, columns = columns)
# # print(df)
#
# # sheet_values = results['valueRanges'][0]['values']
# # print(sheet_values)
# print(results)


import config
import telebot
import requests
from telebot import types

bot = telebot.TeleBot(config.token)



# Рабочий скрипт на отправку погоды из openweathermap


@bot.message_handler(commands = ['start', 'help'])

def welcome_mess(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Погода', 'Помощ']])  # не работает без ' * '
    bot.send_message(message.chat.id, 'Привет! \n   Я знаю какая сегодня погода!\n  Используй команду ''/weather'' чтобы включить inline клавиатуру',
    reply_markup = keyboard)




# inline клавиатура

@bot.message_handler(commands = ['weather'])
def weather(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name)
                                              for name in ['Киев', 'Львов', 'Амстердам']])

    msg = bot.send_message(message.chat.id, 'Выбери город:',
                           reply_markup= keyboard)

@bot.callback_query_handler(func=lambda call: True)

def inline(call):
    if call.data =='Киев':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text= 'Львов')

    elif call.data == 'Львов':
        bot.edit_message_text(
            chat_id= call.message.chat.id,
            message_id= call.message.message_id,
            text= 'Киев')

    elif call.data == 'Амстердам':
        bot.edit_message_text(
        chat_id= call.message.chat.id,
        message_id= call.message.message_id,
        text= 'Рай'
    )


# Reply клавиатура
@bot.message_handler(regexp = 'weather')
@bot.message_handler(regexp = 'погода')
@bot.message_handler(regexp = 'главная')


def weather(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Киев', 'Львов', 'Амстердам']])  # не работает без ' * '
    bot.send_message(message.chat.id, 'Выбери город',
                     reply_markup = keyboard)

@bot.message_handler(regexp = 'помощ')

def welcome_mess(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    keyboard.add(*[types.KeyboardButton('Проблема №1')])
    keyboard.add(*[types.KeyboardButton('Проблема №2')])
    keyboard.add(*[types.KeyboardButton('Проблема №3')])
    keyboard.add(*[types.KeyboardButton('Проблема №4')])
    keyboard.add(*[types.KeyboardButton('Проблема №5')])
    keyboard.add(*[types.KeyboardButton(name) for name in ['/start',]])  # не работает без ' * '

    bot.send_message(message.chat.id, 'Что-то пошло не так? \n Выбери из списка свою проблему:',
                     reply_markup = keyboard)

# -------------------------------------------------------------Kiev----------------------


@bot.message_handler(regexp = 'киев')
@bot.message_handler(regexp = 'kiev')

def send_weather(message):

    appid = '774067f0788f99bd70a5f48059ea0998'

    s_city = 'kiev'

    r = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

    try:

        r = requests.get("http://api.openweathermap.org/data/2.5/find",
                         params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

        data = r.json()

        cities = ['{} ({})'.format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print('Город: ', cities)

        city_id = data['list'][0]['id']
        print('id Города = ', city_id)

    except Exeption as e:
        print('Exeption (find): ', e)
        pass
        
        
    bot.send_message(message.chat.id, cities)
    #bot.send_message(message.chat.id, city_id)

    try:

        res = requests.get('http://api.openweathermap.org/data/2.5/weather',
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

        data = res.json()
        weat = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']

        print('Погода: ', weat)
        print('Температура: ', temp)
        print('Температура минимум: ', temp_min)
        print('Температура максимум: ', temp_max)


    except Exeption as e:
        print('Exeption (weather):', e)
        pass


    bot.send_message(message.chat.id, 'Погода: {}'.format(weat))
    bot.send_message(message.chat.id, 'Средняя температура: {}'.format(temp))
    bot.send_message(message.chat.id, 'Температура мин: {}'.format(temp_min))
    bot.send_message(message.chat.id, 'Температура макс: {}'.format(temp_max))

    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['/start']])  # не работает без ' * '
        bot.send_message(message.chat.id,'-', reply_markup=keyboard)

    except Exeption as e:
        print('Exeption (weather):', e)
        pass





#--------------------------------------Львов---------------------------------------------------

@bot.message_handler(regexp='lviv')
@bot.message_handler(regexp='львов')
@bot.message_handler(regexp='львів')

def send_weather(message):
    appid = '774067f0788f99bd70a5f48059ea0998'

    s_city = 'lviv'

    r = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

    try:

        r = requests.get("http://api.openweathermap.org/data/2.5/find",
                         params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

        data = r.json()

        cities = ['{} ({})'.format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print('Город: ', cities)

        city_id = data['list'][0]['id']
        print('id Города = ', city_id)

    except Exeption as e:
        print('Exeption (find): ', e)
        pass

    bot.send_message(message.chat.id, cities)
    # bot.send_message(message.chat.id, city_id)

    try:

        res = requests.get('http://api.openweathermap.org/data/2.5/weather',
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

        data = res.json()
        weat = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']

        print('Погода: ', weat)
        print('Температура: ', temp)
        print('Температура минимум: ', temp_min)
        print('Температура максимум: ', temp_max)


    except Exeption as e:
        print('Exeption (weather):', e)
        pass

    bot.send_message(message.chat.id, 'Погода: {}'.format(weat))
    bot.send_message(message.chat.id, 'Средняя температура: {}'.format(temp))
    bot.send_message(message.chat.id, 'Температура мин: {}'.format(temp_min))
    bot.send_message(message.chat.id, 'Температура макс: {}'.format(temp_max))


    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['/start']])  # не работает без ' * '
        bot.send_message(message.chat.id,'-', reply_markup=keyboard)

    except Exeption as e:
        print('Exeption (weather):', e)
        pass


#--------------------------------------Амстердам---------------------------------------------------

@bot.message_handler(regexp='Amsterdam')
@bot.message_handler(regexp='Амстердам')

def send_weather(message):
    appid = '774067f0788f99bd70a5f48059ea0998'

    s_city = 'amsterdam'

    r = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

    try:

        r = requests.get("http://api.openweathermap.org/data/2.5/find",
                         params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

        data = r.json()

        cities = ['{} ({})'.format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print('Город: ', cities)

        city_id = data['list'][0]['id']
        print('id Города = ', city_id)

    except Exeption as e:
        print('Exeption (find): ', e)
        pass

    bot.send_message(message.chat.id, cities)
    # bot.send_message(message.chat.id, city_id)

    try:

        res = requests.get('http://api.openweathermap.org/data/2.5/weather',
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

        data = res.json()
        weat = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']

        print('Погода: ', weat)
        print('Температура: ', temp)
        print('Температура минимум: ', temp_min)
        print('Температура максимум: ', temp_max)


    except Exeption as e:
        print('Exeption (weather):', e)
        pass

    bot.send_message(message.chat.id, 'Погода: {}'.format(weat))
    bot.send_message(message.chat.id, 'Средняя температура: {}'.format(temp))
    bot.send_message(message.chat.id, 'Температура мин: {}'.format(temp_min))
    bot.send_message(message.chat.id, 'Температура макс: {}'.format(temp_max))


    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['/start']])  # не работает без ' * '
        bot.send_message(message.chat.id,'-', reply_markup=keyboard)

    except Exeption as e:
        print('Exeption (weather):', e)
        pass




if __name__ == '__main__':
   main()


   # bot.polling(none_stop = True, interval=1)
    





'''
перекидівает в телеграм информацию НО на любое слово (Не привязан к запросу)

@bot.message_handler (content_types = ['text'])

def send_city (message):

    appid = '774067f0788f99bd70a5f48059ea0998'

    s_city = 'Kiev'


    r = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

    try:

        r = requests.get("http://api.openweathermap.org/data/2.5/find",
                         params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

        data = r.json()

        cities = ['{} ({})'.format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print('Город: ', cities)

        city_id = data['list'][0]['id']
        print('id Города = ', city_id)

    except Exeption as e:
        print('Exeption (find): ', e)
        pass
    bot.send_message(message.chat.id, cities)
    bot.send_message(message.chat.id, city_id)

    try:

        res = requests.get('http://api.openweathermap.org/data/2.5/weather',
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

        data = res.json()

        weat = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']

    except Exeption as e:
        print('Exeption (weather):', e)
        pass

    bot.send_message(message.chat.id, weat)
    bot.send_message(message.chat.id, temp)
    bot.send_message(message.chat.id,('Min:',temp_min))
    bot.send_message(message.chat.id, temp_max)
'''



'''   

--------------> parse json in readeble form (with import simplejson)


r = requests.get(url + token + '/getUpdates')
print (r.json())  # не обязательно


form = simplejson.dumps(r.json(),sort_keys= True, indent=4)
print(form)


--------------> Repeating all messages 

@bot.message_handler(content_types = ['text'])


def repeat_all_messages (message):
    bot.send_message(message.chat.id, message.text)

--------------> long polling

if __name__ == '__main__':
    bot.polling(none_stop = True, interval = 1)
    

--------------> Эхо (повторюха)

@bot.message_handler(content_types = ['text'])

def echo (message):
    bot.send_message(message.chat.id, message.text)

   
    
    
#  -----> Установка  Reply keyboard



from telebot import types

# Reply клавиатура
1)  @bot.message_handler(commands = ['weather','погода'])

def weather(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Киев', 'Одесса', 'Харьков']])  # не работает без ' * '
    bot.send_message(message.chat.id, 'Выбери город',
                     reply_markup = keyboard)

2) @bot.message_handler(content_types = ['text'])

def reply_keyboard(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('first letter', 'second letter')
    markup.row('c', 'Third lett', 'e')
    bot.send_message(message.chat.id, 'choose one letter', reply_markup=markup)


----------------------Inline клавиатура (пока не смог настроить что бы были функции как у replykeyboard)-------------------


@bot.message_handler(commands = ['weather','погода'])

def weather(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text = name, callback_data = name ) for name in
                   ['Киев', 'Одесса']])
    msg = bot.send_message(message.chat.id, 'Выбери город', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda c: True)

def inline(c):
    if c.data == 'Киев':
        bot.send_message(c.message.chat.id, )
    elif c.data == 'Oдесса':
        bot.send_message(c.message.chat.id, 'Одесса')



'''
import telebot
import requests
import json

TELEGRAM_API_KEY = '6121768016:AAE4QKucWjh0IoABF5NIO0k7irsHOdbciUI'
OPENWEATHER_API_KEY = '08a28bf2dcbc1cbd8fc2eb57e6fd1408'

bot = telebot.TeleBot(TELEGRAM_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me a city name and I'll provide the current temperature.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    city_name = message.text
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}')
    data = json.loads(response.text)
    if data['cod'] == 200:
        temp = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        bot.reply_to(message, f'The current temperature in {city_name} is {temp:.2f}°C.')
    else:
        bot.reply_to(message, 'Sorry, I could not find that city.')

bot.polling()

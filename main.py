from telebot import TeleBot
from agregator import Agregator
from config import TELEGA_TOKEN
from schemas import SalarySchemas
import json

API_TOKEN = TELEGA_TOKEN

bot = TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
        Привет! Я - AgrBot. Я не агрусь, а агригирую данные. Введите данные, как в примере ниже\n
        {
            "dt_from": "2022-09-01T00:00:00",
            "dt_upto": "2022-12-31T23:59:00",
            "group_type": "month"
        }
        Варианты параметра "group_type": "month", "day", "hour"
        """
                 )


@bot.message_handler(func=lambda message: True)
def agr_message(message):
    message_text = json.loads(message.text)
    message_data = SalarySchemas(**message_text)
    a = Agregator(dt_from=message_data.dt_from, dt_upto=message_data.dt_upto, group_type=message_data.group_type)
    b = a.start_aggregation()
    bot.reply_to(message, json.dumps(b))


if __name__ == "__main__":
    bot.infinity_polling()

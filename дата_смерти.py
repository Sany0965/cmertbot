import telebot
import datetime
import random
import time

bot = telebot.TeleBot('Ваштокен')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который предскажет дату вашей смерти. Для предсказания отправьте команду /data_smerti и ваше Имя и Фамилию (Например: Иванов Иван)")

@bot.message_handler(commands=['data_smerti'])
def predict_death_date(message):
    try:
        msg = bot.send_message(message.chat.id, "Пожалуйста, пришлите ваше Имя и Фамилию (Например: Иванов Иван)")
        bot.register_next_step_handler(msg, process_name)
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')

def process_name(message):
    try:
        user_name = message.text.lower()
        is_special_user = "ура роблокс" in user_name

        bot.send_message(message.chat.id, 'Подключаюсь к серверам Бога Смерти 🍕...')
        time.sleep(5)

        start_date = datetime.datetime(2023, 11, 6)
        end_date = datetime.datetime(2100, 1, 1)
        random_date = start_date + datetime.timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

        today = datetime.datetime.now()
        delta = random_date - today
        years, days = divmod(delta.days, 365)
        months = days // 30
        days = days % 30

        reasons = [
            "Из-за автомобильной аварии",
            "Лучший друг",
            "Убийца",
            "Старость",
            "Смерть на работе",
            "Болезнь",
            "Вейп или Сигареты",
            "Случайное падение кирпича",
            "Атака медузы",
            "Волшебное заклинание",
            "Сердечно-сосудистые заболевания",
            "Инсульт",
            "Рак",
            "Бронхиальная астма",
            "Пневмония",
            "Дорожно-транспортные происшествия",
            "Диабет",
            "Гепатит и цирроз печени",
            "Другие инфекционные заболевания",
            "Хроническая обструктивная болезнь легких (ХОБЛ)",
            "Суицид",
            "Ожирение",
            "Употребление алкоголя",
            "Онкологические заболевания легких",
            "Болезнь Альцгеймера и другие деменции",
            "Гепатоцеллюлярная карцинома",
            "Мочекаменная болезнь",
            "Хроническая болезнь почек",
            "Черепно-мозговые травмы"
        ]
        random_reason = random.choice(reasons)

        formatted_date = random_date.strftime("%d %B %Y")

        time_until_death = f'{years} год(а/лет), {months} месяц(а/ев), {days} день(дней)'

        result_message = f'{user_name.title()}, ваша дата Смерти: {formatted_date}\n'
        result_message += f'Вы Умрёте через: {time_until_death}\n'
        if is_special_user:
            result_message += "Причина: Электронные сигареты / Лучший друг\n"
        else:
            result_message += f'Причина: {random_reason}\n'
        result_message += "Приятного дня"
        bot.send_message(message.chat.id, result_message)
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')

@bot.message_handler(commands=['code'])
def send_code(message):
    bot.send_message(message.chat.id, "Исходный код бота доступен на GitHub: [GitHub Repo](https://github.com/Sany0965/cmertbot)")

if __name__ == "__main__":
    bot.polling(none_stop=True)



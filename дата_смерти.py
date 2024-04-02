import telebot
import datetime
import random
import time

bot = telebot.TeleBot('ТОКЕНОТБОТФАЗЕР')

# Чтение причин смерти из файла
def read_death_reasons():
    with open('death_reasons.txt', 'r', encoding='utf-8') as file:
        reasons = file.readlines()
    return reasons

# Функция для предсказания даты смерти
def predict_death(user_name):
    reasons = read_death_reasons()

    start_date = datetime.datetime(2023, 11, 6)
    end_date = datetime.datetime(2100, 1, 1)
    random_date = start_date + datetime.timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

    today = datetime.datetime.now()
    delta = random_date - today
    years, days = divmod(delta.days, 365)
    months = days // 30
    days = days % 30

    formatted_date = random_date.strftime("%d %B %Y")
    time_until_death = f'{years} год(а/лет), {months} месяц(а/ев), {days} день(дней)'
    
    random_reason = random.choice(reasons).strip()
    if ',' in random_reason:
        reason_index, reason_text = random_reason.split(',')
        random_reason = reason_text.strip()

    return formatted_date, time_until_death, random_reason

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton('Код бота 🤖', callback_data='code'),
                telebot.types.InlineKeyboardButton('Предсказать дату смерти 💀', callback_data='predict_death'))
    bot.send_message(message.chat.id, "Привет! Я бот, который предскажет дату вашей смерти.", reply_markup=markup)

# Обработчик нажатия на инлайн-кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'code':
        bot.send_message(call.message.chat.id, "Исходный код бота доступен на GitHub: [GitHub Repo](https://github.com/Sany0965/cmertbot) 📝", parse_mode='Markdown')
    elif call.data == 'predict_death':
        msg = bot.send_message(call.message.chat.id, "Пожалуйста, пришлите ваше Имя и Фамилию (Например: Иванов Иван) 🙂")
        bot.register_next_step_handler(msg, process_name)

# Обработчик ввода имени и фамилии
def process_name(message):
    try:
        user_name = message.text.lower()

        # Предсказание даты смерти
        formatted_date, time_until_death, random_reason = predict_death(user_name)

        result_message = f'{user_name.title()}, ваша дата Смерти: {formatted_date} 💀\n'
        result_message += f'Вы Умрёте через: {time_until_death} ⏳\n'
        result_message += f'Причина: {random_reason} 😱\n'
        result_message += "Приятного дня! ☀️"
        bot.send_message(message.chat.id, result_message)
    except Exception as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')

if __name__ == "__main__":
    bot.polling(none_stop=True)

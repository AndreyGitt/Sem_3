import telebot
import random
import time

TOKEN = '123456789:AAAAAAAAAAAAAAA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_game(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Добро пожаловать в игру на сложение и умножение чисел на время!")
    bot.send_message(chat_id, "У вас будет 5 раундов. Чем быстрее вы ответите, тем больше очков вы получите.")
    bot.send_message(chat_id, "Готовы начать игру? Введите /play")

@bot.message_handler(commands=['play'])
def play_game(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Игра началась! Приготовьтесь...")
    score = 0

    for round in range(1, 6):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '*'])

        question = f"Раунд {round}:\n"
        question += f"Сколько будет {num1} {operator} {num2}?"

        bot.send_message(chat_id, question)

        start_time = time.time()

        @bot.message_handler(func=lambda m: True)
        def check_answer(message):
            nonlocal score

            if message.text.isdigit():
                answer = int(message.text)

                if operator == '+':
                    result = num1 + num2
                else:
                    result = num1 * num2

                if answer == result:
                    elapsed_time = time.time() - start_time
                    score += int(10 - elapsed_time)
                    score +=2
                    bot.send_message(chat_id, f"Правильно! Ваш текущий счет: {score}")
                else:
                    bot.send_message(chat_id, "Неправильно!")

        time.sleep(10)  # Ожидаем 10 секунд для ответа

    bot.send_message(chat_id, f"Игра окончена! Ваш итоговый счет: {score}")

bot.polling()



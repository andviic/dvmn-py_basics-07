import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')


def wait(chat_id, message):
    timer = parse(message)
    message_id = bot.send_message(chat_id, 'Запускаю таймер...')
    bot.create_countdown(
        timer,
        notify_progress,
        chat_id=chat_id,
        message_id=message_id,
        timer=timer
    )
    bot.create_timer(timer, choose, chat_id=chat_id)


def notify_progress(secs_left, chat_id, message_id, timer):
    message = f"""Осталось {secs_left} секунд
    {render_progressbar(timer, secs_left)}"""
    bot.update_message(chat_id, message_id, message)


def choose(chat_id):
    answer = 'Время вышло!'
    bot.send_message(chat_id, answer)


def render_progressbar(
    total,
    iteration,
    prefix='',
    suffix='',
    length=30,
    fill='█',
    zfill='░'
):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    global bot
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(wait)
    bot.run_bot()


if __name__ == "__main__":
    main()

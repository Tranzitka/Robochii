import time
import requests

# Пример: автоматическая публикация партнерских ссылок на Telegram-канал
# Требуется: создать бота в BotFather, добавить в канал и дать права администратора

TELEGRAM_BOT_TOKEN = "8036462590:AAEHWrMUnho4xFnxGe3dlX_JmEQAkJr-Zn8"
CHANNEL_ID = "@Robich"  # пример: @mychannel
AFFILIATE_LINKS = [
    "https://partner.example.com/link1",
    "https://partner.example.com/link2",
    "https://partner.example.com/link3"
]

def post_to_channel(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "disable_web_page_preview": False
    }
    response = requests.post(url, data=payload)
    print(f"Posted: {message} | Status: {response.status_code}")

def run_bot():
    while True:
        for link in AFFILIATE_LINKS:
            post_to_channel(f"Зарабатывай с нами: {link}")
            time.sleep(3600)  # постим раз в час

if __name__ == "__main__":
    run_bot()

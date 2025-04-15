import requests
import datetime
import pytz

BOT_TOKEN = "7635920665:AAHMbgpOFuqrnQYiltkLYrywawvdq1mZ2Rw"
CHAT_ID = "-1002313397362"
UNSPLASH_ACCESS_KEY = "Y_x7FDcrDmTlLLXzzTRYI0RhBXc3lYxFT3z-HnkMo3M"

# Bengali date from WorldTimeAPI
def get_bangla_date():
    now = datetime.datetime.now(pytz.timezone('Asia/Dhaka'))
    bangla_months = ['বৈশাখ', 'জ্যৈষ্ঠ', 'আষাঢ়', 'শ্রাবণ', 'ভাদ্র', 'আশ্বিন', 'কার্তিক', 'অগ্রহায়ণ', 'পৌষ', 'মাঘ', 'ফাল্গুন', 'চৈত্র']
    return f"{now.day} {bangla_months[(now.month % 12)]}, {now.year}"

# Get photo from Unsplash
def get_image_url():
    res = requests.get(f"https://api.unsplash.com/photos/random?query=morning&client_id={UNSPLASH_ACCESS_KEY}")
    return res.json()["urls"]["regular"]

# Send message
def send_message():
    eng_date = datetime.datetime.now(pytz.timezone('Asia/Dhaka')).strftime("%A, %d %B %Y")
    bng_date = get_bangla_date()
    image_url = get_image_url()

    caption = f"🌞 **শুভ সকাল!**\n\nআজকের তারিখ:\n**EN:** {eng_date}\n**BN:** {bng_date}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)

send_message()

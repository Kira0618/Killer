import requests
import telebot, time
from telebot import types
import threading, os, re
from collections import deque

from m1 import (
    go0, go1, go2, go3, go4,
    go5, go6, go7, go8, go9,
    go10, go11, go12, go13, go14
)

# =========================
# TELEGRAM CONFIG
# =========================
TOKEN = "8399279421:AAHiFfuxnTXns1zfrTPbhCzySWLqmNBGjSE"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML", threaded=False)

# =========================
# AUTH
# =========================
OWNER_ID = "7954343626"
allowed_users = {OWNER_ID}
AUTH_FILE = "authorized_users.txt"

if os.path.exists(AUTH_FILE):
    with open(AUTH_FILE) as f:
        allowed_users |= {x.strip() for x in f if x.strip()}

def save_users():
    with open(AUTH_FILE, "w") as f:
        for u in allowed_users:
            f.write(u + "\n")

# =========================
# GLOBAL CONFIG
# =========================
WORKERS = 3
FUNCTIONS = [go0, go1, go2, go3, go4, go5, go6, go7, go8, go9, go10, go11, go12, go13, go14]
SAVE_FILE = "unfortunately.txt"

card_queue = deque()
queue_lock = threading.Lock()
edit_lock = threading.Lock()
stop_event = threading.Event()

user_running_files = {}

# =========================
# AUTH COMMAND
# =========================
@bot.message_handler(commands=["auth"])
def auth_user(message):
    if str(message.chat.id) != OWNER_ID:
        bot.reply_to(message, "❌ Owner only")
        return

    try:
        _, action, uid = message.text.split()
        if action == "add":
            allowed_users.add(uid)
            save_users()
            bot.reply_to(message, f"✅ Authorized {uid}")
        elif action == "remove":
            allowed_users.discard(uid)
            save_users()
            bot.reply_to(message, f"⛔ Removed {uid}")
    except:
        bot.reply_to(message, "Usage: /auth add <id> | /auth remove <id>")

# =========================
# START
# =========================
@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "❌ Not authorized")
        return
    bot.reply_to(message, "📂 Send combo file")

# =========================
# WORKER FUNCTION
# =========================
def process_cards(message, msg_id, total, stats):
    dd, live, ch, ccn, cvv, lowfund = stats
    session = requests.Session()

    while not stop_event.is_set():
        with queue_lock:
            if not card_queue:
                return
            cc = card_queue.popleft()
            func = FUNCTIONS[len(card_queue) % len(FUNCTIONS)]

        # BIN INFO
        try:
            r = session.get(
                f"https://bins.antipublic.cc/bins/{cc[:6]}",
                timeout=5
            )
            data = r.json()
        except:
            data = {}

        brand = data.get("brand", "Unknown")
        card_type = data.get("type", "Unknown")
        country = data.get("country_name", "Unknown")
        country_flag = data.get("country_flag", "")
        bank = data.get("bank", "Unknown")

        start = time.time()
        try:
            last = str(func(cc))
        except:
            last = "ERROR"

        exec_time = time.time() - start

        # RESULT
        if "succeeded" in last:
            ch[0] += 1
            result = "Transaction was successful"
        elif "sufficient" in last.lower():
            lowfund[0] += 1
            result = "Insufficient Funds"
        elif "requires_action" in last:
            cvv[0] += 1
            result = "3D Secure Required"
        elif "Unfortunately" in last:
            dd[0] += 1
            with open(SAVE_FILE, "a") as f:
                f.write(cc + "\n")
            result = "Unfortunately"
        else:
            dd[0] += 1
            result = "Declined"

        # INLINE BUTTON
        kb = types.InlineKeyboardMarkup(row_width=1)
        kb.add(
            types.InlineKeyboardButton(f"CHARGED [{ch[0]}]", callback_data="x"),
            types.InlineKeyboardButton(f"CVV [{cvv[0]}]", callback_data="x"),
            types.InlineKeyboardButton(f"LOW FUNDS [{lowfund[0]}]", callback_data="x"),
            types.InlineKeyboardButton(f"DECLINED [{dd[0]}]", callback_data="x"),
            types.InlineKeyboardButton(f"TOTAL [{total}]", callback_data="x"),
            types.InlineKeyboardButton("STOP", callback_data="stop")
        )

        # SAFE EDIT
        with edit_lock:
            try:
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=msg_id,
                    text=f"""
CARD: <code>{cc}</code>
RESPONSE: <code>{result}</code>

BIN: <code>{cc[:6]} | {brand} | {card_type}</code>
BANK: <code>{bank}</code>
COUNTRY: <code>{country} {country_flag}</code>

TIME: <code>{exec_time:.1f}s</code>
WORKER: <b>{threading.current_thread().name}</b>
""",
                    reply_markup=kb
                )
            except:
                pass

# =========================
# FILE HANDLER
# =========================
@bot.message_handler(content_types=["document"])
def main(message):
    uid = str(message.chat.id)
    if uid not in allowed_users:
        return

    if user_running_files.get(uid):
        bot.reply_to(message, "❌ Already running")
        return

    user_running_files[uid] = True
    stop_event.clear()

    try:
        msg = bot.reply_to(message, "CHECKING... ⏳")
        msg_id = msg.message_id

        file = bot.get_file(message.document.file_id)
        data = bot.download_file(file.file_path)

        with open("combo.txt", "wb") as f:
            f.write(data)

        with open("combo.txt") as f:
            cards = [x.strip() for x in f if x.strip()]

        card_queue.clear()
        card_queue.extend(cards)

        total = len(cards)
        stats = ([0], [0], [0], [0], [0], [0])

        threads = []
        for i in range(WORKERS):
            t = threading.Thread(
                target=process_cards,
                args=(message, msg_id, total, stats),
                name=f"Worker-{i}"
            )
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=msg_id,
            text="CHECKED ✅"
        )

        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "rb") as f:
                bot.send_document(message.chat.id, f)
            os.remove(SAVE_FILE)

    finally:
        user_running_files[uid] = False
        stop_event.clear()

# =========================
# STOP BUTTON
# =========================
@bot.callback_query_handler(func=lambda c: c.data == "stop")
def stop_bot(call):
    stop_event.set()
    bot.answer_callback_query(call.id, "Stopped")

# =========================
print("BOT STARTED")
bot.infinity_polling(timeout=60, long_polling_timeout=60)

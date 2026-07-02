import os
import json
import random
import asyncio
from telegram import Update
from telegram.ext import Application, ChatMemberHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

GROUPS_FILE = "groups.json"

questions = [
    "🧪 Science Quiz\n\nQ. Human body ka sabse bada organ kaunsa hai?\n\nA) Liver\nB) Skin\nC) Heart\nD) Brain\n\n✅ Answer: B) Skin",

    "⚛️ Physics Quiz\n\nQ. SI unit of Force?\n\nA) Joule\nB) Watt\nC) Newton\nD) Pascal\n\n✅ Answer: C) Newton",

    "🧬 Biology Quiz\n\nQ. Blood ka red color kis wajah se hota hai?\n\nA) Chlorophyll\nB) Hemoglobin\nC) Plasma\nD) Platelets\n\n✅ Answer: B) Hemoglobin",

    "🧪 Chemistry Quiz\n\nQ. Water ka chemical formula?\n\nA) CO2\nB) H2O\nC) O2\nD) NaCl\n\n✅ Answer: B) H2O"
]


def load_groups():
    if os.path.exists(GROUPS_FILE):
        with open(GROUPS_FILE, "r") as f:
            return json.load(f)
    return []


def save_groups(groups):
    with open(GROUPS_FILE, "w") as f:
        json.dump(groups, f)


async def track_groups(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat

    if chat and chat.type in ["group", "supergroup"]:
        groups = load_groups()

        if chat.id not in groups:
            groups.append(chat.id)
            save_groups(groups)
            print(f"Added group: {chat.id}")


async def send_quiz_loop(app):
    while True:
        groups = load_groups()

        for group_id in groups:
            try:
                await app.bot.send_message(
                    chat_id=group_id,
                    text=random.choice(questions)
                )
            except Exception as e:
                print(e)

        await asyncio.sleep(1800)  # 30 min


async def post_init(app):
    asyncio.create_task(send_quiz_loop(app))


app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()



print("Bot Started...")
app.run_polling()

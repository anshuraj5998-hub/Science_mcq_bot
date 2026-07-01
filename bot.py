import os
import time
import random
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

questions = [
    "🔬 Science Quiz\n\nQ. Human body ka sabse bada organ kaunsa hai?\n\nA) Liver\nB) Skin\nC) Heart\nD) Brain\n\n✅ Answer: B) Skin",

    "⚛️ Physics Quiz\n\nQ. SI unit of Force?\n\nA) Joule\nB) Watt\nC) Newton\nD) Pascal\n\n✅ Answer: C) Newton",

    "🧪 Chemistry Quiz\n\nQ. Water ka chemical formula?\n\nA) CO2\nB) H2O\nC) O2\nD) NaCl\n\n✅ Answer: B) H2O",

    "🧬 Biology Quiz\n\nQ. Blood ka red color kiski wajah se hota hai?\n\nA) Chlorophyll\nB) Hemoglobin\nC) Plasma\nD) Platelets\n\n✅ Answer: B) Hemoglobin"
]

while True:
    msg = random.choice(questions)

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

    time.sleep(1800)

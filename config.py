## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("BADuXB8AL2O6LqKqB-6Ogh-eQ-uj3WzQee7A4KO5OoSM3lTOIDMjTpwzzE0enSKNm3Q70_8ImcaN7PyeosobSOCOGVTQkEWtIz9P7k5P7oYKexmweSyDZX4cya7qqSUX-f_LzJD2BGl5hKeoTiZ6uuwrtdVO9MujTywbBkmqXEj2Faqockel9vLod85t4UfNe5dtHJbZ7fXg51sC8KGOay421MKJ-fCS3t-2nt0FE7_-3WXbzR8ySKoLM0u5V0T75yegQsQlaAashSQ9sTl4l6MoQNPlLMnBTmJlq92Soa1Hec-X1w8mPBFW0Aph3Q4ejDbHeEtbwalnPzTFT0D29ZG7MCDbmQAAAAFR6C_FAA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5618620730:AAEPmBKFNO5Qr-JLHYm0UXbNEK_tg61obx8")
BOT_NAME = getenv("BOT_NAME", "illestniccur")

API_ID = int(getenv("API_ID", "26410786"))
API_HASH = getenv("API_HASH", "c71a12e92d2bba0406a6b15c032306c6")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://illestniccur1:collinsouma@cluster0.lvoi93c.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "illestniccurr")
ALIVE_NAME = getenv("ALIVE_NAME", "illestniccur")
BOT_USERNAME = getenv("BOT_USERNAME", "iniccur1bot")
OWNER_ID = getenv("OWNER_ID", "1882002437")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "iniccur")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "test258099")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "techzonebots")
HEROKU_APP_NAME = getenv("new")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "4b42df51-236c-45c0-91d3-019e5787763b")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1882002437").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1200"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)

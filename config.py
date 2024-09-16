# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22475741"))
API_HASH = getenv("API_HASH", "1a217be71a0225e0a678af286c211f8a")
BOT_TOKEN = getenv("BOT_TOKEN", "7544718340:AAFTOwtcmKhA44PeL572OLTgtFxlDfUri4k")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6562642609").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://navedmohammad053:Aslam@8005@telegram.9xlun.mongodb.net/?retryWrites=true&w=majority&appName=Telegram")
LOG_GROUP = getenv("LOG_GROUP", "4576435324")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("28996666")
APP_HASH = os.environ.get("409bb6487e989a4a0d2c333a8d539c17")
BOT_USERNAME = os.environ.get("qszpbot")
session = os.environ.get("1BJWap1sBu3FtWzRgPKsydMsWFxJa7jFcGgBn3XcMwWWrcfUvSo4xEpwhQK7j9SGgF34ftJwsRpoYiQoknei-VSd5D1VPOA1Zj-LVNFHCewObZMxVZQRgZ6CqKbPXeAK_qTdn3nOSZ1wyQ-8lMuptb77QoHDyhKHYd3T0V5hbGyXe-iQo7ra0idZDVG64ktk0OE_V3fLGx_0AricEq2Wvpxpr07faj2SltKXBfXxzCvZcjsJzhvVO1Kzlyfb_lJ5a0TABarGCxovfvFOXFNmENja4ILbaSvLScatUXWeFg_t-kRXHBAu5UudjED8WCxwVw9ofkxZI4MqY5EWabTG3_Qqs1I6iNsM=")
SESSION = os.environ.get("1BJWap1sBu3FtWzRgPKsydMsWFxJa7jFcGgBn3XcMwWWrcfUvSo4xEpwhQK7j9SGgF34ftJwsRpoYiQoknei-VSd5D1VPOA1Zj-LVNFHCewObZMxVZQRgZ6CqKbPXeAK_qTdn3nOSZ1wyQ-8lMuptb77QoHDyhKHYd3T0V5hbGyXe-iQo7ra0idZDVG64ktk0OE_V3fLGx_0AricEq2Wvpxpr07faj2SltKXBfXxzCvZcjsJzhvVO1Kzlyfb_lJ5a0TABarGCxovfvFOXFNmENja4ILbaSvLScatUXWeFg_t-kRXHBAu5UudjED8WCxwVw9ofkxZI4MqY5EWabTG3_Qqs1I6iNsM=")
token = os.environ.get("7408849877:AAEGl-VCR52h3bgYPHLM9M51zgWEQKkxYC0")
ze = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
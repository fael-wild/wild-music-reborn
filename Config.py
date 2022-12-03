import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "8073603"))
    API_HASH = os.environ.get("API_HASH", "b307090ebd480b62c47c038f722cd7ff")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2033769589:AAHLjbSOU62pJqMLHQoFTT-r8Y1gJkDsK5k")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLkBuzySTHC8lY4txOgBX5bcorkZLO_k11v-ljM40wAwpd0rOU0mqZJgQqkQYZ2TOx5upOQ3LOxoHaNtJ6Belz3M13k6C87hZmrfYqk4slBsvK1P2errW05DwHZrRueI8Xx-mkCT-7H_6ssu09v5zev_J7LVJmBUHC7y7_AlsgfSyMX8vAePPuPPZWalib7Nu3EzYL3alJxDhJZ72tqyDrsJ2YlAtvlr-wiq4OecqzyR85qt0uqt36nJ6p0Ti45Sfs-22QOgQCc8aZkuSWqUQq7UQUcdczYA6hKVQazhjgXMsBzbbkeuf8GB6fO0m9BVs_6w2RxxxaWCrGLA23fQ39_BG9g=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "WildenMusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "2052293423")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

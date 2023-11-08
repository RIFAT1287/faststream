from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 11421014))
    API_HASH = env.get("TELEGRAM_API_HASH", "9ac3fd02dccbde3435d6b58a5e430bcb")
    OWNER_ID = int(env.get("OWNER_ID", 5076258969))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "5076258969").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "AnimeLoungeLeechbot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6594858799:AAH6eW59XyW2UpDORCD6f-Lo9FrRKU1PkgY")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001830345770))
    BOT_WORKERS = int(env.get("BOT_WORKERS", 10))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 3))

class Server:
    BASE_URL = env.get("BASE_URL", "https://faststreambot-89ca732a343e.herokuapp.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'hypercorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hypercorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}

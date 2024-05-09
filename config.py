HOME_DIR = "C:\Users\Самвел\PycharmProjects\pythonProject13"
IAM_TOKEN_PATH = f'{HOME_DIR}/creds/iam_token.txt' 
FOLDER_ID_PATH = f'{HOME_DIR}/creds/folder_id.txt'
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt'
COUNT_LAST_MSG = 4
MAX_USER_TTS_SYMBOLS = 1000
MAX_TTS_SYMBOLS = 200
MAX_USER_STT_BLOCKS = 12
MAX_USERS = 3
MAX_GPT_TOKENS = 120
MAX_USER_GPT_TOKENS = 2_000
SYSTEM_PROMPT = [{'role': 'system',
                  'text': 'Ты умный и дружелюбный собеседник. '
                          'Общайся с пользователем на "ты" и используй юмор.'
                          'Поддерживай диалог. Изображай человека'}]
LOGS = f'{HOME_DIR}logs.txt'
PATH_TO_DB = f'{HOME_DIR}messages.db'

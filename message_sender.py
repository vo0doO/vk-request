import time
import vk_api
import sqlite3
from numpy import random
import logging
import sys
import os


LOG_FILENAME = os.path.dirname(os.path.abspath(__file__)) + '/messages.log'
PATH_TO_USERS_DB = os.path.dirname(os.path.abspath(__file__)) + '/kirishi_users.db'
USER_LOGIN = "89602607508"
USER_PASSWORD = "mmmmMMMM0809"
APP_ID = "6009351"
API_VER = '5.73'
CLIENT_SECRET = '415c746e415c746e415c746ee54107c6694415c415c746e1858a90711ebafe24fd0637f'


logger = logging.getLogger(__name__)

# ОТПРАВИТЕЛЬ СООБЩЕНИЙ
def sender_my_mesages(db, login, password, api_version, app_id, client_secret):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row
    sql = 'SELECT * FROM kirishiVkUsers1 WHERE `message_send` isnull'
    vk_session = vk_api.VkApi(login, password, api_version, app_id, client_secret)
    vk_session.auth()
    vk = vk_session.get_api()
    for usr in cursor.execute(sql):
        random_mess_id = random.randint(111111111, 999999999)
        try:
            vk.messages.send(user_id = int(f"{usr[0]}"), message = f"Здравствуйте {usr[1]} {usr[2]}. Вам предварительно одобрен займ, до 30 000 руб. Звоните: +7-921-444-73-44", random_id = random_mess_id)
            cursor.execute(f"UPDATE kirishiVkUsers1 SET message_send={random_mess_id} WHERE id={usr[0]}")
            logger.info(f"Сообщение пользователю {usr[0]} отправленно")
        except:
            logger.exception(f"Сообщение пользователю {usr[0]} не отправленно")
            continue
        conn.commit()
        break


# ПОЛУЧАЕМ ЛОГИ
def get_logs(logfiles):

    fmt = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s')

    file_handler = logging.FileHandler(filename=logfiles)
    file_handler.setFormatter(fmt)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(fmt)

    root_logger = logging.getLogger()

    root_logger.addHandler(file_handler)
    root_logger.addHandler(stdout_handler)

    root_logger.setLevel(logging.DEBUG)

    return root_logger


if __name__ == "__main__":
    root_logger = get_logs(LOG_FILENAME)
    sender_my_mesages(PATH_TO_USERS_DB, USER_LOGIN, USER_PASSWORD, API_VER, APP_ID, CLIENT_SECRET)

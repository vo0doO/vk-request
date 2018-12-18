import time
import vk_api
import sqlite3
from numpy import random
import logging
import sys


LOG_FILENAME = 'messages.log'
USER_LOGIN = "+79319629413"
USER_PASSWORD = "e31f567b"
APP_ID = "6009351"


logger = logging.getLogger(__name__)


def sender_my_mesages():
    conn = sqlite3.connect("/home/node/PycharmProjects/vk-request/kirishi_users.db")
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row
    sql = "SELECT * FROM `kirishiVkUsers` WHERE `message_send` isnull"
    login, password, api_version, app_id, client_secret = '+79319629413', 'e31f567b', '5.73', '6009351', '415c746e415c746e415c746ee54107c6694415c415c746e1858a90711ebafe24fd0637f'
    vk_session = vk_api.VkApi(login, password, api_version, app_id, client_secret)
    vk_session.auth()
    vk = vk_session.get_api()
    for usr in cursor.execute(sql):
        random_mess_id = random.randint(111111111, 999999999)
        try:
            vk.messages.send(user_id = int(f"{usr[0]}"), message = f"Здравствуйте {usr[1]} {usr[2]}. Вам предварительно одобрен займ, до 30 000 руб. Звоните: +7-921-444-73-44", random_id = random_mess_id)
            cursor.execute(f"UPDATE kirishiVkUsers SET message_send={random_mess_id} WHERE id={usr[0]}")
            logger.info(f"Сообщение пользователю {usr[0]} отправленно")
        except:
            logger.exception(f"Сообщение пользователю {usr[0]} не отправленно")
            continue
        conn.commit()
        time.sleep(100)


# ПОЛУЧАЕМ ЛОГИ
def get_logs():

    fmt = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s')

    file_handler = logging.FileHandler(filename=LOG_FILENAME)
    file_handler.setFormatter(fmt)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(fmt)

    root_logger = logging.getLogger()

    root_logger.addHandler(file_handler)
    root_logger.addHandler(stdout_handler)

    root_logger.setLevel(logging.DEBUG)

    return root_logger


if __name__ == "__main__":
    root_logger = get_logs()
    sender_my_mesages()
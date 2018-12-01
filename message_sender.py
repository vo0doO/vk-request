import time
import vk_api
import sqlite3
from numpy import random
import logging





USER_LOGIN = "+79319629413"
USER_PASSWORD = "e31f567b"
APP_ID = "6009351"


def sender_my_mesages():
    conn = sqlite3.connect("/home/node/PycharmProjects/vk-request/kirishi_users.db")
    cursor = conn.cursor()
    conn.row_factory = sqlite3.Row
    sql = "SELECT * FROM `kirishiVkUsers` WHERE `message_send` isnull"
    login, password, api_version, app_id, client_secret = '+79319629413', 'e31f567b', '5.73', '6009351', '415c746e415c746e415c746ee54107c6694415c415c746e1858a90711ebafe24fd0637f'
    logger = logging.getLogger("vk_api")
    vk_session = vk_api.VkApi(login, password, api_version, app_id, client_secret)
    vk_session.auth()
    vk = vk_session.get_api()
    for usr in cursor.execute(sql):
        random_mess_id = random.randint(111111111, 999999999)
        try:
            vk.messages.send(user_id = int(f"{usr[0]}"), message = f"Здравствуйте {usr[1]} {usr[2]}. Вам предварительно одобрен займ, до 30 000 руб. Звоните: +7-921-444-73-44", random_id = random_mess_id)
            cursor.execute(f"UPDATE kirishiVkUsers SET message_send={random_mess_id} WHERE id={usr[0]}")
            print(f"Сообщение пользователю {usr[0]} отправленно")
        except Exception as e:
            print(e)
            #cursor.execute(f"UPDATE kirishiVkUsers SET message_send = 1 WHERE id = {usr[0]}")
            #print(f"Сообщение пользователю {usr[0]} не отправленно")
            continue
        conn.commit()
        time.sleep(100)

sender_my_mesages()
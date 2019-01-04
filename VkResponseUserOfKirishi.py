# coding=utf-8

import vk_api
import sqlite3
import logging
import os, sys


LOG_FILENAME = os.path.dirname(os.path.abspath(__file__)) + "/vk-response-to-write-db.log"


logger = logging.getLogger(__name__)

conn = sqlite3.connect("/home/node/PycharmProjects/vk-request/kirishi_users_20_40.db")
cursor = conn.cursor()
#cursor.execute("CREATE TABLE kirishiVkUsers2040 (id integer, first_name text, last_name text, sex integer, last_seen_time integer, last_seen_platform integer)")

class Users():
    """
    Пользователь полученный путем запроса к базе вк и получение в качестве ответа массива генераторов => раскодирования текста => сериализация в строку json => запись в файл
    """

    __slots__ = ('users', 'age')

    af = [f for f in range(20, 41)]
    at = [t for t in range(20, 41)]

    def search_users(count):
        login, password = '89785754108', 'udubis49'
        vk_session = vk_api.VkApi(login, password, api_version="5.67", app_id="6009351", client_secret="735b008e735b008e735b008e817300b2897735b735b008e28a62d138fd3f4138278dcfb", scope=140492191)
        try:
            
            vk_session.auth()
        except vk_api.AuthError as errorsmg:
            print(errorsmg)
            return

        tools = vk_api.VkTools(vk_session)

        return tools.get_all_iter(
            method='users.search',
            max_count=1000,
            # КИРИШИ - city: 1743
            values = {'sort': 0,
                      'city': 1743,
                      'fields':
                          ['photo_id',
                           'verified',
                           'sex',
                           'bdate',
                           'city',
                           'country',
                           'home_town',
                           'has_photo',
                           'photo_50',
                           'photo_100',
                           'photo_200_orig',
                           'photo_200',
                           'photo_400_orig',
                           'photo_max',
                           'photo_max_orig',
                           'online',
                           'lists',
                           'domain',
                           'has_mobile',
                           'contacts',
                           'site',
                           'education',
                           'universities',
                           'schools',
                           'status',
                           'last_seen',
                           'followers_count',
                           'common_count',
                           'occupation',
                           'nickname',
                           'relatives',
                           'relation',
                           'personal',
                           'connections',
                           'exports',
                           'wall_comments',
                           'activities',
                           'interests',
                           'music',
                           'movies',
                           'tv',
                           'books',
                           'games',
                           'about',
                           'quotes',
                           'can_post',
                           'can_see_all_posts',
                           'can_see_audio',
                           'can_write_private_message',
                           'can_send_friend_request',
                           'is_favorite',
                           'is_hidden_from_feed',
                           'timezone',
                           'screen_name',
                           'maiden_name',
                           'crop_photo',
                           'is_friend',
                           'friend_status',
                           'career',
                           'military',
                           'blacklisted',
                           'blacklisted_by_me'],
                      'age_from': f'{Users.af[count]}',
                      'age_to': f'{Users.at[count]}',
                      'sex': 0,
                      'online': 0,
                      'has_photo': 0},
            limit=25000)


def main():
    u = []
    id = []
    id_test = set(id)
    test_list = list(id_test)
    test_result = len(test_list)
    count = 0
    max_count = len(Users.af) - 1
    while count <= max_count:
        gen = Users.search_users(count)
        if gen is not None:
            for user in gen:
                try:
                    cursor.execute(f"INSERT OR IGNORE INTO kirishiVkUsers VALUES ({user['id']}, '{user['first_name']}', '{user['last_name']}', {user['sex']}, time.ctime({user['last_seen']['time']}), {user['last_seen']['platform']})")
                except:
                    continue
                u.append(user)
                id.append(user["id"])
                print(user["first_name"])
                print(f"В возрасте до {Users.af[count]} найденно {len(u)}")
                x=2
            count += 1
        else:
            count+=1
    conn.commit()
    y=1
    return u

def test(u):
    user_id = []
    for user in u:
        user_id.append(user["id"])
    user_id_set = set(user_id)
    user_id_list_2 = list(user_id_set)
    result = len(user_id_list_2)
    print(result)
    z=5
u = main()
test(u)

x = 2


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
    # root_logger = get_logs()

    
    print('Готово')
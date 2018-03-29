# coding=utf-8
import json
import logging
import vk_api
from collections import namedtuple
count = int()
ku = []


class Users(object):
    """
    Пользователь полученный путем запроса к базе вк и получение в качестве ответа массива генераторов => раскодирования текста => сериализация в строку json => запись в файл
    """

    __slots__ = ('users', 'age')

    af = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
          44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66]
    at = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
          44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66]


    def search_users(self):
        login, password, api_version, app_id, client_secret = '89523761689', 'e31f567b', '5.73', '6009351', '415c746e415c746e415c746ee54107c6694415c415c746e1858a90711ebafe24fd0637f'
        vk_session = vk_api.VkApi(login, password, api_version, app_id, client_secret)
        try:
            
            vk_session.auth(reauth = True)
        except vk_api.AuthError as errorsmg:
            print(errorsmg)
            return

        tools = vk_api.VkTools(vk_session)

        return tools.get_all_iter(
            method='users.search',
            max_count=978,
            values = {'sort': 0, 'city': 1743, 'fields': ['photo_id', 'verified', 'sex', 'bdate', 'city', 'country', 'home_town', 'has_photo', 'photo_50', 'photo_100', 'photo_200_orig', 'photo_200', 'photo_400_orig', 'photo_max', 'photo_max_orig', 'online', 'lists', 'domain', 'has_mobile', 'contacts', 'site', 'education', 'universities', 'schools', 'status', 'last_seen', 'followers_count', 'common_count', 'occupation', 'nickname', 'relatives', 'relation', 'personal', 'connections', 'exports', 'wall_comments', 'activities', 'interests', 'music', 'movies', 'tv', 'books', 'games', 'about', 'quotes', 'can_post', 'can_see_all_posts', 'can_see_audio', 'can_write_private_message', 'can_send_friend_request', 'is_favorite', 'is_hidden_from_feed', 'timezone', 'screen_name', 'maiden_name', 'crop_photo', 'is_friend', 'friend_status', 'career', 'military', 'blacklisted', 'blacklisted_by_me'],'age_from': f'{Users.af[count]}', 'age_to': f'{Users.at[count]}', 'interests': str(),'sex': 0,'status': 0,'online': 0,'has_photo': 0,'company': str(),'position': str(),'group_id': 0,'from_list': str()},     limit=1000)

    def __init__(self, age):
        self.age = age
        self.users = Users.search_users(self)
        
    def __next__(self):
        for user in self.users:
            self.users = Users.search_users(self)
            return self.users

    def __iter__(self):
        return self.users.__iter__()

    def __call__(self, *args, **kwargs): ## TODO:
        us = []
        for i in range(17, 70, 1):
            us.append(Users(age=i).users)
        generators = us.copy()
        find_users = []
        n = 0
        while n <= len(generators):
            try:
                find_users.append(generators[int(n)].send(None))
                print(f"{n}{find_users[-1]}")
            except:
                n = n + 1
                continue
        return find_users


if __name__ == "__main__":
    print('Готово')
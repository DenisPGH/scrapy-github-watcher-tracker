import requests

cookies = {
    '_octo': 'GH1.1.1734369365.1642346170',
    '_device_id': '04a5a26ad00fda4381c2a4f31ae0fcfd',
    'user_session': 'MEu00tgDPVYb4ImpwRmqUdnqQmb9Gb2NayE9LV2R1SC2D4uz',
    '__Host-user_session_same_site': 'MEu00tgDPVYb4ImpwRmqUdnqQmb9Gb2NayE9LV2R1SC2D4uz',
    'logged_in': 'yes',
    'dotcom_user': 'DenisPGH',
    'has_recent_activity': '1',
    'color_mode': '%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D',
    'tz': 'Europe%2FSofia',
    '_gh_sess': '7tsiT1SccIU72mCQUF94AuvVjSJOtEyKOhqCZhZt7X%2BOxw9hZIALDpwf9rhqRMNhxcoTM%2BKvW%2FBK50%2FqDK9aiJmkOK9d0CG95m7%2Bw0IdM1PHSyaxJjkt%2BpbHhH4gIhWqtn0VleuCpwwGwmkVxF6nnWfKOnnBYnwY29UnIuGx89s%3D--CEisqShoIV2Fv6Vk--IW6KI%2BkIcrzErkfVeRbhVQ%3D%3D',
}

headers = {
    'authority': 'github.com',
    'accept': 'text/html',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_octo=GH1.1.1734369365.1642346170; _device_id=04a5a26ad00fda4381c2a4f31ae0fcfd; user_session=MEu00tgDPVYb4ImpwRmqUdnqQmb9Gb2NayE9LV2R1SC2D4uz; __Host-user_session_same_site=MEu00tgDPVYb4ImpwRmqUdnqQmb9Gb2NayE9LV2R1SC2D4uz; logged_in=yes; dotcom_user=DenisPGH; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Europe%2FSofia; _gh_sess=7tsiT1SccIU72mCQUF94AuvVjSJOtEyKOhqCZhZt7X%2BOxw9hZIALDpwf9rhqRMNhxcoTM%2BKvW%2FBK50%2FqDK9aiJmkOK9d0CG95m7%2Bw0IdM1PHSyaxJjkt%2BpbHhH4gIhWqtn0VleuCpwwGwmkVxF6nnWfKOnnBYnwY29UnIuGx89s%3D--CEisqShoIV2Fv6Vk--IW6KI%2BkIcrzErkfVeRbhVQ%3D%3D',
    'if-none-match': 'W/"61b33c885dedc0539edcf225b7375e70"',
    'referer': 'https://github.com/Minkov/python-advanced-2020-05/watchers',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'x-pjax': 'true',
    'x-pjax-container': '#js-repo-pjax-container',
    'x-pjax-csp-version': 'ca8f28be2f02ebc697029bdc0646515d9017cf770c4c1ff8414eccd96f6b5a2a',
    'x-pjax-css-version': '79a4acb89d89cb56c8f7833f5757e40fec323a1bce485804931522a20754d913',
    'x-pjax-js-version': 'e526375391e214ae0860f571142eaf977ee9a35e8cd376ec271112bd9844b4da',
    'x-pjax-version': '06f4366e1e2d5171421e668b8e4827dd20f009d7e7ff0a9f05b11c03853226ae',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.get('https://github.com/Minkov/python-advanced-2020-05/watchers', cookies=cookies, headers=headers)
print(response.css('.truncate::text'))
#print(response.content)
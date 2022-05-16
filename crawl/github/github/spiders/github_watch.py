
import json
import os
from datetime import datetime


os.environ.setdefault('github.settings','SCRAPY_SETTINGS_MODULE')
import requests
import scrapy
import re
import psycopg2

pattern=r'(?P<deni>(class="Truncate")) title="(?P<name>([A-Z- a-z]+))"'

class ConnectionDB():
    conn = psycopg2.connect(
        host="localhost",
        database="roboweb_db",
        user="denis_postgre",
        password="D_12-K9")
    @staticmethod
    def close_connection():
        return ConnectionDB.conn.close()






class GithubSpider(scrapy.Spider, ConnectionDB):
    custom_settings = {
        'github.settings':'SCRAPY_SETTINGS_MODULE',
    }
    name = "github"
    start_urls = ["https://github.com/DenisPGH/REST-API-for-cars"]


    def parse(self,response,**kwargs):
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
            '_gh_sess': 'c9y7%2Bcif4jom%2FR01iuBzDJdhE5MC5oehC9ZQCGrAAF7%2BQP3TDuUVfaKJMXWwkX791oWgP4zY00JGN88GTEM0LBQ9KQPHrJBAz%2BeBZVfu8VdU6s1ccJ9hDIEjDuJ%2Bz3PpZd2KKH4i%2B%2FZxUxvnxaWlYfnyO6hg8kKhSZu2PMLMAyg%3D--vfv03vibdgYNxLKT--6iVIrxjY3rBRNkbiyRaJzg%3D%3D',
        }

        headers = {
            'authority': 'github.com',
            'accept': 'text/html',
            'accept-language': 'en-US,en;q=0.9',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_octo=GH1.1.1734369365.1642346170; _device_id=04a5a26ad00fda4381c2a4f31ae0fcfd; user_session=MEu00tgDPVYb4ImpwRmqUdnqQmb9Gb2NayE9LV2R1SC2D4uz; __Host-user_session_same_site=MEu00tgDPVYb4ImpwRmqUdnqQmb9Gb2NayE9LV2R1SC2D4uz; logged_in=yes; dotcom_user=DenisPGH; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Europe%2FSofia; _gh_sess=c9y7%2Bcif4jom%2FR01iuBzDJdhE5MC5oehC9ZQCGrAAF7%2BQP3TDuUVfaKJMXWwkX791oWgP4zY00JGN88GTEM0LBQ9KQPHrJBAz%2BeBZVfu8VdU6s1ccJ9hDIEjDuJ%2Bz3PpZd2KKH4i%2B%2FZxUxvnxaWlYfnyO6hg8kKhSZu2PMLMAyg%3D--vfv03vibdgYNxLKT--6iVIrxjY3rBRNkbiyRaJzg%3D%3D',
            'if-none-match': 'W/"8be1d1feab3883e45670c7aa1d8915bb"',
            'referer': 'https://github.com/DenisPGH/REST-API-for-cars/watchers',
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

        response_ = requests.get('https://github.com/DenisPGH/REST-API-for-cars/watchers', cookies=cookies,
                                headers=headers)




        current_text=response_.text
        dict_ = {}
        dict_['time'] = f"{datetime.now()}"
        dict_['names'] = []
        all_wached=re.finditer(pattern,current_text)
        for each in all_wached:
            dict_['names'].append(each.group('name').strip())
        print('done')
        with open('file.txt','a') as file:
            file.write(json.dumps(dict_)+"\n")

        cursor = self.conn.cursor() # 2022-05-16 16:09:43.531859
        info_date=str(datetime.now()).split(" ")
        date_=info_date[0]
        time_=info_date[1].split(".")[0]

        names_=', '.join(dict_['names'])
        dict_query={'a':date_,
                    'b':time_,
                    'c':names_}

        cursor.execute('INSERT INTO github(date,time,names ) VALUES(%(a)s, %(b)s, %(c)s)', dict_query)
        self.conn.commit()

        print('done')




# conn.close()
# #cursor.close()










# process = CrawlerProcess({'USER_AGENT' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
#                           })
# process.crawl(GithubSpider) # here have to change the name to NoticeSpider
# process.start()
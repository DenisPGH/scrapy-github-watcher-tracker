#from scrapy.utils.project import get_project_settings




# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(GithubSpider)  # here have to change the name to NoticeSpider
#     process.start()
#
# runner = CrawlerRunner({
#     'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
#
# })
# runner.crawl(GithubSpider)


# from scrapy.crawler import CrawlerProcess
# from scrapy.selector import Selector
# import re
#
# from scrapy.utils.project import get_project_settings


# @staticmethod
    # def start_connection():
    #     conn = psycopg2.connect(
    #         host="localhost",
    #         database="roboweb_db",
    #         user="denis_postgre",
    #         password="D_12-K9")


# process = CrawlerProcess({'USER_AGENT' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
#                           })
# process.crawl(GithubSpider) # here have to change the name to NoticeSpider
# process.start()

###########################################################################
# import json
# from datetime import datetime
#
# day=f'{datetime.today().date()}'
# unique_visitors={}
# unique_visitors[day]={} # {'2022-05-19':{"Denislav Petrov":['first time of watching'],"Other Person":['first time of watching']},
# with open('file.txt', 'r') as file:
#     for each_record in file:
#         dict_record=json.loads(each_record)
#         visitors=dict_record['names'] #list
#         # if len(visitors)==1:
#         #     continue
#         for each_visitor_index in range(len(visitors)):
#             # if visitors[each_visitor_index]=='Denislav Petrov':
#             #     continue
#             if (visitors[each_visitor_index] not in unique_visitors[day]) \
#                     and dict_record['time'].split(' ')[0]==day:
#                 unique_visitors[day][visitors[each_visitor_index]]=dict_record['time']
#
#
#
# with open('report.txt','a') as report:
#     report.write(json.dumps(unique_visitors))
# print(unique_visitors)
#

# import pyttsx3
#
# speaker = pyttsx3.init()
# speaker.setProperty("rate", 140)
# speaker.setProperty("voice", 'Bulgarian+m2')
# speaker.say('START!!')
# speaker.runAndWait()

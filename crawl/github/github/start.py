import json
import os
import sys
from datetime import datetime
import pyttsx3
from scrapy.crawler import CrawlerProcess
from github.github.spiders.github_watch import GithubSpider, ConnectionDB

os.environ.setdefault('github.settings','SCRAPY_SETTINGS_MODULE', )
speaker = pyttsx3.init()
speaker.setProperty("rate", 150)
speaker.setProperty("voice", 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
# speaker.say('START!!')
speaker.runAndWait()



def run_crawl():
    process = CrawlerProcess()
    process.crawl(GithubSpider)  # here have to change the name to NoticeSpider
    if "twisted.internet.reactor" in sys.modules:
        del sys.modules["twisted.internet.reactor"]

    process.start()


counter=0
try:
    while True:
        if counter>0:
            break
        run_crawl()
        # time.sleep(3)
        #print(f"counter={counter}")
        counter+=1
except:

    text_1 = "It's an error!!!"*3
    speaker.say(text_1)
    speaker.runAndWait()
    while True:
        if counter>0:
            break
        run_crawl()
        counter+=1

finally:
    ConnectionDB.close_connection()
    print(f'{counter}')
    day = f'{datetime.today().date()}'
    unique_visitors = {}
    unique_visitors[
        day] = {}  # {'2022-05-19':{"Denislav Petrov":['first time of watching'],"Other Person":['first time of watching']},
    with open('file.txt', 'r') as file:
        for each_record in file:
            dict_record = json.loads(each_record)
            visitors = dict_record['names']  # list
            # if len(visitors)==1:
            #     continue
            for each_visitor_index in range(len(visitors)):
                # if visitors[each_visitor_index]=='Denislav Petrov':
                #     continue
                if (visitors[each_visitor_index] not in unique_visitors[day]) \
                        and dict_record['time'].split(' ')[0] == day:
                    unique_visitors[day][visitors[each_visitor_index]] = dict_record['time']


    with open('report.txt', 'a') as report:
        report.write(json.dumps(unique_visitors)+'\n')
    #print(unique_visitors)

    text_2 = f"End! You have {len(unique_visitors[day])} unique visitors today." \
             f" Their names are : {', '.join(unique_visitors[day])}"
    speaker.say(text_2)
    speaker.runAndWait()




"""
TODO:
+1.add voice to speak, when new one is watching + in the end, who were wachting today
+2. add voice INDICATION by error
+3. add statistic file to store watcher for current day after finish the crawling ===> 
{'2022-05-19':{"Denislav Petrov":['first time of watching'],"Other Person":['first time of watching']},
'2022-05-20':{"Denislav Petrov":['first time of watching'],"Other Person":['first time of watching']},
}
+4. Only one row in statistic file for current day-> check it!!!

"""

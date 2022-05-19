import os
import sys
from scrapy.crawler import CrawlerProcess


from github.github.spiders.github_watch import GithubSpider, ConnectionDB

os.environ.setdefault('github.settings','SCRAPY_SETTINGS_MODULE', )



def run_crawl():
    process = CrawlerProcess()
    process.crawl(GithubSpider)  # here have to change the name to NoticeSpider
    if "twisted.internet.reactor" in sys.modules:
        del sys.modules["twisted.internet.reactor"]

    process.start()


counter=0
while True:
    if counter>100:
        break
    run_crawl()
   # time.sleep(3)
    #print(f"counter={counter}")
    counter+=1


"""
TODO:
1.add voice to speak, when new one is watching + in the end, who were wachting today
2. add voice INDICATION by error
3. add statistic file to store watcher for current day after finish the crawling ===> 
{'2022-05-19':{"Denislav Petrov":['first time of watching'],"Other Person":['first time of watching']},
'2022-05-20':{"Denislav Petrov":['first time of watching'],"Other Person":['first time of watching']},
}
4. Only one row in statistic file for current day-> check it!!!

"""
ConnectionDB.close_connection()
print(f'{counter}')
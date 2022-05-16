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
    if counter>10:
        break
    run_crawl()
   # time.sleep(3)
    print(f"counter={counter}")
    counter+=1


ConnectionDB.close_connection()

print(f'{counter}')
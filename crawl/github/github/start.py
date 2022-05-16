import os
import sys
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from github.github.spiders.github_watch import GithubSpider
os.environ.setdefault('github.settings','SCRAPY_SETTINGS_MODULE', )




# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(GithubSpider)  # here have to change the name to NoticeSpider
#     process.start()
#



def run_crawl():
    process = CrawlerProcess()
    process.crawl(GithubSpider)  # here have to change the name to NoticeSpider
    if "twisted.internet.reactor" in sys.modules:
        del sys.modules["twisted.internet.reactor"]

    process.start()
    # runner = CrawlerRunner({
    #     'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
    #
    # })
    # runner.crawl(GithubSpider)

counter=0
while True:
    if counter>10:
        break
    run_crawl()
   # time.sleep(3)
    print(f"counter={counter}")
    counter+=1



print(f'{counter}')
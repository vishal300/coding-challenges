import threading
from queue import Queue
from scraper import Scraper
from main import *
from domain import *

PROJECT_NAME = 'MyScrap'
HOMEPAGE = 'https://www.medium.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Scraper(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)


# will die depending when main get finished
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        Scraper.crawl_page(threading.current_thread().name,url)
        queue.task_done()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0 :
        print(str(len(queue_links)) + '  Links in Queue')
        create_jobs()

create_workers()
crawl()

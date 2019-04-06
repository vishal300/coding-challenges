from urllib.request import urlopen
from link_finder import LinkFinder
from main import *

class Scraper:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self,project_name, base_url,domain_name):
        Scraper.project_name = project_name
        Scraper.base_url = base_url
        Scraper.domain_name = domain_name
        Scraper.queue_file = Scraper.project_name + '/queue.txt'
        Scraper.crawled_file = Scraper.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Scraper', Scraper.base_url)

    @staticmethod
    def boot():
        create_project_dir(Scraper.project_name)
        create_data_files(Scraper.project_name,Scraper.base_url)
        Scraper.queue = file_to_set(Scraper.queue_file)
        Scraper.crawled = file_to_set(Scraper.crawled_file)

    @staticmethod
    def crawl_page(thread_name,page_url):
        if page_url not in Scraper.crawled:
            print(thread_name + ' now Crawling ' + page_url)
            print('Queue ' + str(len(Scraper.queue)) + ' | Crawled   ' + str(len(Scraper.crawled)))
            Scraper.add_links_to_queue(Scraper.gather_link(page_url))
            Scraper.queue.remove(page_url)
            Scraper.crawled.add(page_url)
            Scraper.update_file()

    @staticmethod
    def gather_link(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")

            finder = LinkFinder(Scraper.base_url,page_url)
            finder.feed(html_string)
        except:
            print('Error : Can not crawl the page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Scraper.queue:
                continue
            if url in  Scraper.crawled:
                continue
            if Scraper.domain_name not in url:
                continue
            Scraper.queue.add(url)

    @staticmethod
    def update_file():
        set_to_file(Scraper.queue,Scraper.queue_file)
        set_to_file(Scraper.crawled,Scraper.crawled_file)

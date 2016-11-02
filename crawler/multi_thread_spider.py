# -*- coding: utf-8 -*-
import os
import sys
import threading
import urlparse
from bs4 import BeautifulSoup
import requests
requests.packages.urllib3.disable_warnings()


class Spider(threading.Thread):
    """Page Spider"""

    def __init__(self, binary_semaphore, url, crawl_depth):
        self.binary_semaphore = binary_semaphore
        self.crawl_depth = int(crawl_depth)
        self.url = url
        cur_dir = os.getcwd()
        self.thread_id = hash(self)
        threading.Thread.__init__(self)

    def run(self):
        urls = [self.url]
        seen = set()

        request = requests.get(self.url, verify=False)
        htmltext = request.content
        soup = BeautifulSoup(htmltext, 'html.parser')

        print 'Scanning {url} for links...'.format(url=self.url)

        self.binary_semaphore.acquire()

        for tag in soup.findAll('a', href=True):
            tag['href'] = urlparse.urljoin(self.url, tag['href'])
            if self.url in tag['href'] and tag['href'] not in seen:
                seen.add(tag['href'])
                urls.append(tag['href'])

        source_urls = []
        for clean_links in urls:
            resp = requests.get(clean_links, verify=False)
            new_html = resp.content
            new_soup = BeautifulSoup(new_html, 'html.parser')
            part = urlparse.urlparse(clean_links)
            source_urls.append(clean_links)

            good_url = set()
            good_urls = []
            for new_tag in new_soup.findAll('a', href=True):
                clink = urlparse.urljoin(self.url, new_tag['href'])
                if self.url in clink and clink not in good_url:
                    good_url.add(clink)
                    good_urls.append(clink)

            scraped_links = []
            for part in good_urls:
                parse = urlparse.urlparse(part)
                if parse.netloc == '':
                    pass
                elif (parse.query != '') or (parse.path):
                    scraped_links.append(part)
                    print part

        self.binary_semaphore.release()

        for url in urls:
            if self.crawl_depth > 1:
                Spider(binary_semaphore, url, self.crawl_depth-1).start()

if __name__ == "__main__":

    binary_semaphore = threading.Semaphore(1)
    spider = Spider(binary_semaphore, sys.argv[1], sys.argv[2])
    spider.run()

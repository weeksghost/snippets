import os
import sys
import urlparse
import requests
requests.packages.urllib3.disable_warnings()
import threading
from bs4 import BeautifulSoup


class ScrapeThread(threading.Thread):

    def __init__(self, binary_semaphore, url):
        """Usage -> python spider.py <URL>
        This is a simple multithreaded spider
        that will first create a stack of urls
        found on the traget site then will loop
        over loop over urls print them out.
        *Note - this script does not care about dupes.*
        """
        self.url = url
        self.binary_semaphore = binary_semaphore
        self.thread_id = hash(self)
        threading.Thread.__init__(self)

    def run(self):
        self.binary_semaphore.acquire()
        urls = [self.url]
        visted = [self.url]
        curdir = os.getcwd()

        while len(urls) > 0:
            try:
                request = requests.get(urls[0], verify=False)
                htmltext = request.text
            except:
                print('Error here {url}'.format(url=urls[0]))
            soup = BeautifulSoup(htmltext, 'html.parser')

            urls.pop(0)
            print(str(len(urls)) + ' links checked out okay')

            for tag in soup.findAll('a', href=True):
                tag['href'] = urlparse.urljoin(self.url, tag['href'])
                if self.url in tag['href'] and tag['href'] not in visted:
                    urls.append(tag['href'])
                    visted.append(tag['href'])
        for link in visted:
            print(link)
            with open(curdir + '/links.txt', 'ab') as links:
                links.write(link + '\n')

        self.binary_semaphore.release()

if __name__ == '__main__':

    binary_semaphore = threading.Semaphore(1)
    spider = ScrapeThread(binary_semaphore, sys.argv[1])
    spider.run()

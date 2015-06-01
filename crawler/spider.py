import unittest
import urlparse
import requests
from bs4 import BeautifulSoup


class Scrape(unittest.TestCase):

    def test_crawler(self):
        '''
        Crawl links
        '''
        url = ''
        urls = [url]
        visted = [url]
        while len(urls) > 0:
            try:
                request = requests.get(urls[0])
                htmltext = request.text
            except:
                print(urls[0])
            soup = BeautifulSoup(htmltext)

            urls.pop(0)
            print(len(urls))

            for tag in soup.findAll('a', href=True):
                tag['href'] = urlparse.urljoin(url, tag['href'])
                if url in tag['href'] and tag['href'] not in visted:
                    urls.append(tag['href'])
                    visted.append(tag['href'])

        for link in visted:
            try:
                response = requests.get(link)
                if response.status_code != 200:
                    print('[{}] {}'.format(response.status_code, link))
            except:
                print('Exception at: [{}]'.format(response.status_code, link))
        print('\nCrawled {} links!\n'.format(len(visted)))


if __name__ == '__main__':
    unittest.main()

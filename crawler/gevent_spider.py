import sys
import gevent
from gevent import monkey
import urlparse
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup

monkey.patch_all()


urls = ['https://www.python.org/']

def print_links(url):
    print 'Starting %s' % url
    request = requests.get(urls[0], verify=False)
    htmltext = request.text
    soup = BeautifulSoup(htmltext, 'html.parser')
    seen = set()
    visted = []
    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        if url in tag['href'] and tag['href'] not in seen:
            seen.add(tag['href'])
            visted.append(tag['href'])
    for link in visted:
        print link

jobs = [gevent.spawn(print_links, _url) for _url in urls]

gevent.wait(jobs)

###########################################
# WARNING - THIS IS A LOAD TESTING SCRIPT #
# MAKE SURE YOU KNOW WHAT YOU ARE DOING   #
# BEFORE YOU RUN THIS                     #
###########################################

import os
import unittest
import requests
import subprocess


HOME = os.getenv("HOME")


class SiegeTest(unittest.TestCase):

    def _urls(self):
        domain = ''
        url = ''
        while url:
            r = requests.get(domain + url)
            json = r.json()
            for obj in json['objects'][::-1]:
                slug = obj['XXXX']['XXXX']
                urls = str(domain + slug + '\n')
                yield urls
            break


    def test_random_siege(self):
        '''
        Stress test server
        '''
        urls = self._urls()
        siegedir = '{}/siegefiles/'.format(HOME)
        if not os.path.exists(os.path.dirname(siegedir)):
            os.makedirs(os.path.dirname(siegedir))
        siegefile = siegedir + '{}.txt'.format('random_urls')
        try:
            fp = open(siegefile)
        except IOError:
            fp = open(siegefile, 'w+')
        with open(siegefile, 'r+') as siegeurls:
            siegeurls.writelines(urls)
            siegeurls.seek(0,1)
            process = subprocess.call(["siege", "--delay=10", "--concurrent=1000", \
                                       "--internet", "--file={}".format(siegefile)])


if __name__ == '__main__':
    unittest.main()

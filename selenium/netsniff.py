import os
import unittest
import subprocess
import requests


HOME = os.getenv("HOME")

class CreateHars(unittest.TestCase):

    def test_pages(self):
        """
        This test visits pages and saves output .HAR files
        using API to cerate testable objects and parameters.
        """
        domain = domain
        url = url

        while url:
            r = requests.get(domain + url)
            json = r.json()
            for obj in json['objects']:
                slug = obj['XXX']['XXXX'] # Create slug object
                name = obj['XXX']['XXXX'] # Create name object
                new_name = name.replace('/', '')
                urls = domain + slug
                current_dir = os.getcwd()
                script_path = "%s/testing/tests/" % current_dir
                hardir = '%s/HARFILES/' % (HOME)
                if not os.path.exists(os.path.dirname(hardir)):
                    os.makedirs(os.path.dirname(hardir))
                file = hardir + '%s.har' % new_name
                try:
                    fp = open(file)
                except IOError:
                    fp = open(file, 'w+')

                with open(file, 'r+') as hars:
                    process = subprocess.call(["phantomjs", script_path + "scripts/netsniff.js", urls], stdout=hars)
                    hars.write(str(process))
                    hars.seek(0,2)
                    size = hars.tell()
                    hars.truncate(size-1)

            break
            url = json['meta'].get('next', '')


if __name__ == '__main__':
    unittest.main()

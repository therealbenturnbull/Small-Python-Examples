#!/usr/bin/python

import uuid
import datetime
import random



# ==================================================================================================================
#

################################################################################

class Scraper:
    id = ''
    type = ''
    status = 'OFFLINE'
    change_options = ''
    last_modified = datetime.datetime.now()

    def __init__(self, additional=None):
        self.id = str(uuid.uuid4())[-9:]
        print('I am alive:' + self.id)
        self.load_additional(additional)

    def load_additional(self, additional):
        return True

    def run(self):
        returndict = {}
        return returndict


################################################################################

class TwitterScraper(Scraper):
    '''
    details here
    '''
    commands = []
    help_str = ''

    # --------------------------------------------------------------------------
    def load_additional(self, additional):
        self.type = 'TWITTER SCRAPER'
        self.help_str = 'hey, I scrape twitters if you give me a chance!'


    def run(twitter_user: str):
        returndict = {}
        print('yo, I am running: ' + self.id)
        print('this is the bit that does the work')
        return returndict

################################################################################

class URLScraper(Scraper):
    '''
    details here
    '''
    commands = []
    help_str = ''


    # --------------------------------------------------------------------------

    def load_additional(self, additional):
        print('*')
        self.type = 'URL SCRAPER'
        self.help_str = 'hey, I scrape urls if you give me a chance!'


    def run(self, url: str):
        # 1 scrape
        # 2 clean up
        # return the following:
        #   dict:
        #       key1: url -> url
        #       key2: text -> complete text
        #...
        returndict = {}
        return returndict


# ==================================================================================================================
#

def main():
                additional = {}
                additional['no'] = 27
                additional['status'] = 'running'

                a1 = URLScraper(additional)
                a2 = URLScraper(additional)
                a3 = URLScraper(additional)
                a4 = URLScraper(additional)

                b1 = TwitterScraper(additional)
                b2 = TwitterScraper(additional)
                b3 = TwitterScraper(additional)
                b4 = TwitterScraper(additional)

                a1.run('google.com')
                a2.run('news.com')
                a3.run('slashdot.org')
                a4.run('beer.com')


if __name__ == "__main__":
    main()

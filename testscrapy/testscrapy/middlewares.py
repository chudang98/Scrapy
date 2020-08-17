from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from os import getenv
import logging

log = logging.getLogger('Middleware')


class AGCDownloaderClientRenderMiddleware(object):
    def __init__(self):
        options = Options()
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
        options.add_argument("--headless")
        if getenv('REMOTE'):
            log.info('Run WebDriver From Remote')
            self.driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
        else:
            log.info('Run WebDriver From APP')
            self.driver = webdriver.Chrome(options=options)

    def process_request(self, request, spider):
        meta = request.meta
        if 'JS' not in meta or meta['JS'] is not True:
            return None

        self.driver.get(request.url)
        body = self.driver.page_source
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

import scrapy
from scrapy.loader import ItemLoader
from scrapy_splash import SplashRequest
from ..item import Rakuten


class PostsSpider(scrapy.Spider):
  name = "posts"
  pages = 1
  count = 1
  no_of_pages = 1
  allowed_domains = ['rakuten.co.jp']
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
  }

  def start_requests(self):
    urls = [
      'https://search.rakuten.co.jp/search/mall/-/100005/?sid=229659',

    ]
    for url in urls:
      yield SplashRequest(url, endpoint="render.html", callback=self.parse)
  


  def parse(self, res):
    self.pages -= 1
    link_products = res.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "content", " " )) and contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]//a/@href').getall()
    for url in link_products:
      link_product = res.urljoin(url)
      yield SplashRequest(link_product, endpoint="render.html", callback=self.parse_produce)

    if(self.no_of_pages > 0):
      next_page_url = res.xpath("//a[@class='item -next nextPage']/@href").get()
      if(next_page_url is None):
        return
      else:
        next_page = res.urljoin(next_page_url)
        yield scrapy.Request(url=next_page, callback=self.parse, headers=self.headers)

    
  def parse_produce(self, res):
    # i = ItemLoader(item=Rakuten(), response=res)
    # i.add_xpath('name', '//span[@class="item_name"]//b/text()')
    # i.add_xpath('item_number', '//span[@class="item_number"]/text()')
    # i.add_xpath('price', '//span[@class="price2"]/@content')
    # i.add_xpath('point', '//div[@class="point-summary__total___3rYYD"]//span/text()')
    # i.add_xpath('rating', '//body//div//div//div//td[3]/text()')

    # name = res.xpath("//span[@class='item_name']//b/text()").get()
    # # Sẽ có những trang không có rating
    rating = res.xpath("//table[@id='js-review-widget']//tbody//tr//td//table//tbody//tr//td//div//table//tbody//tr//td//span/text()").get()
    # item_number = res.xpath("//span[@class='item_number']/text()").get()
    # point = res.xpath("//div[@class='point-summary__total___3rYYD']//span/text()").get()
    # price = res.xpath("//span[@class='price2']/@content").get()
    # print('Name : ' + name)
    # print('Item number : ' + item_number)
    # print('Price : ' + price + ' 円')
    # print('Point : ' + point + ' point')

    try:
      float(rating)
    except Exception:
      rating = 0

    self.count += 1
import scrapy
from scrapy_splash import SplashRequest
from ..item import Rakuten
from w3lib.url import add_or_replace_parameters

class PostsSpider(scrapy.Spider):
  name = "posts"
  count = 1
  no_of_pages = 1
  allowed_domains = ['rakuten.co.jp']
  file = open("data.txt","a")
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
  }
  # current_brand = ''
  start_urls = [
    'https://search.rakuten.co.jp/search/mall/-/100020/'
  ]
  
  def start_requests(self):
    for url in self.start_urls:
      # self.current_brand = url.split('item.rakuten.co.jp/')[1].split('/')[0]
      # yield SplashRequest(url, endpoint='render.html', callback=self.parse)
      for i in range(1,100,2):
        params = { 
          "max": i + 1,
          "min": i,
        }
        search_url = add_or_replace_parameters(url, params)
        yield scrapy.Request(search_url, callback=self.parse_page)

  def parse_page(self, res):
    print('--------------')
    print(res.url)
    self.no_of_pages -= 1
    link_products = res.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]//a/@href').getall()
    for url in link_products:
      link_product = res.urljoin(url)
      yield SplashRequest(link_product, endpoint="render.html", callback=self.parse_product)

    if(self.no_of_pages > 0):
      next_page_url = res.xpath("//a[@class='item -next nextPage']/@href").get()
      if(next_page_url is None):
        return
      else:
        next_page = res.urljoin(next_page_url)
        yield scrapy.Request(url=next_page, callback=self.parse_page, headers=self.headers)

  def parse_product(self, res):
    # brand = self.current_brand
    # self.file.write(f'{res.url}\n')
    # print(self.count)
    # self.count += 1
    name = res.xpath("//span[@class='item_name']//b/text()").get()
    # rating = res.xpath("//table[@id='js-review-widget']//tbody//tr//td//table//tbody//tr//td//div//table//tbody//tr//td//span/text()").get()
    # item_number = res.xpath("//span[@class='item_number']/text()").get()
    # point = res.xpath("//div[@class='point-summary__total___3rYYD']//span/text()").get()
    # price = res.xpath("//span[@class='price2']/@content").get()
    # freeship = res.xpath("//span[@class='dsf-shipping-cost shipping-free']").get()
    # isFreeship = (freeship is None)
    # descriptions = res.xpath("//span[@class='item_desc']/text()").extract()
    # description = ''
    # for str in descriptions:
    #   description += str
    #   description += '\n'
    # description = description.strip()

    # print('------------------------------------------------------')
    # print('Brand : ' + self.current_brand)
    print('Name : ' + name)
    # print('Item number : ' + item_number)
    # print('Price : ' + price + ' 円')
    # print('Point : ' + point + ' point')
    # print(f'Rating : {rating}')
    # print(f'Freeship : {isFreeship}')
    # print(f'Description : {description}')
    # print('------------------------------------------------------')

    # yield Rakuten(name=name, rating=rating, item_number=item_number,
    #   point=point, price=price, description=description, freeship=isFreeship)


  def parse_catagory(self, res):
    sub_catagories = res.xpath("//body//div[@class='dui-container main']//div[@class='item']//div[@class='item']//a/@href").getall()
    if not sub_catagories:
      self.file.write(f'{res.url}\n')
      # yield scrapy.Request(res.url, callback=self.parse_page, headers=self.headers)
    else:
      for sub_catagory in sub_catagories:
        link_catagory = res.urljoin(sub_catagory)
        yield scrapy.Request(link_catagory, callback=self.parse_catagory, headers=self.headers)


  # def find_limit_product(self, res):
  #   url = res.xpath("//a[@class='item -next nextPage']/@href").get()
  #   print(f"{self.count} --- {url}")
  #   self.count += 1
  #   next_page = res.urljoin(url)
  #   yield scrapy.Request(url=next_page, callback=self.find_limit_product, headers=self.headers)

import scrapy
from scrapy_splash import SplashRequest
from ..item import RakutenItem
from w3lib.url import add_or_replace_parameters
from scrapy.shell import inspect_response
import time

class RakutenSpider(scrapy.Spider):
	name = "rakuten"
	count = 1
	no_of_pages = 1
	allowed_domains = [
		'rakuten.co.jp'
	]
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
	}
	start_urls = [
    'https://search.rakuten.co.jp/search/mall/-/100012/'
	]
	
	def start_requests(self):
		for url in self.start_urls:
			# self.current_brand = url.split('item.rakuten.co.jp/')[1].split('/')[0]
			# yield SplashRequest(url, endpoint='render.html', callback=self.parse)
			for i in range(0,100000,2):
				params = { 
					"min": i,
					"max": i + 1,
				}
				search_url = add_or_replace_parameters(url, params)
				yield scrapy.Request(search_url, callback=self.parse_page)


	def parse_page(self, res):
		# self.no_of_pages -= 1
		link_products = res.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]//a/@href').getall()
		for url in link_products:
			link_product = res.urljoin(url)
			yield scrapy.Request(link_product, callback=self.parse_product, headers=self.headers)

		# if(self.no_of_pages >= 0):
		next_page_url = res.xpath("//a[@class='item -next nextPage']/@href").get()
		if(next_page_url is None):
			return
		else:
			next_page = res.urljoin(next_page_url)
			yield scrapy.Request(url=next_page, callback=self.parse_page, headers=self.headers)

	def parse_product(self, res):
		# if res.status != 200:
		# 	inspect_response(res, self)
		# brand = self.current_brand
		self.count += 1
		print(self.count)
		JAN_CODE = res.xpath("//input[@id='ratRanCode']/@value").get()
		if JAN_CODE is None or JAN_CODE is '':
			return
		else:
			title = res.xpath("//span[@class='item_name']//b/text()").get()
			# Sẽ có những trang không có rating
			# point = res.xpath("//div[@class='point-summary__total___3rYYD']//span/text()").get()
			price = res.xpath("//span[@class='price2']/@content").get()
			price = f'￥ {price}'
			review = res.xpath("//table[@id='js-review-widget']//a[1]/@href").get()
			link_image = res.xpath("//a[@class='rakutenLimitedId_ImageMain1-3']//img/@src").get()
			link_product = res.url
			brand = link_product.split('item.rakuten.co.jp/')[1].split('/')[0]
			descriptions = res.xpath("//span[@class='item_desc']/text()").extract()
			# description = ''
			inStock = True
			featureBullet = []
			for str in descriptions:
				str = str.replace('\n', '')
				if not (str is ''):
					featureBullet.append(str)
			
		# print(description)
		# print(name)
			yield RakutenItem(_id=JAN_CODE ,title=title, price=price, brand=brand,featureBullet=featureBullet,
				inStock=inStock, image=link_image, urlReview=review, urlProduct=link_product)

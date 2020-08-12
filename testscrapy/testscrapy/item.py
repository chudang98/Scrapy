import scrapy
from scrapy.item import Field, Item

class Rakuten(Item):
  name = Field()
  item_number = Field()
  point = Field()
  price = Field()
  rating = Field()

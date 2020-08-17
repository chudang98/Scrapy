from scrapy.item import Field, Item

class RakutenItem(Item):
  _id = Field()
  title = Field()
  brand = Field()
  price = Field()
  inStock = Field()
  featureBullet = Field()
  image = Field()
  urlReview = Field()
  urlProduct = Field()

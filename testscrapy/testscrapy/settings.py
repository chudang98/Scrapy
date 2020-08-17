BOT_NAME = 'testscrapy'

SPIDER_MODULES = ['testscrapy.spiders']
NEWSPIDER_MODULE = 'testscrapy.spiders'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
  'testscrapy.pipelines.TestscrapyPipeline' : 12
}

SPLASH_URL = 'http://localhost:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
COOKIES_ENABLED = True # Nếu cần dùng Cookie
SPLASH_COOKIES_DEBUG = False
SPIDER_MIDDLEWARES = {
  'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
  # 'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': True,
}
DOWNLOADER_MIDDLEWARES = {
  'scrapy_splash.SplashCookiesMiddleware': 723,
  'scrapy_splash.SplashMiddleware': 725,
  'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
}
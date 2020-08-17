# BOT_NAME = 'AGCCrawl'

# SPIDER_MODULES = ['AGCCrawl.spiders']
# NEWSPIDER_MODULE = 'AGCCrawl.spiders'
# ROBOTSTXT_OBEY = False
# CONCURRENT_ITEMS = 10
# CONCURRENT_REQUESTS = 8
# MONGO_URI = 'mongodb://root:Agriconnect123%40@54.178.207.10:27017'
# MONGO_DATABASE = 'agriconnect'

# SPLASH_URL = 'http://localhost:8050'
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
# COOKIES_ENABLED = True # Nếu cần dùng Cookie
# SPLASH_COOKIES_DEBUG = False
# DOWNLOADER_MIDDLEWARES = {
#     'AGCCrawl.middlewares.AGCDownloaderClientRenderMiddleware': 100,
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }

# # EXTENSIONS = {
# #    'scrapy.extensions.telnet.TelnetConsole': None,
# # }

# SPIDER_MIDDLEWARES = {
#     # 'AGCCrawl.middlewares.AGCCrawlSpiderMiddleware': 543,
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 101,
# }

# ITEM_PIPELINES = {
#     'AGCCrawl.pipelines.AGCMongoDBPipeline': 300,
# }
BOT_NAME = "AGCCrawl"
SPIDER_MODULES = ["AGCCrawl.spiders"]
NEWSPIDER_MODULE = "AGCCrawl.spiders"
ROBOTSTXT_OBEY = False
MONGO_URI = "mongodb://root:Agriconnect123%40@54.178.207.10:27017"
MONGO_DATABASE = "agriconnect"

DOWNLOADER_MIDDLEWARES = {
    "AGCCrawl.middlewares.AGCDownloaderClientRenderMiddleware": 100,
}

# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# SPIDER_MIDDLEWARES = {
#     "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
# }

ITEM_PIPELINES = {
    "AGCCrawl.pipelines.AGCMongoDBPipeline": 300,
}

DUPEFILTER_CLASS = "scrapy.dupefilters.BaseDupeFilter"
CONCURRENT_ITEMS = 9
CONCURRENT_REQUESTS = 5
DOWNLOAD_DELAY = 0.25
# -*- coding: utf-8 -*-

# Scrapy settings for recipe project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'recipe'

SPIDER_MODULES = ['recipe.spiders']
NEWSPIDER_MODULE = 'recipe.spiders'
ITEM_PIPELINES = {'recipe.pipelines.RecipePipeline':100}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'recipe (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True



PROXIES = [
    {'ip_port': '111.11.228.75:80', 'user_pass': ''},
    {'ip_port': '120.198.243.22:80', 'user_pass': ''},
    {'ip_port': '111.8.60.9:8123', 'user_pass': ''},
    {'ip_port': '101.71.27.120:80', 'user_pass': ''},
    {'ip_port': '122.96.59.104:80', 'user_pass': ''},
    {'ip_port': '122.224.249.122:8088', 'user_pass': ''},
]
COOKIES_ENABLES=False
DOWNLOADER_MIDDLEWARES = {  
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,  
            'recipe.rotate_useragent.RotateUserAgentMiddleware' :543
        }  
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
LOG_ENABLED=True
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'recipe.middlewares.RecipeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'recipe.middlewares.RecipeDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'recipe.pipelines.recipeRecipePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

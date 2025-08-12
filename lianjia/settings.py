# Scrapy settings for lianjia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianjia'

SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Proxy settings
PROXY_HOST = "www.16yun.cn"
PROXY_PORT = "5445"
PROXY_USER = "16QMSOML"
PROXY_PASS = "280651"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 1.5
RANDOMIZE_DOWNLOAD_DELAY = True

# Retry settings
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'lianjia.middlewares.RandomUserAgentMiddleware': 400,
    'lianjia.middlewares.DynamicProxyMiddleware': 500,
    'lianjia.middlewares.ProxyRetryMiddleware': 600,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 700,
}

# Configure item pipelines
ITEM_PIPELINES = {
    'lianjia.pipelines.LianjiaPipeline': 300,
}

# Log settings
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

# Fake headers
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://bj.lianjia.com/',
}
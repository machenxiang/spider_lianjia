BOT_NAME = 'lianjia'

SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 1.5
RANDOMIZE_DOWNLOAD_DELAY = True

RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]

DOWNLOADER_MIDDLEWARES = {
    'lianjia.middlewares.RandomUserAgentMiddleware': 400,
    'lianjia.middlewares.DynamicProxyMiddleware': 543,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 600,
}

ITEM_PIPELINES = {
    'lianjia.pipelines.LianjiaPipeline': 300,
}

LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://bj.lianjia.com/',
}

# 代理API配置，middleware中使用
PROXY_API_URL = 'http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=58e0f110e9461e35615d4efd6b7e2f23&orderNo=GL20250812155752mPpFUDbp'

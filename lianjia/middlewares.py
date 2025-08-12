# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import base64
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.exceptions import NotConfigured
from urllib.parse import urlparse
import random

class DynamicProxyMiddleware:
    def __init__(self, proxy_host, proxy_port, proxy_user, proxy_pass):
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_user = proxy_user
        self.proxy_pass = proxy_pass

    @classmethod
    def from_crawler(cls, crawler):
        proxy_host = crawler.settings.get('PROXY_HOST')
        proxy_port = crawler.settings.get('PROXY_PORT')
        proxy_user = crawler.settings.get('PROXY_USER')
        proxy_pass = crawler.settings.get('PROXY_PASS')
        
        if not all([proxy_host, proxy_port, proxy_user, proxy_pass]):
            raise NotConfigured('Proxy settings are missing')
            
        return cls(proxy_host, proxy_port, proxy_user, proxy_pass)

    def process_request(self, request, spider):
        # proxy_url = f"http://{self.proxy_host}:{self.proxy_port}"
        # request.meta['proxy'] = proxy_url
        
        # # 代理认证
        # auth = f"{self.proxy_user}:{self.proxy_pass}"
        # encoded_auth = base64.b64encode(auth.encode()).decode()
        # request.headers['Proxy-Authorization'] = f"Basic {encoded_auth}"
        
        # spider.logger.debug(f"Using proxy: {proxy_url}")
        spider.logger.info("Proxy disabled for testing")

class ProxyRetryMiddleware(RetryMiddleware):
    def __init__(self, settings):
        super().__init__(settings)
        self.max_retry_times = settings.getint('RETRY_TIMES', 3)
        
    def process_response(self, request, response, spider):
        if response.status in self.retry_http_codes:
            reason = f"Retrying {request.url} due to status code {response.status}"
            spider.logger.info(reason)
            return self._retry(request, reason, spider) or response
        return response

class RandomUserAgentMiddleware:
    def __init__(self, user_agents):
        self.user_agents = user_agents
        
    @classmethod
    def from_crawler(cls, crawler):
        user_agents = crawler.settings.get('USER_AGENTS', [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ])
        return cls(user_agents)
    
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)

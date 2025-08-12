import random
import requests
from scrapy.exceptions import NotConfigured

class DynamicProxyMiddleware:
    def __init__(self):
        self.proxy_list = []
        self.api_url = "http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=58e0f110e9461e35615d4efd6b7e2f23&orderNo=GL20250812155752mPpFUDbp&count=10&isTxt=1&proxyType=1&returnAccount=2"

    def _fetch_proxies(self):
        """处理文本格式的代理响应"""
        try:
            r = requests.get(self.api_url, verify=False, timeout=10)
            r.encoding = 'utf-8'
            proxies = []
            for line in r.text.split('\n'):
                line = line.strip()
                if line and len(line.split()) == 3:
                    ip_port, user, pwd = line.split()
                    ip, port = ip_port.split(':')
                    proxies.append({
                        'ip': ip,
                        'port': port,
                        'account': user,
                        'password': pwd
                    })
            if not proxies:
                raise Exception("No valid proxies found in response")
            return proxies
        except Exception as e:
            # 失败时返回空列表，避免抛异常阻断
            return []

    def process_request(self, request, spider):
        try:
            if not self.proxy_list:
                self.proxy_list = self._fetch_proxies()
                if not self.proxy_list:
                    spider.logger.error("代理列表为空，未设置代理")
                    return

            proxy_data = random.choice(self.proxy_list)
            proxyMeta = "http://{user}:{password}@{host}:{port}".format(
                host=proxy_data['ip'],
                port=proxy_data['port'],
                user=proxy_data['account'],
                password=proxy_data['password']
            )
            request.meta['proxy'] = proxyMeta
            spider.logger.debug(f'Using proxy: {proxyMeta}')

        except Exception as e:
            spider.logger.error(f'Proxy error: {str(e)}')
            if 'proxy' in request.meta:
                del request.meta['proxy']

    def process_exception(self, request, exception, spider):
        proxy = request.meta.get('proxy')
        if proxy:
            spider.logger.warning(f"请求异常，移除代理: {proxy}")
            self.proxy_list = [p for p in self.proxy_list if
                               "http://{user}:{password}@{host}:{port}".format(
                                   user=p['account'],
                                   password=p['password'],
                                   host=p['ip'],
                                   port=p['port']) != proxy]
        return None


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
        ua = random.choice(self.user_agents)
        request.headers['User-Agent'] = ua
        spider.logger.debug(f'Set User-Agent: {ua}')

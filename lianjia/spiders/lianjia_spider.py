import scrapy
from scrapy.loader import ItemLoader
from lianjia.items import LianjiaItem
import json

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia_spider'

    # 请替换为你自己的Cookie字符串（复制浏览器请求的Cookie）
    cookie_str = 'SECKEY_ABVK=hxHWyOAiImeBXoY6VKogszJRzWvFgQXWkQ6uDmB4m6jzzgHCuqEA3kga0v8ITB0OM9KGaTsV5faNan/H3azYxg%3D%3D; BMAP_SECKEY=hxHWyOAiImeBXoY6VKogszJRzWvFgQXWkQ6uDmB4m6jrJeL4TZsU_IDUBZF3W6AQ6IDIxn2RA2FZjAPbEXYKhLLrJXaKsWrHWUTWdkxh_XE8iqKKxXuJ7i9eBfAR4ZaDQ6pg3Que6o5R3VWvPXuX7yerH7goLrp8YMC1IS9hRzXGIbZFSkG2M2DyDY1o2vfHfxTtfdAkhL3TdsaSNE3GGQ; lianjia_uuid=7489c9e1-40e7-4253-a2c5-96980c4e178f; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1754874866; HMACCOUNT=ACB8FEFB772E3526; _jzqc=1; crosSdkDT2019DeviceId=-q0c4yi-wngoaf-sfuo61fz3gzbu36-kr1g2oz8h; _ga=GA1.2.423872738.1754874877; _gid=GA1.2.736176434.1754874877; _ga_QJN1VP0CMS=GS2.2.s1754874878$o1$g0$t1754874878$j60$l0$h0; _ga_KJTRWRHDL1=GS2.2.s1754874878$o1$g0$t1754874878$j60$l0$h0; login_ucid=2000000128313435; lianjia_token=2.001432c43076164187059fed01b0ea2274; lianjia_token_secure=2.001432c43076164187059fed01b0ea2274; security_ticket=Ua+T8uNr+lK9AwzFsqz3iE8X7OGLBOpwzqUtxpdEueCR1/J/n6Yw03z6Ip9R/ujV4jrNFHJQq5B27dPx92nVR1Va47jBMfQj4CuvBHIiVEPL0u8+zSAan7US6e4rQwkrjxhrOVoHxtoVtOrpxP3ubeA3pjh0RcmHYpAw1N/fEhg=; ftkrc_=2e66f13c-9fd4-4515-a523-ff864789835d; lfrc_=53e1933a-3fb5-42ac-abdd-4784c20bb252; _qzjc=1; _jzqckmp=1; _ga_PV625F3L95=GS2.2.s1754987880$o2$g1$t1754989117$j60$l0$h0; _jzqa=1.3242248109190968000.1754874866.1754992200.1755001293.8; _jzqx=1.1754874866.1755001293.5.jzqsr=cn%2Ebing%2Ecom|jzqct=/.jzqsr=cn%2Ebing%2Ecom|jzqct=/; lianjia_ssid=7ae6157d-21fa-4a85-a9e4-97ae58e4a5f9; hip=WKNNBaQ0dCt92YSgaYb_jpT7ch6o2QZJ2glfPKIRzOW_swhv18eHog9d4wXe93kmE0LCjYHecPshUXhSd6akL6C1xwrcuxvu6xH-wjkkh7TzWMliMA4oXVq_l0gLd3wXZA-9mzx8Dn2HYhq4uw83XmGy9L1dA_NBarvle9_ZFZOAQVh-w_F4NpJSVgk%3D; _ga_WLZSQZX7DE=GS2.2.s1755001322$o2$g0$t1755001322$j60$l0$h0; _ga_TJZVFLS7KV=GS2.2.s1755001322$o2$g0$t1755001322$j60$l0$h0; select_city=510100; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219896b16aac28a-0b049842f2523b-1e462c6f-2073600-19896b16aad18b2%22%2C%22%24device_id%22%3A%2219896b16aac28a-0b049842f2523b-1e462c6f-2073600-19896b16aad18b2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22biying%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1755001576; _qzja=1.1838640628.1754874917037.1754992199504.1755001325281.1755001560693.1755001575517.0.0.0.70.7; _qzjb=1.1755001325280.7.0.0.0; _qzjto=42.5.0; _jzqb=1.10.10.1755001293.1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMjFlOWJiNTQzZjQ0YWU0MDEyNDJlOTNhMTZmNDNjMGUzNzc0MGJlMzBlOTM4ZDYzODk5NzYwZGYyNmVjMDA5MWRkNWM4ZDYzYjllMGVlMzIyNWM0ZGE0YWQ0MjFlNmJkNTQzY2Y2N2NlZDY4ODQ2Mjc4YTIzZDYyYWZkNTU2Yjk3NWFmMjMzMjNkM2Y2YjRhYjhhNzEwNTNkZDMwNDQ4NjdhNDhkOWYyYjc4MTFhYzcwMzU0YWNiODZlY2JiYzg0YWMxYTI0ODk3YzYwNzNhM2Q3NTAwMzNiNGQ0ZTExOWQ2NDg5ZTAwNjkxMGNiNWFhZmUyZWUxMTVlZjM1YTk1M2NhMjBlZWY2ZWIyODAzZTMxZWFmZDM0YmM0YjUxNjM3M2E1YzEwYmRkNjYxZDBmOWE5YjEzOWE0YTA2YTYxNTNcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiOGVmYzY5MGJcIn0iLCJyIjoiaHR0cHM6Ly9jZC5saWFuamlhLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _ga_NKBFZ7NGRV=GS2.2.s1755001344$o7$g1$t1755001586$j45$l0$h0; _ga_XLL3Z3LPTW=GS2.2.s1755001344$o7$g1$t1755001586$j45$l0$h0'

    allowed_domains = ['lianjia.com']
    start_urls = ['https://cd.lianjia.com/ershoufang/rs/']

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        # 根据需要可启用日志级别为INFO
        'LOG_LEVEL': 'INFO',
    }

    def cookie_str_to_dict(self, cookie_str):
        cookie_dict = {}
        for kv in cookie_str.split('; '):
            if '=' in kv:
                k, v = kv.split('=', 1)
                cookie_dict[k] = v
        return cookie_dict

    def start_requests(self):
        cookies = self.cookie_str_to_dict(self.cookie_str)
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/127.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "zh-CN,zh;q=0.9",
        }

        for url in self.start_urls:
            yield scrapy.Request(
                url,
                cookies=cookies,
                headers=headers,
                callback=self.parse
            )

    def parse(self, response):
        self.logger.info(f'Got response url: {response.url}')
        
        house_links = response.css('.sellListContent li .title a::attr(href)').getall()
        self.logger.info(f"当前页 {response.url}，抓取到房源链接数量: {len(house_links)}")

        cookies = self.cookie_str_to_dict(self.cookie_str)
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/127.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "zh-CN,zh;q=0.9",
        }

        for link in house_links:
            yield scrapy.Request(
                url=response.urljoin(link),
                callback=self.parse_house_detail,
                cookies=cookies,
                headers=headers,
            )

        # 使用页面上的下一页链接，不自己拼url，防止出错
        next_page = response.css('.page-box .next::attr(href)').get()
        if next_page:
            next_url = response.urljoin(next_page)
            self.logger.info(f"准备爬取下一页: {next_url}")
            yield scrapy.Request(
                url=next_url,
                callback=self.parse,
                cookies=cookies,
                headers=headers,
            )
        else:
            self.logger.info("没有找到下一页，爬取结束。")

    def parse_house_detail(self, response):
        if response.status != 200:
            self.logger.warning(f"详情页请求失败，状态码: {response.status}, URL: {response.url}")
            return

        self.logger.info(f"详情页请求成功: {response.url}")
        loader = ItemLoader(item=LianjiaItem(), response=response)

        loader.add_css('title', '.title .main::text')
        loader.add_css('price', '.price .total::text')
        loader.add_css('unit_price', '.unitPrice .unitPriceValue::text')
        loader.add_css('community', '.communityName .info::text')
        loader.add_css('district', '.areaName .info a::text')
        loader.add_value('detail_url', response.url)

        house_info = {}
        for info in response.css('.introContent .content li'):
            key = info.css('span.label::text').get()
            value = info.css('::text').getall()[-1].strip() if info.css('::text').getall() else ''
            if key:
                house_info[key] = value
        loader.add_value('basic_info', house_info)

        transaction_info = {}
        for info in response.css('.transaction .content li'):
            key = info.css('span.label::text').get()
            value = info.css('span:nth-child(2)::text').get()
            if key:
                transaction_info[key] = value
        loader.add_value('transaction_info', transaction_info)

        position_info = response.css('.areaName .info a::text').getall()
        if len(position_info) >= 2:
            loader.add_value('location', ' '.join(position_info[:2]))

        item = loader.load_item()
        self.logger.info(f"生成item: {item}")
        yield item

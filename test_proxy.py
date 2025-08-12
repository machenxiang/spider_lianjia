import requests

# 链家目标 URL
url = "https://cd.lianjia.com/ershoufang/"

# 你的链家 Cookie（替换为你自己的）
cookies_str = "SECKEY_ABVK=hxHWyOAiImeBXoY6VKogszJRzWvFgQXWkQ6uDmB4m6jzzgHCuqEA3kga0v8ITB0OM9KGaTsV5faNan/H3azYxg%3D%3D; BMAP_SECKEY=hxHWyOAiImeBXoY6VKogszJRzWvFgQXWkQ6uDmB4m6jrJeL4TZsU_IDUBZF3W6AQ6IDIxn2RA2FZjAPbEXYKhLLrJXaKsWrHWUTWdkxh_XE8iqKKxXuJ7i9eBfAR4ZaDQ6pg3Que6o5R3VWvPXuX7yerH7goLrp8YMC1IS9hRzXGIbZFSkG2M2DyDY1o2vfHfxTtfdAkhL3TdsaSNE3GGQ; lianjia_uuid=7489c9e1-40e7-4253-a2c5-96980c4e178f; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1754874866; HMACCOUNT=ACB8FEFB772E3526; _jzqc=1; crosSdkDT2019DeviceId=-q0c4yi-wngoaf-sfuo61fz3gzbu36-kr1g2oz8h; _ga=GA1.2.423872738.1754874877; _gid=GA1.2.736176434.1754874877; _ga_QJN1VP0CMS=GS2.2.s1754874878$o1$g0$t1754874878$j60$l0$h0; _ga_KJTRWRHDL1=GS2.2.s1754874878$o1$g0$t1754874878$j60$l0$h0; login_ucid=2000000128313435; lianjia_token=2.001432c43076164187059fed01b0ea2274; lianjia_token_secure=2.001432c43076164187059fed01b0ea2274; security_ticket=Ua+T8uNr+lK9AwzFsqz3iE8X7OGLBOpwzqUtxpdEueCR1/J/n6Yw03z6Ip9R/ujV4jrNFHJQq5B27dPx92nVR1Va47jBMfQj4CuvBHIiVEPL0u8+zSAan7US6e4rQwkrjxhrOVoHxtoVtOrpxP3ubeA3pjh0RcmHYpAw1N/fEhg=; ftkrc_=2e66f13c-9fd4-4515-a523-ff864789835d; lfrc_=53e1933a-3fb5-42ac-abdd-4784c20bb252; _ga_TJZVFLS7KV=GS2.2.s1754874911$o1$g0$t1754874911$j60$l0$h0; _ga_WLZSQZX7DE=GS2.2.s1754874911$o1$g0$t1754874911$j60$l0$h0; _qzjc=1; _jzqckmp=1; _jzqa=1.3242248109190968000.1754874866.1754980559.1754987689.6; _jzqx=1.1754874866.1754987689.4.jzqsr=cn%2Ebing%2Ecom|jzqct=/.jzqsr=cd%2Elianjia%2Ecom|jzqct=/; lianjia_ssid=9bed38e2-17bc-4ec8-b05d-5f12bcba6267; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219896b16aac28a-0b049842f2523b-1e462c6f-2073600-19896b16aad18b2%22%2C%22%24device_id%22%3A%2219896b16aac28a-0b049842f2523b-1e462c6f-2073600-19896b16aad18b2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22biying%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; hip=TQkxRjG3QeA3onV9wDd_b8x99F5Q9XOhn-UwJlY21sIrulaHhmcZLwf9HccSZWAGaZkB9gcR7vbSionQV-6IguRyGlZMfhXx4bZK_yx8EtU9HzUdxkbtX8-olHWOzY_wnv0Iwg4L8hn-H31f3erSFazF3PbdtjybYmOXqwkaR9u_yw3b_TptF4H4Zg%3D%3D; _ga_PV625F3L95=GS2.2.s1754987880$o2$g1$t1754989117$j60$l0$h0; select_city=510100; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1754989403; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMjFlOWJiNTQzZjQ0YWU0MDEyNDJlOTNhMTZmNDNjMGUzNzc0MGJlMzBlOTM4ZDYzODk5NzYwZGYyNmVjMDA5MWRkNWM4ZDYzYjllMGVlMzIyNWM0ZGE0YWQ0MjFlNmJkNTQzY2Y2N2NlZDY4ODQ2Mjc4YTIzZDYyYWZkNTU2Yjk3NWFmMjMzMjNkM2Y2YjRhYjhhNzEwNTNkZDMwNDQ4NjdhNDhkOWYyYjc4MTFhYzcwMzU0YWNiODZlY2JiYzg0ZGY1NjExNjQyMTA2YmFjM2MxMWQ0YTU3MmI1NTE5Mjk3YTJiYjUyNDU2MmYwZTc4ZjdlMGVlMjRjYzFiZjc4NzZjOWE3ZGE2Nzc5MDIzNzIxOWEwZTBkZWU4ZDhiZjViM2ZjNTFiNTQ1MGZkNDdmODVhNGQ3ZGNlYzgxNmVkNWRcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiZjgzMDM1ZjhcIn0iLCJyIjoiaHR0cHM6Ly9jZC5saWFuamlhLmNvbS9lcnNob3VmYW5nL3JzLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _jzqb=1.21.10.1754987689.1; _qzja=1.1838640628.1754874917037.1754980559132.1754987689149.1754989388466.1754989403880.0.0.0.60.5; _qzjb=1.1754987689149.18.0.0.0; _qzjto=32.3.0; _ga_XLL3Z3LPTW=GS2.2.s1754987703$o5$g1$t1754989415$j60$l0$h0; _ga_NKBFZ7NGRV=GS2.2.s1754987703$o5$g1$t1754989415$j60$l0$h0"

# 转换 Cookie 字符串为字典
cookies = {k.strip(): v for k, v in (item.split("=", 1) for item in cookies_str.split(";"))}

# 代理列表：IP 端口 用户名 密码
raw_proxies = """
171.83.204.56:12605 xmdlc1e6 xmdl3c4f
115.196.223.204:11629 xmdlc1e6 xmdl3c4f
114.232.248.223:11420 xmdlc1e6 xmdl3c4f
171.40.167.171:11432 xmdlc1e6 xmdl3c4f
183.136.251.70:22621 xmdlc1e6 xmdl3c4f
60.177.190.201:10351 xmdlc1e6 xmdl3c4f
114.232.9.17:14146 xmdlc1e6 xmdl3c4f
220.190.63.3:10534 xmdlc1e6 xmdl3c4f
125.78.229.122:11965 xmdlc1e6 xmdl3c4f
113.226.107.179:13684 xmdlc1e6 xmdl3c4f
""".strip().split("\n")

# 转换成 requests 代理格式
proxies_list = [
    f"http://{user}:{pwd}@{ip_port}"
    for ip_port, user, pwd in (line.split() for line in raw_proxies)
]

# 测试
for proxy in proxies_list:
    try:
        resp = requests.get(
            url,
            proxies={"http": proxy, "https": proxy},
            cookies=cookies,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
            },
            timeout=8
        )
        if "captcha" in resp.url.lower():
            print(proxy, "❌ 验证码拦截")
        elif resp.status_code == 200:
            print(proxy, "✅ 可用")
        else:
            print(proxy, f"⚠ 状态码 {resp.status_code}")
    except Exception as e:
        print(proxy, "❌ 连接失败", e)

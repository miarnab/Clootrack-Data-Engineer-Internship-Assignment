import requests
from bs4 import BeautifulSoup
from itertools import cycle
import time

proxies = [
    'http://128.14.65.84:443',
    'http://234.567.89.01:8080',
    'http://345.678.90.12:8080',
]

proxy_pool = cycle(proxies)

url = 'http://testhtml5.vulnweb.com/#/popular/page/1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

max_retries = 3

for _ in range(len(proxies)):
    proxy = next(proxy_pool)
    print(f"Using proxy: {proxy}")
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=60)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            print(f"Page title: {soup.title.text}")
            break
        except requests.exceptions.ProxyError:
            print(f"Proxy error with {proxy}. Trying a new proxy...")
            break
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} with proxy {proxy} failed: {e}")
            time.sleep(2)
        else:
            break
    else:
        continue
    break

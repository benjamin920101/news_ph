from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def extract_public_health_news(search_text, num_results):
    search_results = search(search_text, num_results=num_results)

    mohw_urls = []
    for result in search_results:
        match = re.search(r'(https?://mohw\.gov\.tw/[^&]+)', result)
        if match:
            mohw_urls.append(match.group(1))

    html_contents = []
    for url in mohw_urls:
        response = requests.get(url)
        html_contents.append(response.text)

    news_data = []
    for html_content in html_contents:
        soup = BeautifulSoup(html_content, 'html.parser')
        # 根據 HTML 結構提取相關資訊，並添加到 news_data 中
        # ...

    df = pd.DataFrame(news_data)
    return df

# 使用範例
search_text = '公共衛生新聞 site:mohw.gov.tw'
num_results = 10
df = extract_public_health_news(search_text, num_results)
print(df)

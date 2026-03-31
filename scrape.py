from ludotrack_backend.scrapers.news.main import scrape_news
from ludotrack_backend.scrapers.x.corvx.corvx import Corvx
from waybackshot import WaybackShot
import pandas as pd
import sys
from googlenewsdecoder import gnewsdecoder

if __name__=="__main__":
    waybackshot = WaybackShot()
    queries = ["riesgos redes sociales adolescentes", "derechos adolescentes afectados redes sociales", "cómo frenar la adicción redes sociales"]
    queries_x = ["ciberacoso"]
    if sys.argv[1] == "X":
        # corvx = Corvx()
        # for query in queries_x:
        #     query_dict = {
        #         "fields": [
        #             {"items": [query], "target": "hashtag"},          
        #         ],
        #         "since": "2026-03-30",
        #         "until": "2026-03-31",
        #         "lang": "es",
        #     }
        #     tweets = corvx.search(query_dict)
        #     for tweet in tweets:
        #         print(f'{tweet["text"]}\n{tweet["url"]}')
        url_tweet = "https://x.com/NoticiasTermo/status/2038771184121049243"
        waybackshot.get_screenshot_from(url_tweet, dir="./data/x/screenshots/")

    elif sys.argv[1] == "news":
        news_data = []
        for query in queries:
            articles = scrape_news(query)
            for article in articles:
                url = article.get("url")
                url_original = gnewsdecoder(url)['decoded_url']
                news_data.append({
                    "query": query,
                    "title": article.get("title"),
                    "url": url_original,
                    "text": article.get("text"),
                    "source": article.get("source")
                })
                waybackshot.get_screenshot_from(url_original, dir="./data/news/screenshots/")
        

        pd.DataFrame(news_data).to_csv("./data/news/news_data.csv", index=False) ##### BUG in saving df

    

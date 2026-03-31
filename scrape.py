from ludotrack_backend.scrapers.news.main import scrape_news
from waybackshot import WaybackShot
import pandas as pd
from googlenewsdecoder import gnewsdecoder

if __name__=="__main__":
    waybackshot = WaybackShot()
    queries = ["riesgos redes sociales adolescentes", "derechos adolescentes afectados redes sociales", "cómo frenar la adicción redes sociales"]
    queries_x = ["#ciberacoso", "#ciberbullying"]

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
     

    pd.DataFrame(news_data).to_csv("./data/news/news_data.csv", index=False)

    

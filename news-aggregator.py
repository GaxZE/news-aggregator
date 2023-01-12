from rss_parser import Parser
from requests import get


def get_articles(search):
    news_list = []
    for term in search:
        url = f"https://news.google.com/rss/search?q={term}&hl=en-GB&gl=GB&ceid=GB:en"
        xml = get(url)
        parser = Parser(xml=xml.content, limit=5)
        feed = parser.parse()

        for item in feed.feed:
            try:
                news = {
                    "title": item.title,
                    "link": item.link,
                    "date": item.publish_date
                }
                news_list.append(news)
            except:
                pass
    return news_list


for article in get_articles(["QPR", "South Oxhey"]):
    print(article["title"])
    print(article["link"])
    print(article["date"])
    print("--")

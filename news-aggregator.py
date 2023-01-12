from rss_parser import Parser
from requests import get


def get_articles(search):
    url = f"https://news.google.com/rss/search?q={search}&hl=en-GB&gl=GB&ceid=GB:en"
    xml = get(url)
    parser = Parser(xml=xml.content, limit=10)
    feed = parser.parse()
    news_list = []

    for item in feed.feed:
        try:
            news_list.append(item.title)
        except:
            pass
    return news_list


for title in get_articles("QPR"):
    print(title)

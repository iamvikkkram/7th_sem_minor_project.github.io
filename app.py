from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route("/")
def home():
    api_key = 'a2e15100adb84caf8f3de3d3a6f54989'
    
    newsapi = NewsApiClient(api_key=api_key)

    top_headlines = newsapi.get_top_headlines(sources = "bbc-news")
    all_articles = newsapi.get_everything(sources = "bbc-news")

    t_articles = top_headlines['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip( news,desc,img,p_date,url)


    return render_template('index.html',contents=contents)


if __name__ == '__main__':
    app.run(debug=True)
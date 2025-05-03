import newspaper
from newspaper import Article
import json 
with open("./log.json", "r") as f:
    urls_json = json.load(f)
for url_json in urls_json:
    article = Article(url_json['url'])
    article.download()
    article.parse()
    with open('./data_train.txt','a') as f:
        f.write(article.text.strip()+'\n')



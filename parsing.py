import requests
from bs4 import BeautifulSoup as BS
import json

main_url  ='https://kaktus.media/?lable=8'


def get_url(url):
    response = requests.get(url)
    return response.text


def get_all_news(html):
    soup = BS(html,'lxml')
    list_news = soup.find('div',{'class':'Tag--articles'})
    news = list_news.find_all('div',{'class':'ArticleItem'})
    
    list1 = []
    for i in news:  
        title = i.find('a',{'class':'ArticleItem--name'}).text.strip()
        image = i.find('a',{'class':'ArticleItem--image'}).find('img').get('src')
        description = i.find('a',{'class':'ArticleItem--name'}).get('href')
        list1.append({'image':image,'title':title,'description':description})   
    return dict(enumerate(list1, 1))
a = get_all_news(get_url(main_url))
# print(a)

with open('a.json','w') as file:
    json.dump(a,file,indent =4,ensure_ascii=False)



# return dict(enumerate(list1, 1))
# -*- coding: utf-8 -*-

import requests 
import re
from bs4 import BeautifulSoup
import time
import csv

def get_paper_keywords(link):
    #поиск ключевых слов на странице
    paper_page = requests.get(link)
    paper_soup = BeautifulSoup(paper_page.content, 'html.parser')
    if len(paper_soup.head('meta', attrs={'name': 'keywords'})) != 0:
        return paper_soup.head('meta', attrs={'name': 'keywords'})[0]['content']
    else:
        print(link)
        return None

def get_papers(init = False):
    news = []
    papers = source_soup.find_all('article')
    for paper in papers:
        ref = paper('a', attrs={'href': re.compile('https://www.cbsnews.com/news/')})
        #print('1:', paper)
        if len(ref) != 0:
            link = ref[0]['href']
            if init:
                initialization_refs.add(link)
            elif not link in initialization_refs:
                features_news = {}
                features_news['url'] = link
                features_news['header'] = paper(class_ = 'item__hed')[0].text.strip()
                features_news['description'] = paper(class_ = 'item__dek')[0].text.strip()
                features_news['keywords'] = get_paper_keywords(link)
                news.append(features_news)
                initialization_refs.add(link)
    return news 

def writer_file_news(FILENAME = 'news', news_list = [], init = False):
    with open(FILENAME, "a", newline="", encoding='utf-8') as file:
        columns = ["url", "header", "description", "keywords"]
        writer = csv.DictWriter(file, fieldnames=columns)
        if init: writer.writeheader()
        writer.writerows(news_list)

print('Начало работы: ', time.asctime())
init_time = time.clock()
running_time = time.clock() - init_time

source_url = 'https://www.cbsnews.com/politics/'
source_page = requests.get(source_url)
source_soup = BeautifulSoup(source_page.content, 'html.parser')

#новости, опубликованные до запуска кода, не анализируются
initialization_refs = set() 
get_papers(True)

writer_file_news('GOP_news.csv', [], True)
writer_file_news('Democrat_news.csv',[], True)
writer_file_news('Another_news.csv', [], True)
t = 1

while running_time < 86400: #меньше суток
    
    source_page = requests.get(source_url)
    source_soup = BeautifulSoup(source_page.content, 'html.parser')
    news = get_papers()
    
    #Распределение новостей по ключевым словам в соотвествующие массивы 
    GOP_news =[]
    Democrat_news = []
    Another_news = []
    
    for n in news:
        if 'republican party' in n['keywords'] or 'GOP' in n['keywords'] or 'republicans' in n['keywords']:
            GOP_news.append(n)
        if 'democratic party' in n['keywords'] or 'democrats' in n['keywords']:
            Democrat_news.append(n)
        if not 'republican party' in n['keywords'] and not 'GOP' in n['keywords'] and not 'democratic party' in n['keywords'] and not 'democrats' in n['keywords'] and not 'republicans' in n['keywords']:
            Another_news.append(n)
        
    writer_file_news('GOP_news.csv', GOP_news )
    writer_file_news('Democrat_news.csv',Democrat_news)
    writer_file_news('Another_news.csv', Another_news)
    
    print('Проход %s'%t)
    t=t+1
    time.sleep(3600) #пауза
    
    running_time = time.clock() - init_time
    print('Общее время работы: ', int(running_time/60), 'минут')
    
    
print('Конец работы: ', time.asctime())


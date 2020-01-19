import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

DOMAIN = 'en.wikipedia.org'
HOST = 'https://'+ DOMAIN

def get_random_url():
    page = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    return page.url


def get_links(url):
    link_list=[]
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    content = soup.find(id='mw-content-text')
    for ref in content.find_all('a', attrs={'href': re.compile('/wiki/')}):
        link = ref['href']
        if not ':' in link:
            if link.startswith('/') and not link.startswith('//'):
                link = HOST + ref['href']
            if urlparse(link).netloc == DOMAIN:
                link_list.append(link)
    return link_list


def searchlink(url_beg,url_dest, deph,loop,stop,bestway):
    if deph<0:
        return (stop,url_beg)
    deph-=1
    graph={}
    print('Level: %s  URL: %s'%(deph+1,url_beg))
    list_link=get_links(url_beg)
    for url in list_link:
        if not url in loop:
            if url.upper()==url_dest.upper():
                deph=-1
                stop=True
            loop.add(url)
            stop,graph[url]=searchlink(url,url_dest,deph,loop,stop,bestway)
            if stop:
                bestway.append(url)
                break
    return (stop,graph)

def main():
    graph_start_to_stop={}
    graph_stop_to_start = {}
    bestway_forward=[]
    bestway_backward=[]
    loop=set()

    start_url= get_random_url() #
    stop_url = get_random_url() #
    loop.add(start_url)
    stop,graph_start_to_stop[start_url]=searchlink(start_url,stop_url,10,loop,False, bestway_forward)
    stop,graph_stop_to_start[stop_url]=searchlink(stop_url,start_url,10,loop,False, bestway_backward)

    bestway_forward=bestway_forward.reverse()
    print('From URL:%s to URL:%s best way:'%(start_url,stop_url,bestway_forward))

    bestway_backward=bestway_backward.reverse()
    print('From URL:%s to URL:%s best way:'%(stop_url,start_url,bestway_backward))


if __name__ == '__main__':
    main()
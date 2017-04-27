#!/usr/bin/env python3
# pbf comic downloader

import os, requests, bs4


# defines output folder
def out_folder():
    while True:
        print('Enter save directory:')
        output_folder = str(input())
        if os.path.exists(output_folder) is True:
            break
        else:
            os.makedirs(output_folder)
            break
    return output_folder


# gives first comic adres to download
def url_starter(number):
    url = 'http://pbfcomics.com/' + number + '/'
    return url


# opens page
def url_opener(url):
    opener = requests.get(url)
    opener.raise_for_status()
    try:
        opener.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    return opener


# soup process on opened page
def soup_processing(opener):
    opener_soup = bs4.BeautifulSoup(opener.text, 'html.parser')
    return opener_soup


# finds comic file to download
def comic_processing(opener_soup):
    comic = opener_soup.select('img')
    if comic is None:
        print('Comic not found')
    else:
        comic_addres = 'http://pbfcomics.com'+comic[0].get('src')
        comic_url = requests.get(comic_addres)
        return comic_addres, comic_url


# downloads file to hard drive
def comic_saver(comic_adres, comic_url):
    download = open(output_folder+'/'+ comic_addres[31:], 'wb')
    print('downloading comic... '+ comic_addres[31:])
    for chunk in comic_url.iter_content(100000):
        download.write(chunk)
    download.close()


# searches for +1 older comic page
def older_comic(opener_soup):
    prev_link = opener_soup.select('#older')
    url = 'http://pbfcomics.com'+prev_link[0].get('href')
    return url


output_folder = out_folder()
url = None
print('Enter newest comic number: ')
number = input()


for i in range(int(number)):
    if url is None:
        url = url_starter(number)
    else:
        url_opener(url)
        opener = url_opener(url)
        opener_soup = soup_processing(opener)
        comic_addres, comic_url = comic_processing(opener_soup)
        comic_saver(comic_addres, comic_url)
        url = older_comic(opener_soup)
import requests
import pprint
from bs4 import BeautifulSoup


def search_books(query, limit=None):
    url = f"https://flibusta.site/booksearch?ask={query}&chb=on"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for li in soup.find_all('li'):
        a_tag = li.find('a')
        if a_tag and '/b/' in a_tag['href']:
            book_title = a_tag.text
            book_url = "https://flibusta.site" + a_tag['href'] 
            author = li.find_all('a')[-1].text
            books.append({
                "title": book_title,
                "author": author,
                "book_url": f'{book_url}',
                "download_url_fb2": f'{book_url}/fb2',
                "download_url_epub": f'{book_url}/epub',
                "download_url_mobi": f'{book_url}/mobi'
            })
            if limit and len(books) >= limit:
                break

    return books

if __name__ == '__main__':
    result = search_books("Хоббит")
    pprint.pprint(result, sort_dicts=False)

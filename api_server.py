from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from main import search_books

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    book_url: str
    download_url_fb2: str
    download_url_epub: str
    download_url_mobi: str


class Search(BaseModel):
    query: str
    limit: int = None

@app.post('/get_books', response_model=List[Book])
def search(search: Search):
    books = search_books(search.query, search.limit)
    return books

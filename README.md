# Flibusta API

A simple API built with FastAPI to search for books from the Flibusta library. This API allows users to query for books based on a search term and retrieve relevant book information including titles, authors, and download links in various formats.

## Features

- Search for books by title or author.
- Retrieve book details including:
  - Title
  - Author
  - Links to book pages
  - Download links in FB2, EPUB, and MOBI formats

## Technologies Used

- Python
- FastAPI
- Pydantic
- BeautifulSoup
- Requests

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Lorgar-Horusov/flibusta-api.git
   cd flibusta-api
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
1. As a web server
   1. Start the FastAPI server:
       ```bash
       uvicorn api_server:app --reload
       ```
   2. Access the API documentation at `http://127.0.0.1:8000/docs`
   3. To search for books, send a POST request to /get_books with a JSON body:
       ```json
       {
       "query": "your_search_query",
       "limit": 10 
       }
       ```
   4. Example using curl:
       ```bash
       curl -X POST "http://127.0.0.1:8000/get_books" -H "Content-Type: application/json" -d '{"query": "Хоббит", "limit": 5}'
       ```
       #### Example Response
       ```json
       [
         {
             "title": "book_name",
             "author": "book_autor",
             "book_url": "https://flibusta.site/b/123456",
             "download_url_fb2": "https://flibusta.site/b/123456/fb2",
             "download_url_epub": "https://flibusta.site/b/123456/epub",
             "download_url_mobi": "https://flibusta.site/b/123456/mobi"
         }
       ]
       ```
2. As a module
   1. Import the `search_books` function from the `search` file
      ```py
      from search import search_books
      ```
   2. book search example
      ```py
      from search import search_books
      import pprint

      
      def main():
           search_books(query='book_name', limit=3)


      if __name__ == '__main__':
           response main()
           pprint.pprint(response, sort_dicts=False)
      ```
       #### Example Response
       ```bash
       [
         {
             "title": "book_name",
             "author": "book_autor",
             "book_url": "https://flibusta.site/b/123456",
             "download_url_fb2": "https://flibusta.site/b/123456/fb2",
             "download_url_epub": "https://flibusta.site/b/123456/epub",
             "download_url_mobi": "https://flibusta.site/b/123456/mobi"
         }
       ]
       ```

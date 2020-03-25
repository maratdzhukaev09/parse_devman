import requests, os, json, argparse
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
from urllib.parse import urljoin
from itertools import groupby

parser = argparse.ArgumentParser(
    description='This parser is designed to quickly and efficiently search for data on science fiction \
    books from tululu.org. At the same time, you can download their contents and their covers.'
)
parser.add_argument('--start_page', help='First page', type=int)
parser.add_argument('--end_page', help='Last page', type=int)
parser.add_argument('--dest_folder', help='Path to the directory with parsing results: images, books, JSON')
parser.add_argument('--skip_imgs', help='Do not download pictures', type=bool)
parser.add_argument('--skip_txt', help='Do not download books')
parser.add_argument('--json_path', help='Indicate your path to the * .json file with the results')
args = parser.parse_args()

def download_picture(url, filename, folder='images/'):
    filepath = os.path.join(folder, sanitize_filename(filename))

    response = requests.get(url, allow_redirects=False)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)

    return filepath

def download_txt(url, filename, folder='books/'):
    filepath = os.path.join(folder, sanitize_filename(filename))

    response = requests.get(url, allow_redirects=False)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)

    return filepath

def get_description_book(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')

    selector_ta = 'td.ow_px_td h1'
    title, author = soup.select_one(selector_ta).text.split('   ::   ')
    book_path = urljoin('http://tululu.org/', soup.find('a', title=title+' - скачать книгу txt')['href'])
    selector_pp = 'div.bookimage img'
    picture_path = urljoin('http://tululu.org/', soup.select_one(selector_pp)['src'])
    selector_c = 'div.texts span'
    comments = [comment.text for comment in soup.select(selector_c)]
    selector_g = 'span.d_book a'
    genres = [genre.text for genre in soup.select(selector_g)]

    return title, author, comments, genres, book_path, picture_path

def check_url(url):
    response = requests.get(url, allow_redirects=False)
    response.raise_for_status()

    try:
        get_description_book(url)
        return True
    except:
        return False


start_page, end_page = args.start_page, args.end_page
if end_page is None:
    end_page = 702
if start_page is None:
    start_page = 1

if args.json_path:
    filename = args.json_path
else:
    filename = "library.json"

os.makedirs("books", exist_ok=True)
os.makedirs("images", exist_ok=True)
if args.dest_folder:
    print(str(str(os.path.abspath('books/')).split('books')[0]))

id_list = []
library = []
get_description_book('http://tululu.org/b9/')

for page in range(start_page, end_page):
    url = urljoin('http://tululu.org/l55/', str(page) + '/')
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    selector_list = 'table.d_book'
    page_id_list = [urljoin('http://tululu.org/', id_.select_one('a')['href']) for id_ in soup.select(selector_list)]
    id_list += page_id_list
    print(page_id_list)

for id_ in id_list:
    if check_url(id_):
        book = dict()
        book['title'], book['author'], book['comments'], book['genres'], url_book, url_image = get_description_book(id_)

        if args.skip_txt:
            book['book_path'] = None
        else:
            book['book_path'] = download_txt(url_book, book['title'] + '.txt')
        if args.skip_imgs:
            book['image_src'] = None
        else:
            image_filename = url_image.split('/')[-1]
            book['image_src'] = download_picture(url_image, image_filename)

        library.append(book)

with open(filename, "w", encoding='utf8') as file:
    json.dump([], file, ensure_ascii=False)
with open(filename, "r") as file:
    library_old = json.load(file)
with open(filename, "w", encoding='utf8') as file:
    library_new = [el for el, _ in groupby(library_old + library)]
    json.dump(library_new, file, ensure_ascii=False)

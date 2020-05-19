import requests, os, json, argparse, datetime, time
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
from urllib.parse import urljoin
from itertools import groupby

def write_json(added_library, filename):
    if not os.path.exists(filename):
        with open(filename, "w", encoding='utf8') as file:
            json.dump([], file, ensure_ascii=False)
    with open(filename, "r") as file:
        old_library = json.load(file)
    with open(filename, "w", encoding='utf8') as file:
        new_library = [el for el, _ in groupby(old_library + added_library)]
        json.dump(new_library, file, ensure_ascii=False)

def get_response(url):
    try:
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()
        if response.is_redirect:
            raise requests.HTTPError('Url redirect.')
        return response
    except requests.exceptions.ConnectionError:
        time.sleep(15)
        print('Trying to reconnect...')
        return get_response(url)
    except ConnectionError:
        time.sleep(15)
        print('Trying to reconnect...')
        return get_response(url)

def download_picture(url, filename, folder='images'):
    filepath = os.path.join(folder, sanitize_filename(filename))
    response = get_response(url)
    with open(filepath, 'wb') as file:
        file.write(response.content)

    return filepath

def download_txt(url, filename, folder='books'):
    filepath = os.path.join(folder, sanitize_filename(filename))
    response = get_response(url)
    with open(filepath, 'wb') as file:
        file.write(response.content)

    return filepath

def get_book(url):
    response = get_response(url)
    soup = BeautifulSoup(response.text, 'lxml')

    selector_ta = 'td.ow_px_td h1'
    title, author = soup.select_one(selector_ta).text.split('   ::   ')
    txt_href = soup.find('a', title=f'{title} - скачать книгу txt')['href']
    txt_url = urljoin(url, txt_href)
    selector_pp = 'div.bookimage img'
    image_href = soup.select_one(selector_pp)['src']
    image_url = urljoin(url, image_href)
    selector_c = 'div.texts span'
    comments = [comment.text for comment in soup.select(selector_c)]
    selector_g = 'span.d_book a'
    genres = [genre.text for genre in soup.select(selector_g)]

    return title, author, comments, genres, txt_url, image_url

def check_page(url):
    try:
        get_book(url)
        return True
    except TypeError:
        return False

def get_page_urls(url):
    response = get_response(url)
    soup = BeautifulSoup(response.text, 'lxml')
    page_urls = [urljoin(url, id_.select_one('a')['href']) for id_ in soup.select('table.d_book')]

    return page_urls

def get_args():
    parser = argparse.ArgumentParser(
        description='This parser is designed to quickly and efficiently search for data on science fiction \
            books from tululu.org. At the same time, you can download their contents and their covers.'
    )
    parser.add_argument('--start_page', help='First page', type=int, default=0)
    parser.add_argument('--end_page', help='Last page', type=int, default=702)
    parser.add_argument('--dest_folder', help='Path to the directory with parsing results: images, books, JSON', type=str, default="")
    parser.add_argument('--skip_imgs', help='Do not download pictures', type=bool, default=False)
    parser.add_argument('--skip_txt', help='Do not download books', type=bool, default=False)
    parser.add_argument('--json_path', help='Indicate your path to the * .json file with the results', type=str, default="library.json")
    args = parser.parse_args()

    return args

def main():
    args = get_args()
    if args.dest_folder == "":
        json_filename = args.json_path
    else:
        json_filename = os.path.join(args.dest_folder, "library.json")
    books_folder = os.path.join(args.dest_folder, "books")
    image_folder = os.path.join(args.dest_folder, "images")
    os.makedirs(books_folder, exist_ok=True)
    os.makedirs(image_folder, exist_ok=True)
    start_page, end_page = args.start_page, args.end_page
    urls = []
    library = []

    for page in range(start_page, end_page):
        url = urljoin('http://tululu.org/l55/', f"{page}/")
        urls += get_page_urls(url)

    for url in urls:
        if not check_page(url):
            continue
        book = dict()
        book['title'], book['author'], book['comments'], book['genres'], txt_url, image_url = get_book(url)

        if args.skip_txt:
            book['book_path'] = None
        else:
            book_filename = f"{book['title']}{datetime.datetime.today().timestamp()}.txt"
            book['book_path'] = download_txt(txt_url, book_filename, books_folder)
        if args.skip_imgs:
            book['image_src'] = None
        else:
            image_filename = image_url.split('/')[-1].split('.')[0] + str(datetime.datetime.today().timestamp()) + ".jpg"
            book['image_src'] = download_picture(image_url, image_filename, image_folder)

        library.append(book)

    write_json(library, json_filename)

if __name__ == "__main__":
    main()
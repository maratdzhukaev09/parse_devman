# Парсер книг с сайта [tululu.org](http://tululu.org/)

Данный парсер предназначен для быстрого и эффективного поиска данных о книгах в жанре научной фантастики с сайта [tululu.org](http://tululu.org/). При этом вы можете скачивать их содержание и их обложки.

## Подготовка к запуску

Для запуска кода у вас уже должен быть установлен Python 3.

- Скачайте код.
- Установите нужные библиотеки командой `pip install requests BeautifulSoup4 lxml pathvalidate urllib3`.
- Запутите код командой `python parse_tululu_category.py`.

**! Команда устанавливает все книги в жанре научной фантастики (прочитайте про аргументы). !**

## Аргументы

<<<<<<< HEAD
### --start_page X
=======
### --start_page xxx
>>>>>>> 6debdbaf8c88df08b85fcd27d9392824cadfb239

xxx - (int, по умолчанию `0`, <702) страница, с которой начинается скачивание книг.

`python parse_tululu_category.py --start_page 700`
<<<<<<< HEAD
`#Скачаются все книги, начиная с 700 страницы`

### --end_page X
=======

`#Скачаются все книги, начиная с 700 страницы`

### --end_page xxx
>>>>>>> 6debdbaf8c88df08b85fcd27d9392824cadfb239

xxx - (int, по умолчанию `702`, <702) страница, до которой скачиваются книги.

`python parse_tululu_category.py --end_page 701`
<<<<<<< HEAD
`#Скачаются все книги, до 702 страницы`

`python parse_tululu_category.py --start_page 700 --end_page 701`
=======

`#Скачаются все книги, до 702 страницы`

`python parse_tululu_category.py --start_page 700 --end_page 701`

>>>>>>> 6debdbaf8c88df08b85fcd27d9392824cadfb239
`#Скачаются все книги, с 700 до 702 страницы`

### --dest_folder xxx

<<<<<<< HEAD
xxx - (bool, по умолчанию `False`) .

`python parse_tululu_category.py --dest_folder True`
=======
xxx - (bool, по умолчанию `False`).

`python parse_tululu_category.py --dest_folder True`

>>>>>>> 6debdbaf8c88df08b85fcd27d9392824cadfb239
`#Выдаст путь к файлу, где хранятся книги, обложки книг и файл с описанием книг`

### --skip_imgs xxx

xxx - (bool, по умолчанию `False`).

`python parse_tululu_category.py --skip_imgs True`
<<<<<<< HEAD
=======

>>>>>>> 6debdbaf8c88df08b85fcd27d9392824cadfb239
`#Не будет скачивать обложки книг`

### --skip_txt xxx

xxx - (bool, по умолчанию `False`).

`python parse_tululu_category.py --skip_txt True`
<<<<<<< HEAD
=======

>>>>>>> 6debdbaf8c88df08b85fcd27d9392824cadfb239
`#Не будет скачивать содержание книг`

### --json_path xxx

xxx - (str, по умолчанию `library.json`) имя файла, где будет хранится описание книг.

`python parse_tululu_category.py --json_path lib.json`
<<<<<<< HEAD
=======

>>>>>>> 6debdbaf8c88df08b85fcd27d9392824cadfb239
`#Описание книг будет сохранятся в файл 'lib.json'`

## Цель проекта

<<<<<<< HEAD
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
=======
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
>>>>>>> 6debdbaf8c88df08b85fcd27d9392824cadfb239

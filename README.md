# Парсер книг с сайта [tululu.org](http://tululu.org/)

Данный парсер предназначен для быстрого и эффективного поиска данных о книгах в жанре научной фантастики с сайта [tululu.org](http://tululu.org/). При этом вы можете скачивать их содержание и их обложки.

## Подготовка к запуску

Для запуска кода у вас уже должен быть установлен Python 3.

- Скачайте код.
- Установите нужные библиотеки командой `pip install -r requirements.txt`.
- Запутите код командой `python parse_tululu_category.py`.

**! Команда устанавливает все книги в жанре научной фантастики (прочитайте про аргументы). !**

## Аргументы

### --start_page xxx

xxx - (int, по умолчанию `0`, <702) страница, с которой начинается скачивание книг.

```sh
python parse_tululu_category.py --start_page 700
#Скачаются все книги, начиная с 700 страницы
```

### --end_page xxx

xxx - (int, по умолчанию `702`, <702) страница, до которой скачиваются книги.

```sh
python parse_tululu_category.py --end_page 701
#Скачаются все книги, до 702 страницы
```

```sh
python parse_tululu_category.py --start_page 700 --end_page 701
#Скачаются все книги, с 700 до 702 страницы
```

### --dest_folder xxx

xxx - (str, по умолчанию `''`).

```sh
python parse_tululu_category.py --dest_folder C:\Users\User\Devman\
#Содержание, описание и обложки книг будут сохраняться в папке C:\Users\User\Devman 
```

### --skip_imgs xxx

xxx - (bool, по умолчанию `False`).

```sh
python parse_tululu_category.py --skip_imgs True
#Не будет скачивать обложки книг
```

### --skip_txt xxx

xxx - (bool, по умолчанию `False`).

```sh
python parse_tululu_category.py --skip_txt True
#Не будет скачивать содержание книг
```

### --json_path xxx

xxx - (str, по умолчанию `library.json`) имя файла, где будет хранится описание книг.

```sh
python parse_tululu_category.py --json_path lib.json
#Описание книг будет сохраняться в файл 'lib.json'
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
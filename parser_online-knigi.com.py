import requests
from bs4 import BeautifulSoup
from pathlib import Path


def find_by_pattern(text, patterns={}, tag='div'):
    soup = BeautifulSoup(text, "lxml")
    return soup.find(tag, attrs=patterns)


def find_data(path):
    req = requests.get(path)
    req.encoding = "utf-8"
    book_name = list(find_by_pattern(
        req.text, {"class": "cont_h1"}).children)[0].text
    book_name = book_name.replace(", стр. 1", '')
    last_page_number = int(find_by_pattern(
        req.text, {"id": "spinner"}, tag="input")['max'])
    return book_name, last_page_number


# Задайте тут адресс книги на сайте online-knigi.com,
# запустите скрипт и наслаждайтесь книгой оффлайн
ADDRESS = 'https://online-knigi.com.ua/page/1'

BOOK_NAME, LAST_PAGE_NUMBER = find_data(ADDRESS)
path = Path.cwd() / 'files' / 'Parsers_gathered_info' / 'online-knigi.com'
if not path.exists():
    Path.mkdir(path, parents=True)
with open(path / (BOOK_NAME + '.txt'),
          'w', encoding='utf-8') as f:
    print(f'\033[35m-Привет Ангел. -Ура мама я в скрипте')
    print(f"Ангел: название книги - {BOOK_NAME}")
    print(f"Ангел: колличество страниц для скачивания - {LAST_PAGE_NUMBER}\033[0m")
    for n in range(1, LAST_PAGE_NUMBER + 1):
        print(f"\033[34mScraping of page {n} has started\033[0m")

        req = requests.get(f'{ADDRESS}?page={n}')
        req.encoding = "utf-8"
        main_text = find_by_pattern(req.text, {'class': "main_text"})
        for i in main_text.children:
            if i.name is not None:
                f.write(i.text + '\n\n')

        print(f"\033[34mScraping of page {n} has ended\033[0m")
    print(f"\033[35mАнгел: книга сохранена в папке {path}\033[0m")

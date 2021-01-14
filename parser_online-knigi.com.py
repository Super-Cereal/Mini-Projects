import requests
from bs4 import BeautifulSoup
from pathlib import Path


ADDRESS = 'https://online-knigi.com.ua/page/8'
BOOK_NAME = 'Wizards_first_rule'
LAST_PAGE_NUMBER = 205

path = Path.cwd() / 'files' / 'Parsers_gathered_info'
if not path.exists():
    Path.mkdir(path, parents=True)
with open(path / (BOOK_NAME + '.txt'),
          'w', encoding='utf-8') as f:
    print(f'\033[33m-Привет Ангел. -Ура мама я в скрипте\033[0m')
    for n in range(1, LAST_PAGE_NUMBER + 1):
        print(f"\033[34mScraping of page {n} has started\033[0m")

        req = requests.get(f'{ADDRESS}?page={n}')
        req.encoding = "utf-8"
        soup = BeautifulSoup(req.text, "lxml")
        main_text = soup.find("div", attrs={"class": "main_text"})
        for i in main_text.children:
            if i.name is not None:
                f.write(i.text + '\n\n')

        print(f"\033[34mScraping of page {n} has ended\033[0m")

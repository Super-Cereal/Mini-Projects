# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# мои данные
my_snils = "160-189-865 79"
my_points = 261
im_am_totally_in = [
    "09.03.01",
    "09.03.02",
    "10.03.01"
]
im_am_totally_not_in = [
        
]

# следующие данные перезатирают мои
I_AM_ELMIRA = False
if I_AM_ELMIRA:
    my_snils = "000-000-000 00"
    my_points = 264
    im_am_totally_in = [
        "09.03.01",
        "09.03.02",
        "10.03.01"
    ]
    im_am_totally_not_in = [
        
    ]

def log(text, my_file):
    print(text)
    my_file.write(text + '\n')

class Partner:
    def __init__(self, withOriginal, withAgreement, points, isMe = False) -> None:
        self.withOriginal = withOriginal
        self.withAgreement = withAgreement
        self.points = points
        self.isMe = isMe

def run():
    # здесь результаты
    my_file = open('elmira.md' if I_AM_ELMIRA else 'egor.md', 'w')

    # нужно установаить geсkodriver
    # (если нет FF - использовать webdriver.Chrome(), его тоже подкачать надо)
    driver = webdriver.Firefox()
    driver.get("http://priem.sut.ru/konkursnie-otbori")

    # получаем полюшки формы
    form = driver.find_element(By.TAG_NAME, "form")
    submit_button = form.find_element(By.CSS_SELECTOR, "input[type=submit]")
    organisation = Select(form.find_element(By.NAME, "general"))
    education_base = Select(form.find_element(By.NAME, "education_base_to"))
    education_distant = Select(form.find_element(By.NAME, "training_form"))
    education_money = Select(form.find_element(By.NAME, "training_type"))

    # заполняем данные формы
    organisation.select_by_visible_text('СПбГУТ')
    education_base.select_by_visible_text('Бакалавриат/Специалитет')
    education_distant.select_by_visible_text('Очное')
    education_money.select_by_visible_text('Бюджет')

    # субмитим форму
    submit_button.click()

    # каждая табличка - одна специальность
    tables = driver.find_elements(By.CSS_SELECTOR, "table.table")
    print("Начали смотреть таблички")
    for table in tables:
        rows = table.find_elements(By.CSS_SELECTOR, 'tr')

        headline = rows[0].text.split('\n')
        title = headline[0]
        common_seats = int(headline[1].split(':')[1])
        empty_seats = int(headline[2].split(':')[1])

        # фильтруем таблички, в котрых нас заведомо нет 
        flag = False
        for imIn in im_am_totally_in:
            if imIn in title:
                break
        else:
            continue

        for imNotIn in im_am_totally_not_in:
            if imNotIn in title:
                flag = True
                break
        if flag:
            continue
        # end фильтра

        partners = []
        global my_points
        im_with_agreement = False
        for row in rows:
            table_cells = row.find_elements(By.TAG_NAME, 'td')
            # table_cells = row.text.split()

            if len(table_cells) < 9: # это хедлайн чаще всего
                continue

            isMe = my_snils in table_cells[1].text
            withOriginal = 'Да' in table_cells[7].text
            withAgreement = 'Да' in table_cells[8].text
            points = int(table_cells[2].text)

            if isMe:
                # оно есть сверху, но на всякий случай
                my_points = points
                break

            if withOriginal or withAgreement:
                partners.append(Partner(withOriginal, withAgreement, points))
                pass
            else:
                break

        elephants_count = 0
        elephants_with_only_original_count = 0
        monkeys_count = 0
        monkeys_with_only_original_count = 0
        slugs_count = 0
        for partner in partners:
            if partner.points > my_points:
                elephants_count += 1
                if not partner.withAgreement:
                    elephants_with_only_original_count += 1
            elif partner.points == my_points:
                monkeys_count += 1
                if not partner.withAgreement:
                    monkeys_with_only_original_count += 1
            else:
                slugs_count += 1

        log('', my_file)
        log(f'### {title}', my_file)
        log(f'Мест к зачислению - {empty_seats}', my_file)
        log(f'Ты на {elephants_count + 1} месте среди подавших доки (из них {elephants_with_only_original_count} без заявления)', my_file)

        if monkeys_count:
            log(f'У {monkeys_count} такие же баллы как у тебя (из них {monkeys_with_only_original_count} без заявления) - они не учитывались при подсчете места', my_file)
        # log(f'Ты впереди {slugs_count} челов, крутой', my_file)

    driver.close()


if __name__ == "__main__":
    run()

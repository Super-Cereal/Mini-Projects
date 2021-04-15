first_dict = {
    "trainers": ["кроссовки"],
    "a fortune": ["состояние", "удача"],
    "allowers": ["карманные деньги"],
    "maintain": ["поддерживать", "обслуживать"]
}

x = set(first_dict.keys())

while x:
    key = x.pop()
    print(f'{key}:', end=' ')
    enter = input()
    if enter not in first_dict.get(key):
        print("\033[31mNah\033[0m")
        print(f'{key}: {first_dict.get(key)}')
        x.add(key)
print("\033[33mGreat job!\033[0m")


# в планах на будущее:
# прописывать словаря в файлах,
# принимать перевод из api -- яндекс теперь не выдают ключи, гугл тоже жлобы
# ...

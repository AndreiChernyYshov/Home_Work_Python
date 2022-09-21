def find(name):
    try:
        with open('directory.txt', 'r', encoding='utf-8') as data:
            for i in data:
                if i.find(name) != -1:
                    return i
            return f'Номер не найден'
    except FileNotFoundError:
        return 'В телефонном справочнике ничего не записано 0_0'


def write_down(number, name):
    try:
        with open('directory.txt', 'x', encoding='utf-8') as data:
            data.write(f'{number} - {name}\n')
            return f'Номер записан'
    except FileExistsError:
        with open('directory.txt', 'r+', encoding='utf-8') as data:
            for i in data:
                if i.find(number) != -1:
                    return f'Номер уже записан'
            data.write(f'{number} - {name}\n')
            return f'Номер записан'

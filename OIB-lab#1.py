'''
Шифр цезаря. Шаг по умолчанию = 0. Для кодирования используется алфавит русского языка + основные знаки препинания.
'''

# Исходный алфавит от а до ё и от ё до я + спец символы
alphabet = [chr(i) for i in range(ord('а'), ord('е') + 1)] + ['ё'] + [chr(i) for i in range(ord('ж'), ord('я') + 1)] + \
    [chr(i) for i in range(33, 65)]


def cesar_code(text: str, step: int = 0) -> str:
    for x in range(len(text)):
        if text[x].lower() in alphabet:
            # Ищем букву в исходном алфавите со сдвигом на step.
            # Для обработки переполнения используется % len(alp)
            temp = alphabet[(alphabet.index(text[x].lower()) + step) % len(alphabet)]
            # Если буква изначально была заглавной, то переводим temp в верхний регистр.
            if text[x].isupper():
                text = text[0:x] + text[x::].replace(text[x], temp.upper(), 1)
            else:
                text = text[0:x] + text[x::].replace(text[x], temp, 1)
    return text


def main():
    text = input("Введите строку для кодирования: ")
    steps = int(input("Введите шаг кодирования: "))
    coded_text = cesar_code(text, steps)
    print(f"Закодируем вашу фразу методом Цезаря и получим: {coded_text}")
    print(f"Дешифруем фразу обратно и получаем: {cesar_code(coded_text, -steps)}")


if __name__ == "__main__":
    main()

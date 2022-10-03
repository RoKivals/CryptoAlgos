import random

alphabet = "".join(chr(i).upper() + chr(i).lower() for i in range(ord('а'), ord('е') + 1)) + 'Ёё' + \
           "".join(chr(i).upper() + chr(i).lower() for i in range(ord('ж'), ord('я') + 1)) + \
           "".join(chr(i) for i in range(32, 65))


def get_contour() -> tuple:
    # Перемешиваем исходный алфавит с помощью sample без повторений
    coding_alp1 = "".join(i for i in random.sample(alphabet, len(alphabet)))
    coding_alp2 = "".join(i for i in random.sample(alphabet, len(alphabet)))
    coding_alp3 = "".join(i for i in random.sample(alphabet, len(alphabet)))
    # Кортеж перемешанных алфавитов, они не изменяются, для экономии памяти используется кортеж
    coding = (coding_alp1, coding_alp2, coding_alp3)
    return coding





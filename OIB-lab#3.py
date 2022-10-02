import random
from constants import *

contour1 = ("".join(i for i in random.sample(alphabet, len(alphabet))),
            "".join(i for i in random.sample(alphabet, len(alphabet))),
            "".join(i for i in random.sample(alphabet, len(alphabet))))
contour2 = ("".join(i for i in random.sample(alphabet, len(alphabet))),
            "".join(i for i in random.sample(alphabet, len(alphabet))),
            "".join(i for i in random.sample(alphabet, len(alphabet))))
contour3 = ("".join(i for i in random.sample(alphabet, len(alphabet))),
            "".join(i for i in random.sample(alphabet, len(alphabet))),
            "".join(i for i in random.sample(alphabet, len(alphabet))))

arr_contour = (contour1, contour2, contour3)


# code_type - тип функции (0 - шифрование, !0 - дешифрование)
def encryption(text: str, sequence: list, period: list, code_type=0) -> str:
    num_of_contour = 0
    curr_period = period[num_of_contour]
    flag = 0
    for i in range(len(text)):
        if curr_period == 0:
            num_of_contour = (num_of_contour + 1) % len(sequence)
            curr_period = period[num_of_contour]
            flag = 0
        if code_type == 0:
            text = text[0:i] + text[i::].replace(text[i],
                                                 arr_contour[sequence[num_of_contour]]
                                                 [flag % len(arr_contour[num_of_contour])][alphabet.index(text[i])], 1)
        else:
            text = text[0:i] + text[i::].replace(text[i],
                                                 alphabet[arr_contour[sequence[num_of_contour]]
                                                 [flag % len(arr_contour[num_of_contour])][alphabet.index(text[i])]], 1)
        curr_period -= 1
        flag += 1
    return text


def main():
    text = input("Введите сообщение для шифрования: ")
    sequence = [int(i) for i in input("Введите порядок использования контуров").strip().split()]
    period = [int(i) for i in input("Введите период использования каждого контура").strip().split()]
    coded_text = encryption(text, sequence, period)
    print(f"Зашифрованное сообщение имеет вид: {coded_text}")
    print(f"Дешифрованное сообщение имеет вид: {encryption(coded_text, sequence, period, -1)}")


if __name__ == "__main__":
    main()

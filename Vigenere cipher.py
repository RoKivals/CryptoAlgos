import numpy as np
from constants import *

alp_matrix = np.array([])
for i in range(len(alphabet)):
    curr_alp = alphabet[i:] + alphabet[0:i]
    alp_matrix = np.append(alp_matrix, np.array(curr_alp))


def encryption(text: str, key: str, code_type=0):
    # Увеличиваем ключ до длины исходного сообщения
    key = "".join(key[i % len(key)] for i in range(len(text)))
    for i in range(len(text)):
        # Первая строка и первый столбец (по которым определяется пересечение идентчины исходному алфавиту
        if code_type == 0:
            temp = alp_matrix[alphabet.index(key[i])][alphabet.index(text[i])]
        else:
            row = alphabet.index(key[i])
            temp = alphabet[alp_matrix[row].index(text[i])]
        text = text[0:i] + text[i::].replace(text[i], temp, 1)
    return text


def main():
    text = input("Введите сообщение для шифрования: ")
    key = input("Введите ключ-фразу. Помните, что её символы не должны повторяться!\n")
    coded_text = encryption(text, key)
    print(f"Зашифрованное сообщение имеет вид: {coded_text}")
    print(f"Дешифрованное сообщение имеет вид: {encryption(coded_text, key, -1)}")


if __name__ == "__main__":
    main()

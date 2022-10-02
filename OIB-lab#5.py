import numpy as np
import math


def create_table(symbols: int, length: int):
    rows = math.ceil(symbols / length)
    table = np.zeros((rows, length), dtype=str)
    return table


def fill_table(table, text: str):
    curr_id = 0
    for x in range(len(table)):
        for i in range(len(table[x])):
            if curr_id < len(text):
                table[x][i] = text[curr_id]
            else:
                table[x][i] = ''
            curr_id += 1
    return table


def encryption(table, sequence: str) -> str:
    coded_str = ''
    for i in sequence:
        coded_str += "".join(i for i in table[:, (int(i) - 1)])
    return coded_str


def decryption(coded_text: str, sequence: str) -> str:
    table = create_table(len(coded_text), len(sequence))
    rows = table.shape[0]
    full_col = len(coded_text) % len(sequence)
    for i in sequence:
        if full_col == 0 or int(i) <= full_col:
            table[0:, int(i) - 1] = [i for i in coded_text[0:rows]]
            coded_text = coded_text[rows::]
        else:
            table[0:, int(i) - 1] = [i for i in coded_text[0:rows - 1]] + ['']
            coded_text = coded_text[rows - 1::]
    result = ''
    for i in table:
        result += ''.join(str(x) for x in i)
    return result


def main():
    text = input("Введите сообщение для шифрования: ")
    key = input("Введите ключ-фразу. Помните, что её символы не должны повторяться!\n")
    table = create_table(len(text), len(key))
    coded_text = encryption(fill_table(table, text), key)
    print(f"Зашифрованное сообщение имеет вид: {coded_text}")
    print(f"Дешифрованное сообщение имеет вид: {decryption(coded_text, key)}")


if __name__ == "__main__":
    main()

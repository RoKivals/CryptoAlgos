import numpy as np
import math


def create_table(symbols: int, length: int, vacuum_len: int):
    rows = math.ceil((symbols + vacuum_len) / length)
    table = np.zeros((rows, length), dtype=str)
    return table


def fill_table(table: np.ndarray, text: str, vacuum_coords: list):
    curr_id = 0
    for x in range(len(table)):
        for i in range(len(table[x])):
            if [x, i] in vacuum_coords:
                pass
            else:
                if curr_id < len(text):
                    table[x][i] = text[curr_id]
                else:
                    table[x][i] = ''
                curr_id += 1
    return table


def encryption(table: np.ndarray, sequence: str, vacuum_coord: list) -> str:
    coded_str = ''
    for i in range(1, len(sequence) + 1):
        col_ind = sequence.index(str(i))
        for x in range(len(table[:, col_ind])):
            if [x, col_ind] in vacuum_coord:
                pass
            else:
                coded_str += table[x][col_ind]
    return coded_str


'''
1) Смотрим кол-во полных столбцов.
2) Идём по ключу от 1 до len(sequence), смотрим, полный ли столбец.
3) Прописываем столбец в пустой строке, учитывай пустые ячейки.
4) Собираем строку слева направо сверху вниз в одну строку (обратно для fill_table)
'''


def decryption(coded_text: str, sequence: str, vacuum_coords: list) -> str:
    table = create_table(len(coded_text), len(sequence), len(vacuum_coords))
    rows = table.shape[0]
    full_col = (len(coded_text) + len(vacuum_coords)) % len(sequence)
    for i in range(1, len(sequence) + 1):
        dots = 0
        curr_col = sequence.index(str(i))
        for x in range(rows):
            if [x, curr_col] in vacuum_coords:
                dots += 1
        if full_col == 0 or curr_col <= full_col - 1:
            for x in range(rows):
                if [x, curr_col] in vacuum_coords:
                    table[x][curr_col] = ''
                    dots -= 1
                else:
                    table[x][curr_col] = coded_text[0]
                    coded_text = coded_text[1::]
        else:
            for x in range(rows - 1):
                if [x, curr_col] in vacuum_coords:
                    dots -= 1
                    table[x][curr_col] = ''
                else:
                    table[x][curr_col] = coded_text[0]
                    coded_text = coded_text[1::]
            table[rows - 1][curr_col] = ''
        while dots:
            for x in range(rows):
                if [x, curr_col] in vacuum_coords:
                    table[x][curr_col] = ''
    print(table)
    result = ''
    for i in table:
        result += ''.join(str(x) for x in i)
    return result


def main():
    text = input("Введите сообщение для шифрования: ")
    key = input("Введите ключ-фразу. Помните, что её символы не должны повторяться!\n")
    count_dots = int(input("Введите кол-во пустых ячеек в таблице: "))
    vacuum_coords = []
    for i in range(count_dots):
        vacuum_coords += [[int(x) for x in input(f"Введите координаты {i + 1} точки: ").strip().split(' ')]]
    table = create_table(len(text), len(key), len(vacuum_coords))
    coded_text = encryption(fill_table(table, text, vacuum_coords), key, vacuum_coords)
    print(f"Зашифрованное сообщение имеет вид: {coded_text}")
    print(f"Дешифрованное сообщение имеет вид: {decryption(coded_text, key, vacuum_coords)}")


if __name__ == "__main__":
    main()

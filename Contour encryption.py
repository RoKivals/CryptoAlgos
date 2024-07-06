from constants import *

coding = get_contour()


def encryption(text: str) -> str:
    flag = 0  # текущий номер алфавита в контуре [0;2]
    for i in range(len(text)):
        # Заменяем только 1 символ, сохраняя все предшествующие символы
        alp_num = flag % len(coding)
        new_sym = coding[alp_num][alphabet.index(text[i])]
        text = text[0:i] + text[i::].replace(text[i], new_sym, 1)
        flag += 1
    return text


def decryption(text: str) -> str:
    flag = 0  # текущий номер алфавита в контуре [0;2]
    for i in range(len(text)):
        alp_num = flag % len(coding)
        new_sym = alphabet[coding[alp_num].index(text[i])]
        text = text[0:i] + text[i::].replace(text[i], new_sym, 1)
        flag += 1
    return text


def main():
    text = input("Введите сообщение для шифрования: ")
    coded_text = encryption(text)
    print(f"Зашифрованное сообщение имеет вид: {coded_text}")
    print(f"Дешифрованное сообщение имеет вид: {decryption(coded_text)}")


if __name__ == "__main__":
    main()

from random import choice
from string import ascii_letters


def encryption(text: str, key: str) -> str:
    for i in range(len(text)):
        t = text[i]
        k = key[i]
        temp = chr(ord(t) ^ ord(k))
        text = text[0:i] + text[i::].replace(text[i], temp, 1)
    return text


def main():
    text = input("Введите сообщение для шифрования: ")
    key = ''.join(choice(ascii_letters) for _ in range(len(text)))
    coded_text = encryption(text, key)
    print(f"Зашифрованное сообщение имеет вид: {coded_text}")
    print(f"Дешифрованное сообщение имеет вид: {encryption(coded_text, key)}")


if __name__ == "__main__":
    main()

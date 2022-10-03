import random
from constants import *


coding_alp1 = "".join(i for i in random.sample(alphabet, len(alphabet)))
coding_alp2 = "".join(i for i in random.sample(alphabet, len(alphabet)))
coding_alp3 = "".join(i for i in random.sample(alphabet, len(alphabet)))
coding = (coding_alp1, coding_alp2, coding_alp3)


def encryption(text: str, code_type=0) -> str:
    flag = 0
    for i in range(len(text)):
        if code_type == 0:
            text = text[0:i] + text[i::].replace(text[i], coding[flag % len(coding)][alphabet.index(text[i])], 1)
        else:
            text = text[0:i] + text[i::].replace(text[i], alphabet[coding[flag % len(coding)][alphabet.index(text[i])]], 1)
        flag += 1
    return text


def main():
    text = input("Введите сообщение для шифрования: ")
    coded_text = encryption(text)
    print(f"Зашифрованное сообщение имеет вид: {coded_text}")
    print(f"Дешифрованное сообщение имеет вид: {encryption(coded_text, -1)}")


if __name__ == "__main__":
    main()

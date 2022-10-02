alphabet = "".join(chr(i).upper() + chr(i).lower() for i in range(ord('а'), ord('е') + 1)) + 'Ёё' + \
           "".join(chr(i).upper() + chr(i).lower() for i in range(ord('ж'), ord('я') + 1)) + \
           "".join(chr(i) for i in range(32, 65))
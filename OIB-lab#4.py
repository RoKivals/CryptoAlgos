import numpy as np

alphabet = "".join(chr(i).upper() + chr(i).lower() for i in range(ord('а'), ord('е') + 1)) + 'Ёё' + \
           "".join(chr(i).upper() + chr(i).lower() for i in range(ord('ж'), ord('я') + 1)) + \
           "".join(chr(i) for i in range(33, 65))

alp_matrix = np.array([])
for i in range(len(alphabet)):
    curr_alp = alphabet[i:] + alphabet[0:i]
    alp_matrix = np.append(alp_matrix, np.array(curr_alp))


print(alp_matrix)

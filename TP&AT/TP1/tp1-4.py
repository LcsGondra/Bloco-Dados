palind = ['radar', 'toot', 'bsalbsal', 'Socorram-me subi no ônibus em marrocos']

import re

for i in palind:
    p = i.lower()
    pattern = '[^A-Za-z0-9]+'
    p = re.sub(pattern, '', p)
    print(f'{i} eh um palindromo? {p == p[::-1]}')
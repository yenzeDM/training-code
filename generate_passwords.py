import random
import string
import re
STRING = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
PATTERN = r'[A-Z]+[a-z]+[0-9]+'


def generate_password(length):
    while True:
        tmp = ''.join(random.sample(STRING, length))
        if re.findall(PATTERN, tmp):
            return tmp


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')

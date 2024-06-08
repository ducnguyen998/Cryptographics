#
# Hệ mật dịch chuyển
#

import random
import string

char_list = list(string.ascii_lowercase)

class ShiftCipher:
    def __init__(self, k = None):
        if k is None:
            k = random.randint(0, 25)
        self.k = k
    
    def encrypt(self, x):
        y = ''
        for x_i in x:
            x_i_key = x_i
            x_i_value = char_list.index(x_i_key)
            y_i_value = (x_i_value + self.k) % 26
            y_i_key = char_list[y_i_value]
            y += y_i_key
        return y
    def decrypt(self, y):
        x = ''
        for y_i in y:
            y_i_key = y_i
            y_i_value = char_list.index(y_i_key)
            x_i_value = (y_i_value - self.k) % 26
            x_i_key = char_list[x_i_value]
            x += x_i_key
        return x
    
def main():
    cipher = ShiftCipher(k=4)
    x = 'hello'
    y = cipher.encrypt(x)
    print(f'Encript : {x} -> {y}')
    x = cipher.decrypt(y)
    print(f'Decript : {y} -> {x}')

if __name__ == '__main__':
    main()
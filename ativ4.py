# -*- coding: utf-8 -*-
def is_primo(value):
  if value < 2:
    return False
  else:
    for i in range(2, value):
        if value % i == 0:
          return False
        else:
          return True

for n in range(1,101):
  if is_primo(n):
    print('%i é primo.' % n)
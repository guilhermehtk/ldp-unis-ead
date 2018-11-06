# -*- coding: utf-8 -*-
value_a = int(input('A: '))
value_b = int(input('B: '))
value_c = int(input('C: '))

if value_a < value_b and value_a < value_c:
  print('Menor: %i' % value_a)
elif value_b < value_a and value_b < value_c:
  print('Menor: %i' % value_b)
elif value_c < value_b and value_c < value_a:
  print('Menor: %i' % value_c)
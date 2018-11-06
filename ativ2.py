# -*- coding: utf-8 -*-
value_a = float(input('A: '))
value_b = float(input('B: '))
value_c = float(input('C: '))

if value_a+value_b > value_c \
and value_a+value_c > value_a \
and value_a+value_c > value_b:
  semi = (value_a+value_b+value_c)/2
  area = (semi*(semi-value_a)*(semi-value_b)*(semi-value_c)) ** 0.5
  print 'Area do triangulo: %0.2f' % area
else:
  print 'A: %0.2f, B: %0.2f, C: %0.2f' % (value_a, value_b, value_c)

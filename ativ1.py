# -*- coding: utf-8 -*-
age_in_days = input('Digite sua idade em dias: ')
age_in_years = age_in_days/365.25
months_over = (age_in_days - (int(age_in_years)*365.25))/30
days_over = age_in_days - (int(age_in_years)*365.25) - (int(months_over)*30)
print('Você possuui %i anos, %i meses e %i dias de idade' % (age_in_years, months_over, days_over))

# A timestamp is three numbers: a number of hours, minutes and seconds.
# Given two timestamps, calculate how many seconds is between them. The
# moment of the first timestamp occurred before the moment of the second
# timestamp. (На английском языке что бы Вы научились понимать 6, 1, 30, 6, 2, 10 result 40 sec.)

h, m, s = int(input('chasy ')), int(input('minuty ')), int(input('sekundy '))
h2, m2, s2 = int(input('chasy2 ')), int(input('minuty2 ')), int(input('sekundy2 '))
raznica = print(f'{h-h2} : {m-m2} : {s-s2}')
raznica_v_sec = print('Разница в секундах',(h-h2)*3600 + (m-m2)*60 + (s-s2))
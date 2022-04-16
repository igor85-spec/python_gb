a = input('Enter duration in sec: ')
a = int(a)
if a < 60:
    print('duration = ', a, 'cек')
elif a < 3600:
    b = a // 60
    c = a % 60
    print ('duration = ', b, 'мин', c, 'сек')
elif a < 86400:
    b = a // 3600
    c = a % 3600
    d = c // 60
    e = c % 60
    print ('duration = ', b, 'час', d, 'мин', e, 'cек')
elif a > 86400:
    b = a // 86400
    c = a % 86400
    d = c // 3600
    e = c % 3600
    f = e // 60
    g = e % 60
    print ('duration = ', b, 'дн', d, 'час', f, 'мин', g, 'cек')


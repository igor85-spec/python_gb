
d_percent = 'процент'
count = 1

while count <= 100:
    if count > 4 and count < 20:
        print(count, d_percent + 'ов')
    elif count % 10 == 1:
        print(count, d_percent)
    elif count % 10 == 2 or count % 10 == 3 or count % 10 == 4:
        print (count, d_percent + 'a')
    else:
        print (count, d_percent + 'ов')
    count += 1

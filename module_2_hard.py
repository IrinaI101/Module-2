n = int(input('Введите целое число от 3 до 20: '))
if 3 <= n <= 20:
    result = ''
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    print('Пароль: ', result)
else:
    print('Число не подходит')






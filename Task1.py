def card(number):
    num = ''
    if number.isdigit:
        for i in range(0, len(number)-4):
            num += '*'
        for i in range(len(number)-4, len(number)):
            num += number[i]
        print(num)
    else:
        print('Eror')
card(input('Введите номер карты: '))


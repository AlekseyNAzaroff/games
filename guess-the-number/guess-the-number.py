import random

print()
print()
print('''Добро пожаловать в числовую угадайку!
Вы можете выбрать из какого диапазона чисел будете угадывать,
просто выберете верхнюю границу.''')
print()


def main():
    x = int(input('Итак, введите число: '))
    num = random.randint(1, x)
    counter = 0

    def is_valid(answer):
        if answer.isdigit() and 0 < int(answer) < x + 1:
            return True
        else:
            return False

    while True:
        answer = input('Какое число я загадал? Твой вариант: ')
        counter += 1
        if is_valid(answer) == False:
            print(f'А может быть все-таки введем целое число от 1 до {x}')
            continue
        else:
            answer = int(answer)
            if num > answer:
                print('Твоё число МЕНЬШЕ загаданного, думай лучше =)')
                print()
            elif num < answer:
                print('Твоё число БОЛЬШЕ загаданного, думай лучше =)')
                print()
            else:
                print(
                    f'Ты угадал, поздравляю! Тебе потребовалось не больше '
                    f'{counter} попыток')
                print(
                    'Если хочешь сыграть еще, нажми "+", для выхода нажми "-"')
                result = input('+ или -: ')
                if result == '+':
                    main()
                else:
                    print('До новых встреч, подлец!')
                    break


if __name__ == '__main__':
    main()

import random


class Coin:
    def __init__(self):
        self.__sideup = 'Орел'

    def drop(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    def get_sideup(self):
        return f'{self.__sideup}'


def main():
    my_coin = Coin()
    print(f'Сейчас монета обращена стороной: {my_coin.get_sideup()}')

    print(f'Бросаю монету...')
    flip(my_coin)

    print(f'Монета упала на сторону: {my_coin.get_sideup()}')


def flip(coin_obj):
    coin_obj.drop()


if __name__ == '__main__':
    main()

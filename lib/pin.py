import wiringpi as gpio


class Pin:
    def __init__(self, pin_num: int):
        self.__pin_num = pin_num

        gpio.pinMode(self.__pin_num, 1)

    def on(self):
        gpio.digitalWrite(self.__pin_num, 1)

    def off(self):
        gpio.digitalWrite(self.__pin_num, 0)

    def __del__(self):
        pass

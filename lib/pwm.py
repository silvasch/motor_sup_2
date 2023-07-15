import wiringpi as gpio


class PWM:
    def __init__(
        self, pin_num: int, frequency: int = 100, initial_duty_cycle: int = 100
    ):
        self.__pin_num = pin_num
        self.__frequency = frequency
        self.__duty_cycle = initial_duty_cycle

        gpio.pinMode(self.__pin_num, 2) # 2: pwm

    def on(self, duty_cycle: float = 100):
        self.__duty_cycle = duty_cycle
        self.write()

    def off(self):
        self.__duty_cycle = 0
        self.write()

    def set_duty_cycle(self, duty_cycle: float):
        self.__duty_cycle = duty_cycle
        self.write()

    def write(self):
        gpio.pwmWrite(self.__pin_num, PWM.duty_cycle(self.__duty_cycle))
        
    @staticmethod
    def duty_cycle(duty_cycle: float) -> int:
        int(duty_cycle / 100 * 1024)

    def __del__(self):
        pass

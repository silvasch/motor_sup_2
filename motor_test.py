import wiringpi as gpio

from lib import Motor


def main():
    gpio.wiringPiSetupPhys()

    motor = Motor(data_1=2, data_2=3, enable=4, frequency=50)

    motor.forwards()

    try:
        while True:
            duty_cycle = float(input("Duty cycle: "))
            motor.change_duty_cylce(duty_cycle)
    except KeyboardInterrupt:
        del motor


if __name__ == "__main__":
    main()

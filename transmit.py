import time
import sys
import RPi.GPIO as GPIO


off = '1010010101100101100101101010011001010101010101010110101010100101' 
on = '1010010101100101100101101010011001010101010101010110100110100101'
test = '1010101010101010101010101'
onehigh = 0.0002
onelow = 0.0003
zerohigh = onehigh
zerolow = 0.0014
intro = 0.003
pause = 0.01029

NUM_ATTEMPTS = 10
TRANSMIT_PIN = 17

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    GPIO.output(TRANSMIT_PIN, 0)
    for t in range(NUM_ATTEMPTS):
        GPIO.output(TRANSMIT_PIN, 1)
        time.sleep(onehigh)
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(intro)
        for i in code:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(onehigh)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(onelow)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(zerohigh)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(zerolow)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 1)
        time.sleep(onehigh)
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(pause)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')


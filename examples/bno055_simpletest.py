# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import adafruit_bno055

import time

import serial

# Define the serial connection
uart = serial.Serial('/dev/serial0', 115200)

# Create an instance of the BNO055 sensor using UART
sensor = adafruit_bno055.BNO055_UART(uart)

# If you are going to use UART uncomment these lines
# uart = board.UART()
# sensor = adafruit_bno055.BNO055_UART(uart)

last_val = 0xFFFF


def temperature():
    global last_val  # pylint: disable=global-statement
    result = sensor.temperature
    if abs(result - last_val) == 128:
        result = sensor.temperature
        if abs(result - last_val) == 128:
            return 0b00111111 & result
    last_val = result
    return result


while True:

    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    print()

    time.sleep(1)

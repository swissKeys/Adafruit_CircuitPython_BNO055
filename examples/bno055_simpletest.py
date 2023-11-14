# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import adafruit_bno055

import time

import serial

# Define the serial connection
uart = serial.Serial('/dev/serial0', 115200)

# Create an instance of the BNO055 sensor using UART
sensor = adafruit_bno055.BNO055_UART(uart, rst_pin=18)

# If you are going to use UART uncomment these lines
# uart = board.UART()
# sensor = adafruit_bno055.BNO055_UART(uart)

last_val = 0xFFFF


while True:

    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    print()

    time.sleep(1)
